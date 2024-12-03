cmake_minimum_required(VERSION 3.15)
project(hotel_booking_system)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Option 1: Use FetchContent to get pybind11
include(FetchContent)
FetchContent_Declare(
    pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11
    GIT_TAG        v2.11.1  # Specify a version tag
)
FetchContent_MakeAvailable(pybind11)

# Find required packages
find_package(MySQL REQUIRED)

# Include directories
include_directories(${MySQL_INCLUDE_DIRS})
include_directories(${CMAKE_SOURCE_DIR}/backend)

# Add backend library
add_library(backend STATIC
    backend/hotel_booking.cpp
    backend/room_search.cpp
    backend/user_account.cpp
)

# Link MySQL to backend
target_link_libraries(backend PRIVATE ${MySQL_LIBRARIES})

# Create Python module
pybind11_add_module(hotel_backend 
    bindings/hotel_bindings.cpp
)

# Link backend to Python module
target_link_libraries(hotel_backend PRIVATE backend)

# Set output directory for the Python module
set_target_properties(hotel_backend PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/frontend
)
