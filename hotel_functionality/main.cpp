#include <iostream>
#include <string>
#include "payment.cpp"        
#include "room_search.cpp"    
#include "useraccount.cpp"    
#include "hotel_booking.cpp"  

using namespace std;

void displayMenu() {
    cout << "\n--- Urban Oasis Hotel ---\n";
    cout << "1. User Login\n";
    cout << "2. Search for Rooms\n";
    cout << "3. Manage Payments\n";
    cout << "4. Book a Room\n";
    cout << "5. Exit\n";
    cout << "Enter your choice: ";
}

// Mangaging Payment Options
void managePayments(MYSQL* conn, int userID) {
    int choice;
    do {
        cout << "\n--- Payment Management ---\n";
        cout << "1. Add Payment Option\n";
        cout << "2. View Payment Options\n";
        cout << "3. Update Payment Option\n";
        cout << "4. Back\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                string cardHolderName, cardNumber, expirationDate, cvv, paymentType, paymentDetails;
                cout << "Enter Card Holder Name: ";
                cin.ignore();
                getline(cin, cardHolderName);
                cout << "Enter Card Number: ";
                cin >> cardNumber;
                cout << "Enter Expiration Date (YYYY-MM-DD): ";
                cin >> expirationDate;
                cout << "Enter CVV: ";
                cin >> cvv;
                cout << "Enter Payment Type (Credit Card/Debit Card/PayPal): ";
                cin >> paymentType;
                cout << "Enter Payment Details (in JSON format): ";
                cin.ignore();
                getline(cin, paymentDetails);
                addPaymentOption(conn, userID, cardHolderName, cardNumber, expirationDate, cvv, paymentType, paymentDetails);
                break;
            }
            case 2:
                getPaymentOptions(conn, userID);
                break;
            case 3: {
                int paymentID;
                string cardHolderName, cardNumber, expirationDate, cvv;
                cout << "Enter Payment ID to Update: ";
                cin >> paymentID;
                cout << "Enter New Card Holder Name: ";
                cin.ignore();
                getline(cin, cardHolderName);
                cout << "Enter New Card Number: ";
                cin >> cardNumber;
                cout << "Enter New Expiration Date (YYYY-MM-DD): ";
                cin >> expirationDate;
                cout << "Enter New CVV: ";
                cin >> cvv;
                updatePaymentOption(conn, paymentID, cardHolderName, cardNumber, expirationDate, cvv);
                break;
            }
            case 4:
                cout << "Returning to Main Menu...\n";
                break;
            default:
                cout << "Invalid choice. Please try again.\n";
        }
    } while (choice != 4);
}