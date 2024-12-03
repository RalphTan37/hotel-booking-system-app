#pragma once
#include <string>
#include <vector>
#include <mysql.h>

struct Room {
    int roomId;
    int roomNumber;
    std::string type;
    double price;
    std::string availabilityDate;
};

class RoomSearch {
public:
    static std::vector<Room> searchRooms(MYSQL* conn, const std::string& roomType, 
                                       double minPrice, double maxPrice, 
                                       const std::string& availabilityDate);
    static bool updateRoomStatus(MYSQL* conn, int roomId, const std::string& status);
    static std::vector<Room> getAllRooms(MYSQL* conn);
};
