import unittest
from unittest.mock import Mock
from backend import Backend 
from database import Database

class UnitTests(unittest.TestCase):

    def setUp(self):
        #Mock the Database class
        self.mock_db = Mock(spec=Database)
        self.backend = Backend()
        self.backend.db = self.mock_db

    def test_add_user(self):
        #Test that adding a user works correctly
        self.backend.add_user("John Doe", "johndoe@example.com", "customer")
        self.mock_db.add_user.assert_called_with("John Doe", "johndoe@example.com", "customer", "Active")

    def test_get_users(self):
        #Test retrieving all users
        self.mock_db.get_all_users.return_value = [
            {"name": "John Doe", "email": "johndoe@example.com", "role": "customer", "status": "Active"},
            {"name": "Jane Smith", "email": "janesmith@example.com", "role": "admin", "status": "Active"}
        ]
        
        users = self.backend.get_users()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0]["name"], "John Doe")
        self.assertEqual(users[1]["email"], "janesmith@example.com")

    def test_delete_user(self):
        #Test deleting a user by email
        self.mock_db.delete_user.return_value = None
        self.backend.delete_user("johndoe@example.com")
        self.mock_db.delete_user.assert_called_with("johndoe@example.com")
    
    def test_get_available_rooms(self):
        #Test getting available rooms
        self.mock_db.get_available_rooms.return_value = [101, 103]
        available_rooms = self.backend.get_available_rooms("2024-12-20")
        self.assertEqual(available_rooms, [101, 103])

    def test_book_room(self):
        #Test booking a room
        self.mock_db.add_booking.return_value = None
        self.mock_db.get_all_bookings.return_value = [
            {"room_id": 101, "check_in": "2024-12-20", "check_out": "2024-12-25", "user_name": "John Doe"}
        ]
        self.backend.book_room(101, "2024-12-20", "2024-12-25", "John Doe")
        self.mock_db.add_booking.assert_called_with(101, "2024-12-20", "2024-12-25", "John Doe")

        bookings = self.backend.get_all_bookings()
        self.assertEqual(len(bookings), 1)
        self.assertEqual(bookings[0]["room_id"], 101)
        self.assertEqual(bookings[0]["user_name"], "John Doe")

if __name__ == '__main__':
    unittest.main()
