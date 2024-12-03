#include <iostream>
#include <string>
#include <mysql.h>

using namespace std;

// Establish connection with Hotel DB
MYSQL* connectDatabase() {
    MYSQL* conn = mysql_init(0);
    if (!conn) {
        cerr << "MySQL Initialization Failed" << endl;
        return nullptr;
    }

    conn = mysql_real_connect(conn, "localhost", "root", "password", "Hotel", 3306, NULL, 0);
    if (conn) {
        cout << "Connected to the Hotel Database!" << endl;
        return conn;
    }

    cerr << "Database Connection Failed: " << mysql_error(conn) << endl;
    return nullptr;
}

// Checking Room Availability
bool isRoomAvailable(MYSQL* conn, int roomNumber) {
    string query = "SELECT AvailabilityDate FROM Rooms WHERE RoomNumber = " + to_string(roomNumber);
    if (mysql_query(conn, query.c_str())) {
        cerr << "Query Error: " << mysql_error(conn) << endl;
        return false;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (!result) {
        cerr << "Store Result Error: " << mysql_error(conn) << endl;
        return false;
    }

    MYSQL_ROW row = mysql_fetch_row(result);
    if (row) {
        string availabilityDate = row[0];
        cout << "Room is available until: " << availabilityDate << endl;
        mysql_free_result(result);
        return true;
    }

    cerr << "Room not found or unavailable." << endl;
    mysql_free_result(result);
    return false;
}

// Booking a Room
bool bookRoom(MYSQL* conn, int roomNumber, const string& customerName, const string& bookingDate) {
    if (!isRoomAvailable(conn, roomNumber)) {
        cout << "Room is not available for booking." << endl;
        return false;
    }

    string query = "INSERT INTO Bookings (RoomNumber, CustomerName, BookingDate) VALUES (" +
                   to_string(roomNumber) + ", '" + customerName + "', '" + bookingDate + "')";
    if (mysql_query(conn, query.c_str())) {
        cerr << "Booking Error: " << mysql_error(conn) << endl;
        return false;
    }

    cout << "Room " << roomNumber << " successfully booked for " << customerName << " on " << bookingDate << endl;

    string updateQuery = "UPDATE Rooms SET AvailabilityDate = '" + bookingDate + "' WHERE RoomNumber = " + to_string(roomNumber);
    if (mysql_query(conn, updateQuery.c_str())) {
        cerr << "Update Error: " << mysql_error(conn) << endl;
        return false;
    }

    return true;
}