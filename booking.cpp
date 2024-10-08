// Booking.cpp
#include "booking.h"

Booking::Booking(std::string user, std::string e, std::string p, std::string checkIn, std::string checkOut, Room r)
    : username(user), email(e), paymentInfo(p), checkInDate(checkIn), checkOutDate(checkOut), room(r) {}
