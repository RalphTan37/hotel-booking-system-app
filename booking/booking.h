#ifndef BOOKING_H
#define BOOKING_H

#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Room details
struct Room {
    int roomNumber;
    string type;
    double price;
    bool isAvailable;
    Room(int num, string t, double p) : roomNumber(num), type(t), price(p), isAvailable(true) {}
};

// Booking details
struct Booking {
    string name;
    string email;
    string paymentInfo;
    string checkInDate;
    string checkOutDate;
    Room room;
    Booking(string n, string e, string p, string checkIn, string checkOut, Room r)
        : name(n), email(e), paymentInfo(p), checkInDate(checkIn), checkOutDate(checkOut), room(r) {}
};

// Function declarations
void displayAvailableRooms(const vector<Room>& rooms);
void bookRoom(vector<Room>& rooms, vector<Booking>& bookings);

#endif // BOOKING_H
