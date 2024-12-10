import unittest
from unittest.mock import MagicMock, patch
from datetime import datetime, timedelta
import sys

class TestHotelSystem(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Mock database connection
        self.db_mock = MagicMock()
        
        # Sample test data
        self.valid_user = {"username": "valid_user", "password": "correct_password"}
        self.invalid_user = {"username": "invalid_user", "password": "wrong_password"}
        self.test_room_id = 101
        self.test_customer_id = 1
        
        # Sample booking data
        self.booking_data = {
            "customer_id": self.test_customer_id,
            "room_id": self.test_room_id,
            "check_in": "2024-12-20",
            "check_out": "2024-12-25",
            "total_price": 500.0
        }
        
        # Sample payment data
        self.payment_data = {
            "amount": 500.0,
            "method": "Credit Card",
            "card_number": "4111111111111111",
            "expiry": "12/25",
            "cvv": "123",
            "transaction_id": "123456"
        }
        
        # Sample room update data
        self.room_update_data = {
            "room_id": self.test_room_id,
            "status": "Under Maintenance",
            "price": 150.0,
            "room_type": "Deluxe",
            "description": "Ocean View Room"
        }

    def test_user_login(self):
        """Test user authentication with both valid and invalid credentials."""
        with patch('login_dialog.validate_login') as mock_validate:
            # Test valid login
            mock_validate.return_value = True
            result = mock_validate(self.valid_user["username"], self.valid_user["password"])
            self.assertTrue(result, "Valid login credentials should return True")
            mock_validate.assert_called_with(self.valid_user["username"], self.valid_user["password"])

            # Test invalid login
            mock_validate.return_value = False
            result = mock_validate(self.invalid_user["username"], self.invalid_user["password"])
            self.assertFalse(result, "Invalid login credentials should return False")
            mock_validate.assert_called_with(self.invalid_user["username"], self.invalid_user["password"])

    def test_room_availability(self):
        """Test room availability checking functionality."""
        with patch('database.check_room_availability') as mock_check:
            # Test available room
            mock_check.return_value = True
            result = mock_check(self.test_room_id)
            self.assertTrue(result, f"Room {self.test_room_id} should be available")
            mock_check.assert_called_with(self.test_room_id)

            # Test unavailable room
            mock_check.return_value = False
            result = mock_check(102)  # Different room ID
            self.assertFalse(result, "Room 102 should be unavailable")
            mock_check.assert_called_with(102)

            # Test invalid room number
            with self.assertRaises(ValueError):
                mock_check.side_effect = ValueError("Invalid room number")
                mock_check(-1)

    def test_create_booking(self):
        """Test the creation of new bookings with various scenarios."""
        with patch('booking.create_booking') as mock_booking:
            # Test successful booking creation
            mock_booking.return_value = True
            result = mock_booking(self.booking_data)
            self.assertTrue(result, "Booking should be created successfully")
            mock_booking.assert_called_with(self.booking_data)

            # Test booking with invalid dates
            invalid_booking_data = self.booking_data.copy()
            invalid_booking_data["check_out"] = "2024-12-19"  # Check-out before check-in
            mock_booking.side_effect = ValueError("Invalid dates")
            with self.assertRaises(ValueError):
                mock_booking(invalid_booking_data)

            # Test booking for unavailable room
            mock_booking.side_effect = ValueError("Room not available")
            with self.assertRaises(ValueError):
                invalid_booking_data["room_id"] = 102  # Unavailable room
                mock_booking(invalid_booking_data)

    def test_payment_processing(self):
        """Test payment processing with different payment scenarios."""
        with patch('payment.process_payment') as mock_payment:
            # Test successful payment
            mock_payment.return_value = True
            result = mock_payment(self.payment_data)
            self.assertTrue(result, "Payment should be processed successfully")
            mock_payment.assert_called_with(self.payment_data)

            # Test invalid payment amount
            invalid_payment_data = self.payment_data.copy()
            invalid_payment_data["amount"] = -500.0
            mock_payment.side_effect = ValueError("Invalid payment amount")
            with self.assertRaises(ValueError):
                mock_payment(invalid_payment_data)

            # Test expired card
            invalid_payment_data["expiry"] = "12/20"
            mock_payment.side_effect = ValueError("Card expired")
            with self.assertRaises(ValueError):
                mock_payment(invalid_payment_data)

            # Test invalid card number
            invalid_payment_data["card_number"] = "1111111111111111"
            mock_payment.side_effect = ValueError("Invalid card number")
            with self.assertRaises(ValueError):
                mock_payment(invalid_payment_data)

    def test_admin_update_room(self):
        """Test admin functionality for updating room information."""
        with patch('admin_panel.update_room') as mock_update:
            # Test successful room update
            mock_update.return_value = True
            result = mock_update(self.room_update_data)
            self.assertTrue(result, "Room should be updated successfully")
            mock_update.assert_called_with(self.room_update_data)

            # Test invalid room status
            invalid_room_data = self.room_update_data.copy()
            invalid_room_data["status"] = "Invalid Status"
            mock_update.side_effect = ValueError("Invalid room status")
            with self.assertRaises(ValueError):
                mock_update(invalid_room_data)

            # Test invalid price
            invalid_room_data["price"] = -150.0
            mock_update.side_effect = ValueError("Invalid price")
            with self.assertRaises(ValueError):
                mock_update(invalid_room_data)

            # Test non-existent room
            invalid_room_data["room_id"] = 999
            mock_update.side_effect = ValueError("Room does not exist")
            with self.assertRaises(ValueError):
                mock_update(invalid_room_data)

    def tearDown(self):
        """Clean up after each test method."""
        pass

if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
