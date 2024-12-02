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

// Searching for Rooms
void searchRoomes(MYSQL* conn, const string& roomType, double minPrice, double maxPrice, const string& availabilityDate) {
    string query = "SELECT * FROM Rooms WHERE Type = '" + roomType + "' AND Price BETWEEN " + to_string(minPrice) + " AND " + to_string(maxPrice) + " AND AvailabilityDate <= '" + availabilityDate + "'";

    if (mysql_query(conn, query.c_str())) {
        cerr << "Query Error: " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    if (!result) {
        cerr << "Store Result Error: " << mysql_error(conn) << endl;
        return;
    }

    MYSQL_ROW row;
    cout << "Available Rooms:" << endl;
    cout << "RoomID | RoomNumber | Type | Price | AvailabilityDate" << endl;
    while ((row = mysql_fetch_row(result))) {
        cout << row[0] << " | " << row[1] << " | " << row[2] << " | $" << row[3] << " | " << row[4] << endl;
    }
    mysql_free_result(result);
}