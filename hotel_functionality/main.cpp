#include <iostream>
#include <string>
#include "payment.cpp"        
#include "room_search.cpp"    
#include "useraccount.cpp"    
#include "hotel_booking.cpp"  

using namespace std;

void displayMenu() {
    cout << "\n--- Hotel Management System ---\n";
    cout << "1. User Login\n";
    cout << "2. Search for Rooms\n";
    cout << "3. Manage Payments\n";
    cout << "4. Book a Room\n";
    cout << "5. Exit\n";
    cout << "Enter your choice: ";
}