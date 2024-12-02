#include <iostream>
#include <string>
#include <mysql.h>

using namespace std;

// Connection with Hotel DB
MYSQL* connectDatabase() {
    MYSQL* conn = mysql_init(0);
    if (!conn) {
        cerr << "MySQL Initialization Failed" << endl;
        return nullptr;
    }

    conn = mysql_real_connect(conn, "localhost", "username", "password", "Hotel", 3306, NULL, 0);
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
