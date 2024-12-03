#include "room_search.h"
#include <sstream>

std::vector<Room> RoomSearch::searchRooms(MYSQL* conn, const std::string& roomType, 
                                        double minPrice, double maxPrice, 
                                        const std::string& availabilityDate) {
    std::vector<Room> rooms;
    std::stringstream query;
    
    query << "SELECT * FROM Rooms WHERE 1=1";
    if (!roomType.empty() && roomType != "Any Type") {
        query << " AND Type = '" << roomType << "'";
    }
    query << " AND Price BETWEEN " << minPrice << " AND " << maxPrice
          << " AND AvailabilityDate <= '" << availabilityDate << "'";
    
    if (mysql_query(conn, query.str().c_str()) != 0) {
        return rooms;
    }
    
    MYSQL_RES* result = mysql_store_result(conn);
    MYSQL_ROW row;
    
    while ((row = mysql_fetch_row(result))) {
        Room room;
        room.roomId = std::stoi(row[0]);
        room.roomNumber = std::stoi(row[1]);
        room.type = row[2];
        room.price = std::stod(row[3]);
        room.availabilityDate = row[4];
        rooms.push_back(room);
    }
    
    mysql_free_result(result);
    return rooms;
}

bool RoomSearch::updateRoomStatus(MYSQL* conn, int roomId, const std::string& status) {
    std::stringstream query;
    query << "UPDATE Rooms SET AvailabilityDate = CURDATE() WHERE RoomID = " << roomId;
    return (mysql_query(conn, query.str().c_str()) == 0);
}

std::vector<Room> RoomSearch::getAllRooms(MYSQL* conn) {
    std::vector<Room> rooms;
    
    if (mysql_query(conn, "SELECT * FROM Rooms ORDER BY RoomNumber") != 0) {
        return rooms;
    }
    
    MYSQL_RES* result = mysql_store_result(conn);
    MYSQL_ROW row;
    
    while ((row = mysql_fetch_row(result))) {
        Room room;
        room.roomId = std::stoi(row[0]);
        room.roomNumber = std::stoi(row[1]);
        room.type = row[2];
        room.price = std::stod(row[3]);
        room.availabilityDate = row[4];
        rooms.push_back(room);
    }
    
    mysql_free_result(result);
    return rooms;
}
