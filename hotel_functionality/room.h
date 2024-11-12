// Room.h
#ifndef ROOM_H
#define ROOM_H

#include <string>

struct Room {
    int roomNumber;
    std::string type;
    double price;
    bool isAvailable;

    Room(int num, std::string t, double p);
};

#endif
