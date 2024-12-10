import sqlite3

class Database:
    def __init__(self, db_name="hotel_management.db"):
        """Initialize the connection to the SQLite database."""
        self.connection = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Create all necessary tables in the database."""
        self.create_users_table()
        self.create_rooms_table()
        self.create_bookings_table()

    def create_users_table(self):
        """Create the users table to store user information."""
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            role TEXT NOT NULL,
            status TEXT NOT NULL
        );
        """
        self.connection.execute(query)

    def create_rooms_table(self):
        """Create the rooms table to store room information."""
        query = """
        CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_number TEXT NOT NULL UNIQUE,
            type TEXT NOT NULL,
            price REAL NOT NULL,
            status TEXT NOT NULL
        );
        """
        self.connection.execute(query)

    def create_bookings_table(self):
        """Create the bookings table to store all room bookings."""
        query = """
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_id INTEGER NOT NULL,
            check_in DATE NOT NULL,
            check_out DATE NOT NULL,
            user_name TEXT NOT NULL,
            FOREIGN KEY (room_id) REFERENCES rooms (id)
        );
        """
        self.connection.execute(query)

    def add_user(self, name, email, role, status="Active"):
        """Add a new user to the users table."""
        try:
            query = "INSERT INTO users (name, email, role, status) VALUES (?, ?, ?, ?);"
            self.connection.execute(query, (name, email, role, status))
            self.connection.commit()
        except sqlite3.IntegrityError as e:
            print(f"Error adding user: {e}")

    def get_all_users(self):
        """Retrieve all users from the users table."""
        query = "SELECT * FROM users;"
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def add_room(self, room_number, room_type, price, status="Available"):
        """Add a new room to the rooms table."""
        try:
            query = "INSERT INTO rooms (room_number, type, price, status) VALUES (?, ?, ?, ?);"
            self.connection.execute(query, (room_number, room_type, price, status))
            self.connection.commit()
        except sqlite3.IntegrityError as e:
            print(f"Error adding room: {e}")

    def get_all_rooms(self):
        """Retrieve all rooms from the rooms table."""
        query = "SELECT * FROM rooms;"
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def get_available_rooms(self, date):
        """Get all available rooms that are not booked on the given date."""
        query = """
        SELECT rooms.id, rooms.room_number, rooms.type, rooms.price 
        FROM rooms 
        WHERE rooms.id NOT IN (
            SELECT room_id FROM bookings 
            WHERE ? BETWEEN check_in AND check_out
        );
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (date,))
        return cursor.fetchall()

    def add_booking(self, room_id, check_in, check_out, user_name):
        """Add a new booking for a room."""
        query = "INSERT INTO bookings (room_id, check_in, check_out, user_name) VALUES (?, ?, ?, ?);"
        self.connection.execute(query, (room_id, check_in, check_out, user_name))
        self.connection.commit()

    def get_all_bookings(self):
        """Retrieve all bookings with details about the room and the user."""
        query = """
        SELECT bookings.id, rooms.room_number, rooms.type, bookings.check_in, bookings.check_out, bookings.user_name 
        FROM bookings 
        JOIN rooms ON bookings.room_id = rooms.id;
        """
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def delete_user(self, user_id):
        """Delete a user from the users table by their ID."""
        query = "DELETE FROM users WHERE id = ?;"
        self.connection.execute(query, (user_id,))
        self.connection.commit()

    def delete_room(self, room_id):
        """Delete a room from the rooms table by its ID."""
        query = "DELETE FROM rooms WHERE id = ?;"
        self.connection.execute(query, (room_id,))
        self.connection.commit()

    def delete_booking(self, booking_id):
        """Delete a booking from the bookings table by its ID."""
        query = "DELETE FROM bookings WHERE id = ?;"
        self.connection.execute(query, (booking_id,))
        self.connection.commit()

    def update_user_status(self, user_id, new_status):
        """Update the status of a user (Active, Inactive)."""
        query = "UPDATE users SET status = ? WHERE id = ?;"
        self.connection.execute(query, (new_status, user_id))
        self.connection.commit()

    def update_room_status(self, room_id, new_status):
        """Update the status of a room (Available, Occupied, Maintenance)."""
        query = "UPDATE rooms SET status = ? WHERE id = ?;"
        self.connection.execute(query, (new_status, room_id))
        self.connection.commit()

    def update_booking_dates(self, booking_id, new_check_in, new_check_out):
        """Update the check-in and check-out dates of a booking."""
        query = "UPDATE bookings SET check_in = ?, check_out = ? WHERE id = ?;"
        self.connection.execute(query, (new_check_in, new_check_out, booking_id))
        self.connection.commit()

    def close(self):
        """Close the connection to the database."""
        self.connection.close()

    def get_user_by_id(self, user_id):
        """Retrieve user details by user_id."""
        query = "SELECT * FROM users WHERE id = ?;"
        cursor = self.connection.cursor()
        cursor.execute(query, (user_id,))
        return cursor.fetchone()

    def get_booking_by_user(self, user_name):
        """Retrieve all bookings made by a user."""
        query = """
        SELECT bookings.id, rooms.room_number, rooms.type, bookings.check_in, bookings.check_out 
        FROM bookings 
        JOIN rooms ON bookings.room_id = rooms.id 
        WHERE bookings.user_name = ?;
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (user_name,))
        return cursor.fetchall()  # Return all bookings

    def check_existing_booking(self, user_name, date):
        """Check if a user already has a booking for the given date."""
        query = """
        SELECT * FROM bookings 
        WHERE user_name = ? AND ? BETWEEN check_in AND check_out;
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (user_name, date))
        return cursor.fetchone()  # Return None if no existing booking

