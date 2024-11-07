#include <iostream>
#include <string>
#include <mysql.h>

using namespace std;

MYSQL* connectDatabase() {
    MYSQL* conn = mysql_init(0);
    if (conn) {
        //Will need to replace username and password with actual values
        conn = mysql_real_connect(conn, "localhost:3306", "username", "password", "Hotel", 0, NULL, 0);
        if (conn) {
            cout << "Connected to the Hotel Database!" << endl;
            return conn;
        }
        cout << "Hotel Database Connection Failed: " << mysql_error(conn) << endl;
        return nullptr;
    }
}
