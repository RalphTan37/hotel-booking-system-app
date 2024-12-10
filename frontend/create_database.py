import sqlite3
import random
from datetime import date

# Name of the SQLite database file
db_name = 'hotel_management.db'

# Create a connection to the SQLite database file
connection = sqlite3.connect(db_name)

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# SQL command to create the `users` table
create_users_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    role TEXT NOT NULL,
    status TEXT NOT NULL
);
"""

# SQL command to create the `rooms` table
create_rooms_table_query = """
CREATE TABLE IF NOT EXISTS rooms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_number TEXT NOT NULL UNIQUE,
    type TEXT NOT NULL,
    price REAL NOT NULL,
    status TEXT NOT NULL
);
"""

# SQL command to create the `bookings` table
create_bookings_table_query = """
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_id INTEGER NOT NULL,
    check_in DATE NOT NULL,
    check_out DATE NOT NULL,
    user_name TEXT NOT NULL,
    FOREIGN KEY (room_id) REFERENCES rooms (id)
);
"""

# Execute the SQL commands to create the tables
cursor.execute(create_users_table_query)
cursor.execute(create_rooms_table_query)
cursor.execute(create_bookings_table_query)

# Insert sample data for the `users` table
sample_users = [
    ("Ralph", "ralph@slu.edu", "Guest", "Active"),
    ("Joli", "joli@slu.edu", "Guest", "Active"),
    ("Risha", "risha@slu.edu", "Guest", "Active"),
    ("Omair", "omair@slu.edu", "Staff", "Active"),
    ("Shayna", "shayna@slu.edu", "Admin", "Active")
]

cursor.executemany("""
INSERT OR IGNORE INTO users (name, email, role, status) 
VALUES (?, ?, ?, ?);
""", sample_users)

# Insert sample data for the `rooms` table (100 rooms with random types)
room_types = ['Standard', 'Deluxe', 'Suite', 'Executive Suite']
sample_rooms_data = [
    (f'{floor}{room:02}', random.choice(room_types), random.randint(80, 350), 'Available')
    for floor in range(1, 6)  # 5 floors
    for room in range(1, 21)  # 20 rooms per floor
]

# Insert sample data for the rooms
cursor.executemany("""
INSERT OR IGNORE INTO rooms (room_number, type, price, status) 
VALUES (?, ?, ?, ?);
""", sample_rooms_data)

# Fetch room IDs and details
cursor.execute("SELECT id, room_number FROM rooms;")
room_data = cursor.fetchall()
room_ids = [row[0] for row in room_data]

# Map each user to a random room for their booking
users_and_bookings = [
    {"user_name": "Ralph", "room_id": random.choice(room_ids)},
    {"user_name": "Joli", "room_id": random.choice(room_ids)},
    {"user_name": "Risha", "room_id": random.choice(room_ids)},
    {"user_name": "Omair", "room_id": random.choice(room_ids)},
    {"user_name": "Shayna", "room_id": random.choice(room_ids)},
]

# Ensure users are assigned unique rooms
assigned_rooms = set()
for booking in users_and_bookings:
    while booking['room_id'] in assigned_rooms:
        booking['room_id'] = random.choice(room_ids)
    assigned_rooms.add(booking['room_id'])

# Insert bookings for December 10, 2024
bookings = [
    (booking['room_id'], '2024-12-10', '2024-12-11', booking['user_name'])
    for booking in users_and_bookings
]

cursor.executemany("""
INSERT INTO bookings (room_id, check_in, check_out, user_name) 
VALUES (?, ?, ?, ?);
""", bookings)

# Update room status for booked rooms to 'Occupied'
for booking in users_and_bookings:
    query = "UPDATE rooms SET status = 'Occupied' WHERE id = ?;"
    cursor.execute(query, (booking['room_id'],))

# Commit the changes and close the connection
connection.commit()
connection.close()

print(f"Database '{db_name}' created successfully with initial users, rooms, and bookings.")
