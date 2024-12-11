# Hotel Booking System - Urban Oasis Hotel

A comprehensive hotel booking system built with C++ backend and Python/Qt frontend. This application provides a robust solution for managing hotel bookings, room availability, and user accounts.

## System Requirements

- Python 3.8 or higher
- C++ compiler (g++ 5.0 or higher)
- MySQL Server 8.0 or higher
- CMake 3.15 or higher

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hotel-booking-system.git
cd hotel-booking-system
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Configure MySQL:
- Ensure MySQL server is running
- Create a database using the SQL script:
```bash
mysql -u root -p < backend/HotelDatabase.sql
```

4. Build C++ bindings:
```bash
mkdir build && cd build
cmake ..
make
cd ..
```

5. Install the Python package:
```bash
python setup.py install
```

## Running the Application

1. Start the application:
```bash
python frontend/main_window.py
```

## Project Structure

```
hotel_booking_system/
├── backend/          # C++ backend implementation
├── frontend/         # Python/Qt GUI implementation
├── bindings/         # C++/Python integration
├── tests/           # Test suite
└── docs/            # Documentation
```

## Features

- **User Management**
  - Secure login system
  - User profile management
  - Role-based access control

- **Booking Management**
  - Room availability checking
  - Booking creation and modification
  - Payment processing

- **Admin Features**
  - Room management
  - Booking overview
  - System configuration

## Development

### Testing
Run the test suite:
```bash
pytest tests/
```

### Code Style
Format Python code:
```bash
black frontend/
```

Run linter:
```bash
flake8 frontend/
```

## Architecture

The application follows a layered architecture:

1. **Frontend Layer (Python/Qt)**
   - Handles user interface and interactions
   - Communicates with backend through bindings

2. **Backend Layer (C++)**
   - Implements core business logic
   - Manages database operations
   - Handles data processing

3. **Database Layer (MySQL)**
   - Stores application data
   - Manages data relationships
   - Ensures data integrity

![Architecture Diagram](docs/images/architecture.png)

## Database Schema

The system uses MySQL with the following main tables:
- LoginCredentials: User authentication and profiles
- Rooms: Room information and availability
- Bookings: Reservation details
- PaymentOptions: Payment methods and transactions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request


# Hotel Booking System Application

Developing a Hotel Booking System Application in C++. Urban Oasis Hotel!

## Running the Program:

Compile the Program:
```
g++ -o main main.cpp
```

Run the Executeable:
```
./main.exe
```

## Connecting to the MySQL Database:

- Ensure that your have MySQL installed.
- Ensure your the have MySQL C++ Connector installed.
- In ```c_cpp_properties.json```, include paths to the MySQL Server and MySQL Connecter C++.


## System Requirements:
Compatible with Windows, macOS, and Linux.
g++ (GNU C++ Compiler) version 5.0 or higher

## Library Requirements:
- Open Source Libraries: Qt

## High-Level Design Overview:
This section provides a high-level design of the Hotel Booking System Application, including key components and architecture.

### Main Components:
1. User Interface (GUI):
   - Handles user interactions for booking, checking availability, and managing reservations.
2. Database:
   - Stores login credentials, hotel rooms
3. Core Classes :
   - Booking: Manages booking details, including check-in and check-out dates, customer information, and room selection.
   - Room: Represents room details, such as type, availability, and pricing.
   - UserAccount: Handles user authentication and profiles.
  
### Architecture Overview:
The application follows a modular architecture, separating concerns between the user interface, business logic, and data management. This design ensures maintainability and scalability as new features can be added with minimal impact on existing code.

   ![Screenshot 2024-10-08 153142](https://github.com/user-attachments/assets/fd4d9177-b32f-4dd6-a6f1-6234c9c97e3d)

![Screenshot 2024-10-08 154019](https://github.com/user-attachments/assets/6e628204-d9b6-4c39-b50c-2b87abc4b761)

![Screenshot 2024-10-08 154859](https://github.com/user-attachments/assets/a7d6a149-ce5a-4eee-ab6f-b25849e1940f)
