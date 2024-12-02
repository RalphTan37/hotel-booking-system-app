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

// Adding a new payment option
void addPaymentOption(MYSQL* conn, int userID, const string& cardHolderName, const string& cardNumber, const string& expirationDate, const string& cvv, const string& paymentType, const string& paymentDetails){
    string query = "INSERT INTO PaymentOptions (UserID, CardHolderName, CardNumber, ExpirationDate, CVV, PaymentType, PaymentDetails) VALUES ('" + to_string(userID) + "', '" + cardHolderName + "', '" + cardNumber + "', '" + expirationDate +"', '" + cvv + "', '" + paymentType + "', '" + paymentDetails + "')";
    if (mysql_query(conn, query.c_str())){
        cerr << "Insert Error: " << mysql_error(conn) << endl;
    } else {
        cout << "Payment Option Added Successfully!" << endl;
    }
}

