#include <iostream>
#include <vector>
#include <string>
using namespace std;

//room details
struct Room{
    int roomNumber;
    string type;
    double price;
    bool isAvailable;
    Room(int num, string t, double p): roomNumber(num), type (t), price(p), isAvailable(true) {}
};

//booking details
struct Booking{
    string name;
    string email;
    string paymentInfo;
    string checkInDate;
    string checkInOut;
    Room room;
    Booking(string n, string e, string p, string checkIn, string CheckOut, Room r): name(n), email(e), paymentInfo(p), checkInDate(checkIn), checkInOut(CheckOut), room(r) {}
};

//available rooms
void displayAvailableRooms(const vector<Room>& rooms) {
    cout <<"Available Rooms:\n";
    for (const auto& room : rooms){
        if (room.isAvailable){
            cout << "Room " << room.roomNumber << " (" << room.type << ") - $" << room.price << " per night\n";
        }
    }
}

//booking a room
void bookRoom(vector<Room>& rooms, vector<Booking>& bookings) {
    string name, email, paymentInfo, checkInDate, checkOutDate;
    int roomNumber;

    //gets users' information
    cout << "Enter your name: ";
    getline(cin, name);
    cout << "Enter your email: ";
    getline(cin, email);
    cout << "Enter payment information (card number): ";
    getline(cin, paymentInfo);
    cout << "Enter check-in date (YYYY-MM-DD): ";
    getline(cin, checkInDate);
    cout << "Enter check-out date (YYYY-MM-DD): ";
    getline(cin, checkOutDate);

    displayAvailableRooms(rooms);

    cout << "Enter room number to book: ";
    cin >> roomNumber; cin.ignore();

    //finds and books room
    for (auto& room : rooms) {
        if (room.roomNumber == roomNumber && room.isAvailable) {
            room.isAvailable = false;
            bookings.push_back(Booking(name, email, paymentInfo, checkInDate, checkOutDate, room));
            cout << "Room " << roomNumber << " has been successfully booked.\n";
            return;
        }
    }

    cout << "Invalid room number or room is already booked.\n";
}

//placeholder for rooms db - creation of file tbd
int main() {
    vector<Room> rooms = {
        Room(101, "Single", 100.0),
        Room(102, "Double", 150.0),
        Room(103, "Suite", 250.0)
    };

    vector<Booking> bookings;

    int choice;

    while (true) {
        cout << "\nHotel Booking System\n";
        cout << "1. View available rooms\n";
        cout << "2. Book a room\n";
        cout << "3. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice; cin.ignore(); 

        switch (choice) {
            case 1:
                displayAvailableRooms(rooms);
                break;
            case 2:
                bookRoom(rooms, bookings);
                break;
            case 3:
                cout << "Exiting the system.\n";
                return 0;
            default:
                cout << "Invalid choice. Please try again.\n";
        }
    }
}