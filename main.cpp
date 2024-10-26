#include <iostream>
#include <vector>
#include <map>
#include "useraccount.h"
#include "room.h"
#include "booking.h"

using namespace std;

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

// Booking a room
void bookRoom(UserAccount& user, vector<Room>& rooms) {
    string paymentInfo, checkInDate, checkOutDate;
    int roomNumber;

    cout << "Enter payment information (card number): ";
    getline(cin, paymentInfo);
    cout << "Enter check-in date (YYYY-MM-DD): ";
    getline(cin, checkInDate);
    cout << "Enter check-out date (YYYY-MM-DD): ";
    getline(cin, checkOutDate);

    for (const auto& room : rooms) {
        if (room.isAvailable) {
            cout << "Room " << room.roomNumber << " (" << room.type << ") - $" << room.price << " per night\n";
        }
    }

    cout << "Enter room number to book: ";
    cin >> roomNumber; cin.ignore();

    for (auto& room : rooms) {
        if (room.roomNumber == roomNumber && room.isAvailable) {
            room.isAvailable = false;
            Booking booking(user.getUsername(), user.getUsername(), paymentInfo, checkInDate, checkOutDate, room);
            user.addBooking(booking);
            return;
        }
    }

    cout << "Invalid room number or room is already booked.\n";
}

int main() {
    vector<Room> rooms = {
        Room(101, "Single", 100.0),
        Room(102, "Double", 150.0),
        Room(103, "Suite", 250.0)
    };

    int choice;
    UserAccount* currentUser = nullptr;

    while (true) {
        cout << "\nHotel Booking System\n";
        cout << "1. Create an account\n";
        cout << "2. Login\n";
        cout << "3. View available rooms\n";
        cout << "4. Book a room\n";
        cout << "5. View my bookings\n";
        cout << "6. Update my bookings\n";
        cout << "7. Cancel my bookings\n";
        cout << "8. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice; cin.ignore();

        switch (choice) {
            case 1:
                createAccount();
                break;
            case 2:
                currentUser = login();
                break;
            case 3:
                if (currentUser) {
                    for (const auto& room : rooms) {
                        if (room.isAvailable) {
                            cout << "Room " << room.roomNumber << " (" << room.type << ") - $" << room.price << " per night\n";
                        }
                    }
                } else {
                    cout << "Please login first.\n";
                }
                break;
            case 4:
                if (currentUser) {
                    bookRoom(*currentUser, rooms);
                } else {
                    cout << "Please login first.\n";
                }
                break;
            case 5:
                if (currentUser) {
                    currentUser->viewBookings();
                } else {
                    cout << "Please login first.\n";
                }
                break;      
        }
}
