// Booking.h
#ifndef BOOKING_H
#define BOOKING_H

#include <string>
#include "room.h"

struct Booking {
    std::string username;
    std::string email;
    std::string paymentInfo;
    std::string checkInDate;
    std::string checkOutDate;
    Room room;

    Booking(std::string user, std::string e, std::string p, std::string checkIn, std::string checkOut, Room r);
};

#endif
