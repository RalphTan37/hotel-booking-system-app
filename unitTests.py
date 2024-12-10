#Test User Login - Verify that valid credentials allow login and invalid credentials are rejected.

def test_user_login():
   from login_dialog import validate_login
   assert validate_login("valid_user", "correct_password") is True
   assert validate_login("invalid_user", "wrong_password") is False

#Test Room Availability - Ensure that querying an available room returns the correct status.

def test_room_availability():
   from database import check_room_availability
   assert check_room_availability(10) is True  # Room is available
   assert check_room_availability(102) is False  # Room is booked

#Test Booking Creation - Check if a booking is created correctly with valid data.

def test_create_booking():
   from booking import create_booking
   booking_data = {
       "customer_id": 1,
       "room_id": 101,
       "check_in": "2024-12-20",
       "check_out": "2024-12-25"
   }
   assert create_booking(booking_data) is True

#Test Payment Processing - Validate that payments are processed correctly with valid details.

def test_payment_processing():
   from payment import process_payment
   payment_details = {
       "amount": 500.0,
       "method": "Credit Card",
       "transaction_id": "123456"
   }
   assert process_payment(payment_details) is True

#Test Admin Room Management - Confirm that admins can update room information.

def test_admin_update_room():
   from admin_panel import update_room
   updated_data = {
       "room_id": 101,
       "status": "Under Maintenance",
       "price": 150.0
   }
   assert update_room(updated_data) is True
