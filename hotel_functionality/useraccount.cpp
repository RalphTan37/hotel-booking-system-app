#include "database.h"
#include <iostream>
#include <string>
#include <mysql.h>

using namespace std;

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

// Allow Users to update their password
void updatePassword(MYSQL* conn, const string& username){
    string newPassword;
    cout << "Enter New Password: ";
    cin >> newPassword;
    string query = "UPDATE LoginCredentials SET Password = '" + newPassword + "' WHERE Username = '" + username + "'";
    if (mysql_query(conn, query.c_str())){
        cerr << "Update Error: " << mysql_error(conn) << endl;
    } else {
        cout << "Password Updated Successfully!" << endl;
    }
}
