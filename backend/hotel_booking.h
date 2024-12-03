#pragma once
#include <string>
#include <vector>
#include <mysql.h>

struct Booking {
    int bookingId;
    int roomNumber;
    std::string customerName;
    std::string bookingDate;
    std::string status;
};

class HotelBooking {
public:
    static MYSQL* connectDatabase();
    static bool bookRoom(MYSQL* conn, int roomNumber, const std::string& customerName, 
                        const std::string& bookingDate);
    static bool isRoomAvailable(MYSQL* conn, int roomNumber);
    static std::vector<Booking> getBookings(MYSQL* conn);
    static bool cancelBooking(MYSQL* conn, int bookingId);
};
