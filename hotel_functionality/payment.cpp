#include <iostream>
#include <string>
#include <mysql.h>

using namespace std;

// Connect to the database
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

    cerr << "Database Connected Failed: " << mysql_error(conn) << endl;
    return nullptr;
}
