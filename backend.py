import sqlite3
from database import Database

class Backend:
    def __init__(self):
        self.db = Database()

    def get_users(self):
        return self.db.get_all_users()

    def add_user(self, name, email, role, status="Active"):
        self.db.add_user(name, email, role, status)

    def delete_user(self, user_id):
        self.db.delete_user(user_id)

    def get_available_rooms(self, date):
        """Return available rooms for a specific date."""
        return self.db.get_available_rooms(date)

    def book_room(self, room_id, check_in, check_out, user_name):
        """Book a room by adding an entry to the bookings table."""
        self.db.add_booking(room_id, check_in, check_out, user_name)

    def get_all_users(self):
        """Return all users from the database."""
        return self.db.get_all_users()

    def get_all_bookings(self):
        """Return all bookings from the database."""
        return self.db.get_all_bookings()

    def get_user_by_id(self, user_id):
        """Retrieve user details by user_id."""
        return self.db.get_user_by_id(user_id)

    def get_booking_by_user(self, user):
        return self.db.get_booking_by_user(user)
    
    def delete_booking(self, booking_id):
        """Delete a booking by booking_id."""
        self.db.delete_booking(booking_id)

