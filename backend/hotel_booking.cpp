#include "hotel_booking.h"
#include <sstream>

MYSQL* HotelBooking::connectDatabase() {
    MYSQL* conn = mysql_init(nullptr);
    if (!conn) {
        return nullptr;
    }

    conn = mysql_real_connect(conn, "localhost", "root", "", "Hotel", 3306, NULL, 0);
    return conn;
}

bool HotelBooking::bookRoom(MYSQL* conn, int roomNumber, const std::string& customerName, 
                           const std::string& bookingDate) {
    std::stringstream query;
    query << "INSERT INTO Bookings (RoomNumber, CustomerName, BookingDate) VALUES ("
          << roomNumber << ", '" << customerName << "', '" << bookingDate << "')";
          
    return (mysql_query(conn, query.str().c_str()) == 0);
}

bool HotelBooking::isRoomAvailable(MYSQL* conn, int roomNumber) {
    std::stringstream query;
    query << "SELECT AvailabilityDate FROM Rooms WHERE RoomNumber = " << roomNumber 
          << " AND RoomNumber NOT IN (SELECT RoomNumber FROM Bookings WHERE BookingDate = CURDATE())";
          
    if (mysql_query(conn, query.str().c_str()) != 0) {
        return false;
    }
    
    MYSQL_RES* result = mysql_store_result(conn);
    bool available = (mysql_num_rows(result) > 0);
    mysql_free_result(result);
    return available;
}

std::vector<Booking> HotelBooking::getBookings(MYSQL* conn) {
    std::vector<Booking> bookings;
    
    if (mysql_query(conn, "SELECT * FROM Bookings ORDER BY BookingDate DESC") != 0) {
        return bookings;
    }
    
    MYSQL_RES* result = mysql_store_result(conn);
    MYSQL_ROW row;
    
    while ((row = mysql_fetch_row(result))) {
        Booking booking;
        booking.bookingId = std::stoi(row[0]);
        booking.roomNumber = std::stoi(row[1]);
        booking.customerName = row[2];
        booking.bookingDate = row[3];
        bookings.push_back(booking);
    }
    
    mysql_free_result(result);
    return bookings;
}

bool HotelBooking::cancelBooking(MYSQL* conn, int bookingId) {
    std::stringstream query;
    query << "DELETE FROM Bookings WHERE BookingID = " << bookingId;
    return (mysql_query(conn, query.str().c_str()) == 0);
}
