import unittest
from unittest.mock import MagicMock, patch
from datetime import datetime, timedelta
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, QDate
import sys
from backend import Backend
from admin_panel import AdminPanel
from customer_panel import CustomerPanel, RoomCard
from main import HotelBookingSystem

class TestBackend(unittest.TestCase):
    def setUp(self):
        self.backend = Backend()
        # Create a mock database connection
        self.backend.db = MagicMock()

    def test_get_users(self):
        mock_users = [
            (1, "Ralph", "ralph@slu.edu", "Guest", "Active"),
            (2, "Joli", "joli@slu.edu", "Guest", "Active")
        ]
        self.backend.db.get_all_users.return_value = mock_users
        users = self.backend.get_users()
        self.assertEqual(users, mock_users)
        self.backend.db.get_all_users.assert_called_once()

    def test_add_user(self):
        self.backend.add_user("Test User", "test@example.com", "Guest")
        self.backend.db.add_user.assert_called_once_with(
            "Test User", "test@example.com", "Guest", "Active"
        )

    def test_delete_user(self):
        user_id = 1
        self.backend.delete_user(user_id)
        self.backend.db.delete_user.assert_called_once_with(user_id)

    def test_get_available_rooms(self):
        mock_rooms = [
            (101, "101", "Standard", 100.0, "Available"),
            (102, "102", "Deluxe", 150.0, "Available")
        ]
        test_date = "2024-12-10"
        self.backend.db.get_available_rooms.return_value = mock_rooms
        rooms = self.backend.get_available_rooms(test_date)
        self.assertEqual(rooms, mock_rooms)
        self.backend.db.get_available_rooms.assert_called_once_with(test_date)

    def test_book_room(self):
        room_id = 101
        check_in = "2024-12-10"
        check_out = "2024-12-11"
        user_name = "Test User"
        self.backend.book_room(room_id, check_in, check_out, user_name)
        self.backend.db.add_booking.assert_called_once_with(
            room_id, check_in, check_out, user_name
        )

class TestAdminPanel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)

    def setUp(self):
        self.user_data = {"username": "admin", "is_admin": True}
        self.admin_panel = AdminPanel(self.user_data)
        self.admin_panel.backend = MagicMock()

    def test_load_bookings(self):
        mock_bookings = [
            (1, "101", "Standard", "2024-12-10", "2024-12-11", "Test User")
        ]
        self.admin_panel.backend.get_all_bookings.return_value = mock_bookings
        self.admin_panel.load_bookings()
        
        # Verify table contents
        self.assertEqual(self.admin_panel.bookings_table.rowCount(), len(mock_bookings))
        for col in range(6):
            item = self.admin_panel.bookings_table.item(0, col)
            self.assertEqual(item.text(), str(mock_bookings[0][col]))

    def test_load_users(self):
        mock_users = [
            (1, "Test User", "test@example.com", "Guest", "Active")
        ]
        self.admin_panel.backend.get_all_users.return_value = mock_users
        self.admin_panel.load_users()
        
        # Verify table contents
        self.assertEqual(self.admin_panel.users_table.rowCount(), len(mock_users))
        for col in range(5):
            item = self.admin_panel.users_table.item(0, col)
            self.assertEqual(item.text(), str(mock_users[0][col]))

class TestCustomerPanel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)

    def setUp(self):
        self.user_data = {"username": "test_user"}
        self.customer_panel = CustomerPanel(self.user_data)
        self.customer_panel.backend = MagicMock()

    def test_show_available_rooms(self):
        mock_rooms = [
            (101, "101", "Standard", 100.0, "Available"),
            (102, "102", "Deluxe", 150.0, "Available")
        ]
        self.customer_panel.backend.get_available_rooms.return_value = mock_rooms
        
        # Set a test date
        test_date = QDate(2024, 12, 10)
        self.customer_panel.check_in_calendar.setSelectedDate(test_date)
        
        self.customer_panel.show_available_rooms()
        
        # Verify table contents
        self.assertEqual(self.customer_panel.rooms_table.rowCount(), len(mock_rooms))
        for row in range(len(mock_rooms)):
            for col in range(3):  # Checking only first 3 columns (excluding action button)
                item = self.customer_panel.rooms_table.item(row, col)
                self.assertEqual(item.text(), str(mock_rooms[row][col]))

class TestRoomCard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)

    def test_room_card_creation(self):
        room_type = "Deluxe"
        price = 150
        features = ["King Size Bed", "Ocean View", "Mini Bar"]
        
        room_card = RoomCard(room_type, price, features)
        
        # Find labels in the room card
        labels = room_card.findChildren(QtWidgets.QLabel)
        
        # Verify room type label
        self.assertTrue(any(label.text() == room_type for label in labels))
        
        # Verify price label
        self.assertTrue(any(label.text() == f"${price}/night" for label in labels))
        
        # Verify feature labels
        for feature in features:
            self.assertTrue(any(label.text() == f"• {feature}" for label in labels))

class TestHotelBookingSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)

    def setUp(self):
        self.window = HotelBookingSystem()
        # Mock the login dialog
        self.window.user_data = {"username": "test_user", "is_admin": True}
        self.window.setup_ui()

    def test_panel_switching(self):
        # Test switching to admin panel
        self.window.show_admin_panel()
        self.assertEqual(self.window.stacked_widget.currentIndex(), 1)
        self.assertEqual(self.window.statusBar().currentMessage(), "Admin Panel")
        
        # Test switching to customer panel
        self.window.show_customer_panel()
        self.assertEqual(self.window.stacked_widget.currentIndex(), 0)
        self.assertEqual(self.window.statusBar().currentMessage(), "Customer Panel")

    def test_menubar_actions(self):
        # Find and test the logout action
        logout_action = next(action for action in self.window.findChildren(QAction) 
                           if action.text() == "Logout")
        self.assertIsNotNone(logout_action)
        
        # Find and test the exit action
        exit_action = next(action for action in self.window.findChildren(QAction) 
                          if action.text() == "Exit")
        self.assertIsNotNone(exit_action)

if __name__ == '__main__':
    unittest.main()
