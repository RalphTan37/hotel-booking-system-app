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

    // Replace these with your database credentials
    conn = mysql_real_connect(conn, "localhost", "username", "password", "Hotel", 3306, NULL, 0);
    if (conn) {
        cout << "Connected to the Hotel Database!" << endl;
        return conn;
    }

    cerr << "Database Connection Failed: " << mysql_error(conn) << endl;
    return nullptr;
}
