# Find required packages for bindings
find_package(pybind11 REQUIRED)

# Set include directories for bindings
include_directories(${CMAKE_SOURCE_DIR}/backend)
