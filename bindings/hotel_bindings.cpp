#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "../backend/hotel_booking.h"
#include "../backend/room_search.h"
#include "../backend/user_account.h"

namespace py = pybind11;

PYBIND11_MODULE(hotel_backend, m) {
    // Booking struct binding
    py::class_<Booking>(m, "Booking")
        .def_readwrite("booking_id", &Booking::bookingId)
        .def_readwrite("room_number", &Booking::roomNumber)
        .def_readwrite("customer_name", &Booking::customerName)
        .def_readwrite("booking_date", &Booking::bookingDate)
        .def_readwrite("status", &Booking::status);

    // Room struct binding
    py::class_<Room>(m, "Room")
        .def_readwrite("room_id", &Room::roomId)
        .def_readwrite("room_number", &Room::roomNumber)
        .def_readwrite("type", &Room::type)
        .def_readwrite("price", &Room::price)
        .def_readwrite("availability_date", &Room::availabilityDate);

    // User struct binding
    py::class_<User>(m, "User")
        .def_readwrite("id", &User::id)
        .def_readwrite("username", &User::username)
        .def_readwrite("email", &User::email)
        .def_readwrite("first_name", &User::firstName)
        .def_readwrite("last_name", &User::lastName)
        .def_readwrite("is_admin", &User::isAdmin);

    // HotelBooking class bindings
    m.def("connect_database", &HotelBooking::connectDatabase);
    m.def("book_room", &HotelBooking::bookRoom);
    m.def("is_room_available", &HotelBooking::isRoomAvailable);
    m.def("get_bookings", &HotelBooking::getBookings);
    m.def("cancel_booking", &HotelBooking::cancelBooking);

    // RoomSearch class bindings
    m.def("search_rooms", &RoomSearch::searchRooms);
    m.def("update_room_status", &RoomSearch::updateRoomStatus);
    m.def("get_all_rooms", &RoomSearch::getAllRooms);

    // UserAccount class bindings
    m.def("verify_credentials", &UserAccount::verifyCredentials);
    m.def("get_user_details", &UserAccount::getUserDetails);
    m.def("update_password", &UserAccount::updatePassword);
}
