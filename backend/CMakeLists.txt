# Set source files
set(SOURCES
    hotel_booking.cpp
    room_search.cpp
    user_account.cpp
)

# Set header files
set(HEADERS
    hotel_booking.h
    room_search.h
    user_account.h
)

# Create library
add_library(backend STATIC ${SOURCES} ${HEADERS})

# Find and link MySQL
find_package(MySQL REQUIRED)
target_link_libraries(backend PRIVATE ${MySQL_LIBRARIES})
