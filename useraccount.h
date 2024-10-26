#ifndef USERACCOUNT_H
#define USERACCOUNT_H

#include <string>
#include <vector>
#include "room.h"
#include "booking.h"

class UserAccount {
private:
    std::string username;
    std::string email;
    std::string password;
    std::vector<Booking> bookings;

public:
    UserAccount(std::string u, std::string e, std::string p);

    std::string getUsername();
    bool authenticate(std::string u, std::string p);

    void viewBookings();
    void updateBooking(std::vector<Room>& rooms);
    void cancelBooking();

    void addBooking(Booking booking);
};

#endif
