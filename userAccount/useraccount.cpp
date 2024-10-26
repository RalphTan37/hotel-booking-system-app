#include "useraccount.h"
#include <iostream>
#include <map>

using namespace std;

UserAccount::UserAccount(string u, string e, string p) : username(u), email(e), password(p) {}

string UserAccount::getUsername() {
    return username;
}

bool UserAccount::authenticate(string u, string p) {
    return (u == username && p == password);
}

void UserAccount::viewBookings() {
    if (bookings.empty()) {
        cout << "No current bookings.\n";
        return;
    }

    cout << "Current Bookings:\n";
    for (const auto& booking : bookings) {
        cout << "Room " << booking.room.roomNumber << " (" << booking.room.type << ") - " << booking.checkInDate
             << " to " << booking.checkOutDate << "\n";
    }
}

void UserAccount::updateBooking(vector<Room>& rooms) {
    if (bookings.empty()) {
        cout << "No current bookings to update.\n";
        return;
    }

    viewBookings();
    int bookingIndex;
    cout << "Enter the index of the booking to update: ";
    cin >> bookingIndex; cin.ignore();

    if (bookingIndex < 0 || bookingIndex >= bookings.size()) {
        cout << "Invalid booking index.\n";
        return;
    }

    Booking& booking = bookings[bookingIndex];
    cout << "Updating booking for Room " << booking.room.roomNumber << ". Enter new check-in date: ";
    getline(cin, booking.checkInDate);
    cout << "Enter new check-out date: ";
    getline(cin, booking.checkOutDate);

    cout << "Booking updated successfully.\n";
}

void UserAccount::cancelBooking() {
    if (bookings.empty()) {
        cout << "No current bookings to cancel.\n";
        return;
    }

    viewBookings();
    int bookingIndex;
    cout << "Enter the index of the booking to cancel: ";
    cin >> bookingIndex; cin.ignore();

    if (bookingIndex < 0 || bookingIndex >= bookings.size()) {
        cout << "Invalid booking index.\n";
        return;
    }

    bookings.erase(bookings.begin() + bookingIndex);
    cout << "Booking cancelled successfully.\n";
}

void UserAccount::addBooking(Booking booking) {
    bookings.push_back(booking);
    cout << "Booking added successfully.\n";
}

map<string, UserAccount> userAccounts;

// Create a new user account
void createAccount() {
    string username, email, password;

    cout << "Enter username: ";
    getline(cin, username);
    cout << "Enter email: ";
    getline(cin, email);
    cout << "Enter password: ";
    getline(cin, password);

    if (userAccounts.find(username) != userAccounts.end()) {
        cout << "Username already exists. Please choose a different one.\n";
        return;
    }

    UserAccount newUser(username, email, password);
    userAccounts[username] = newUser;
    cout << "Account created successfully.\n";
}

// User login function
UserAccount* login() {
    string username, password;

    cout << "Enter username: ";
    getline(cin, username);
    cout << "Enter password: ";
    getline(cin, password);

    if (userAccounts.find(username) != userAccounts.end() &&
        userAccounts[username].authenticate(username, password)) {
        cout << "Login successful.\n";
        return &userAccounts[username];
    } else {
        cout << "Invalid username or password.\n";
        return nullptr;
    }
}