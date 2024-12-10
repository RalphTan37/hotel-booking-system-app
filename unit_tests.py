import unittest
from unittest.mock import MagicMock, patch
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, QDate
import sys
from backend import Backend
from admin_panel import AdminPanel
from customer_panel import CustomerPanel
from main import HotelBookingSystem

class TestHotelManagementSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)
        cls.backend = Backend()
        cls.backend.db = MagicMock()  # Mock database connection

    def test_room_booking_flow(self):
        """Test the complete room booking process from availability check to confirmation"""
        # Setup
        customer_panel = CustomerPanel({"username": "test_user"})
        customer_panel.backend = self.backend
        test_date = "2024-12-10"
        
        # Mock available rooms
        mock_rooms = [(101, "101", "Standard", 100.0, "Available")]
        self.backend.db.get_available_rooms.return_value = mock_rooms
        
        # Test room availability check
        customer_panel.check_in_calendar.setSelectedDate(QDate.fromString(test_date, "yyyy-MM-dd"))
        customer_panel.show_available_rooms()
        
        # Verify room display
        self.assertEqual(customer_panel.rooms_table.rowCount(), 1)
        self.assertEqual(customer_panel.rooms_table.item(0, 0).text(), "101")
        
        # Test room booking
        self.backend.book_room(101, test_date, test_date, "test_user")
        self.backend.db.add_booking.assert_called_once()

    def test_user_management(self):
        """Test user creation, retrieval, and deletion functionality"""
        # Mock users data
        mock_users = [(1, "Test User", "test@example.com", "Guest", "Active")]
        self.backend.db.get_all_users.return_value = mock_users
        
        # Test user retrieval
        users = self.backend.get_users()
        self.assertEqual(users, mock_users)
        
        # Test user addition
        self.backend.add_user("New User", "new@example.com", "Guest")
        self.backend.db.add_user.assert_called_once_with(
            "New User", "new@example.com", "Guest", "Active"
        )
        
        # Test user deletion
        self.backend.delete_user(1)
        self.backend.db.delete_user.assert_called_once_with(1)

    def test_admin_panel_functionality(self):
        """Test core admin panel features including booking and user management"""
        # Setup
        admin_panel = AdminPanel({"username": "admin", "is_admin": True})
        admin_panel.backend = self.backend
        
        # Mock data
        mock_bookings = [(1, "101", "Standard", "2024-12-10", "2024-12-11", "Test User")]
        mock_users = [(1, "Test User", "test@example.com", "Guest", "Active")]
        
        self.backend.db.get_all_bookings.return_value = mock_bookings
        self.backend.db.get_all_users.return_value = mock_users
        
        # Test booking management
        admin_panel.load_bookings()
        self.assertEqual(admin_panel.bookings_table.rowCount(), 1)
        
        # Test user management
        admin_panel.load_users()
        self.assertEqual(admin_panel.users_table.rowCount(), 1)

    def test_system_authentication(self):
        """Test system login and role-based access control"""
        # Create main window with admin user
        window = HotelBookingSystem()
        window.user_data = {"username": "admin", "is_admin": True}
        window.setup_ui()
        
        # Verify admin has access to both panels
        self.assertTrue(hasattr(window, 'admin_panel'))
        self.assertTrue(hasattr(window, 'customer_panel'))
        
        # Create main window with regular user
        window = HotelBookingSystem()
        window.user_data = {"username": "user", "is_admin": False}
        window.setup_ui()
        
        # Verify regular user only has access to customer panel
        self.assertFalse(hasattr(window, 'admin_panel'))
        self.assertTrue(hasattr(window, 'customer_panel'))

    def test_room_availability_system(self):
        """Test the room availability and booking status management"""
        test_date = "2024-12-10"
        
        # Mock available rooms
        mock_rooms = [
            (101, "101", "Standard", 100.0, "Available"),
            (102, "102", "Deluxe", 150.0, "Occupied")
        ]
        self.backend.db.get_available_rooms.return_value = mock_rooms
        
        # Test availability check
        available_rooms = self.backend.get_available_rooms(test_date)
        self.assertEqual(len(available_rooms), 2)
        
        # Test booking status update
        room_id = 101
        self.backend.book_room(room_id, test_date, test_date, "test_user")
        self.backend.db.add_booking.assert_called_once_with(
            room_id, test_date, test_date, "test_user"
        )

if __name__ == '__main__':
    unittest.main()
