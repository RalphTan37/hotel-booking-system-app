#include <iostream>
#include <string>
#include <mysql.h>

using namespace std;

// Establish connection with Hotel Database
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

// Verify Username & Password
bool verifyCredentials(MYSQL* conn, const string& username, const string& password){
    string query = "SELECT COUNT (*) FROM LoginCredentials WHERE Username = '" + username + "' AND Password = '" + password + "'";
    if(mysql_query(conn, query.c_str())){
        cerr << "Query Error: " << mysql_error(conn) << endl;
        return false;
    }

    MYSQL_RES* result = mysql_store_result(conn);
    MYSQL_ROW row = mysql_fetch_row(result);
    bool isAuthenticated = (stoi(row[0]) > 0);
    mysql_free_result(result);
    return isAuthenticated;
}