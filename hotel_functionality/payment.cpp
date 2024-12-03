#include "database.h"
#include <iostream>
#include <string>
#include <mysql.h>

using namespace std;

// Adding a new payment option
void addPaymentOption(MYSQL* conn, int userID, const string& cardHolderName, const string& cardNumber, const string& expirationDate, const string& cvv, const string& paymentType, const string& paymentDetails){
    string query = "INSERT INTO PaymentOptions (UserID, CardHolderName, CardNumber, ExpirationDate, CVV, PaymentType, PaymentDetails) VALUES ('" + to_string(userID) + "', '" + cardHolderName + "', '" + cardNumber + "', '" + expirationDate +"', '" + cvv + "', '" + paymentType + "', '" + paymentDetails + "')";
    if (mysql_query(conn, query.c_str())){
        cerr << "Insert Error: " << mysql_error(conn) << endl;
    } else {
        cout << "Payment Option Added Successfully!" << endl;
    }
}

// Obtaining payment option
void getPaymentOptions(MYSQL* conn, int userID) {
    string query = "SELECT * FROM PaymentOptions WHERE UserID = " + to_string(userID);
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
    cout << "Payment Options for User ID: " << userID << endl;
    while ((row = mysql_fetch_row(result))) {
        cout << "PaymentID: " << row[0] << ", CardHolderName: " << row[2] << ", PaymentType: " << row[6] << endl;
    }
    mysql_free_result(result);
}

// Updating payment option
void updatePaymentOption(MYSQL* conn, int paymentID, const string& cardHolderName, const string& cardNumber, const string& expirationDate, const string& cvv) {
    string query = "UPDATE PaymentOptions SET CardHolderName = '" + cardHolderName + "', CardNumber = '" + cardNumber + "', ExpirationDate = '" + expirationDate + "', CVV = '" + cvv + "' WHERE PaymentID = " + to_string(paymentID);
    if (mysql_query(conn, query.c_str())) {
        cerr << "Update Error: " << mysql_error(conn) << endl;
    } else {
        cout << "Payment Option Update Successfully!" << endl;
    }
}