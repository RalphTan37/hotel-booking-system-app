#include <iostream>
#include <string>

using namespace std;

//constants for room rates
const double singleRoom = 80.00;
const double doubleRoom = 90.00;
const double queenRoom = 100.00;
const double kingRoom = 110.00;
const double suiteRoom = 140.00;
const double presedentialRoom = 200.00;
const double deluxeRoom = 300.00;

//constants for additional services
const double food = 30.00;
const double snack = 10.00;
const double drink = 5.00;
const double laundry = 8.00;

class Payment {
private:
    int roomType;
    int nights;
    bool includeFood;
    bool includeSnack;
    bool includeDrink;
    bool includeLaundry;
    int paymentMethod; // 1 for cash, 2 for credit card, 3 for digital wallet

    // function to calculate room cost based on room type and nights
    double calculateRoomCost() {
        double roomRate = 0.0;

        switch (roomType) {
            case 1:
                roomRate = singleRoom;;
                break;
            case 2:
                roomRate = doubleRoom;
                break;
            case 3:
                roomRate = queenRoom;
                break;
            case 4:
                roomRate = kingRoom;
                break;
            case 5:
                roomRate = suiteRoom;
                break;
            case 6:
                roomRate = presedentialRoom;
                break;
            case 7:
                roomRate = deluxeRoom;
                break;
            default:
                cout << "Invalid room type selected." << endl;
                return 0.0;
        }

        return roomRate * nights;
    }

    // function to calculate additional service costs
    double calculateServiceCost() {
        double totalCost = 0.0;

        if (includeFood) {
            totalCost += food;
        }
        if (includeSnack) {
            totalCost += snack;
        }
        if (includeDrink) {
            totalCost += drink;
        }
        if (includeLaundry) {
            totalCost += laundry;
        }
        return totalCost;
    }

    //function to simulate different payment methods
    void processPaymentMethod(double totalCost) {
        switch (paymentMethod) {
            case 1:
                cout << "You have selected Cash payment." << endl;
                cout << "Please proceed to the counter to pay $" << totalCost << endl;
                break;
            case 2: {
                string cardNumber;
                cout << "You have selected Credit Card payment." << endl;
                cout << "Enter your credit card number: ";
                cin >> cardNumber;
                cout << "Processing payment of $" << totalCost << " through Credit Card ending with ****" << cardNumber.substr(cardNumber.length() - 4) << endl;
                break;
            }
            case 3: {
                string walletId;
                cout << "You have selected Digital Wallet payment." << endl;
                cout << "Enter your digital wallet ID: ";
                cin >> walletId;
                cout << "Processing payment of $" << totalCost << " via Digital Wallet ID: " << walletId << endl;
                break;
            }
            default:
                cout << "Invalid payment method selected." << endl;
                break;
        }
    }

public:
    //constructor to initialize the Payment object
    Payment() {
        roomType = 0;
        nights = 0;
        includeFood = false;
        includeLaundry = false;
        paymentMethod = 0;
    }

    //function to input payment details
    void inputDetails() {
        char foodOption, laundryOption;

        // Input room details
        cout << "Welcome to the Hotel Payment System" << endl;
        cout << "Select room type: " << endl;
        cout << "1. Single Room ($80 per night)" << endl;
        cout << "2. Double Room ($90 per night)" << endl;
        cout << "3. Queen Room ($100 per night)" << endl;
        cout << "4. King Room ($110 per night)" << endl;
        cout << "5. Suite Room ($140 per night)" << endl;
        cout << "6. Presidential Room ($200 per night)" << endl;
        cout << "7. Deluxe Room ($300 per night)" << endl;

        cout << "Enter room type (1-7): ";
        cin >> roomType;

        cout << "Enter number of nights: ";
        cin >> nights;

        // Input additional services
        cout << "Would you like to include food service? (y/n): ";
        cin >> foodOption;
        if (foodOption == 'y' || foodOption == 'Y') {
            includeFood = true;
        }

        cout << "Would you like to include laundry service? (y/n): ";
        cin >> laundryOption;
        if (laundryOption == 'y' || laundryOption == 'Y') {
            includeLaundry = true;
        }

        // Input payment method
        cout << "Select payment method: " << endl;
        cout << "1. Cash" << endl;
        cout << "2. Credit Card" << endl;
        cout << "3. Digital Wallet" << endl;
        cout << "Enter payment method (1-3): ";
        cin >> paymentMethod;
    }

    // Function to calculate and process the total payment
    void processPayment() {
        double roomCost = calculateRoomCost();
        double serviceCost = calculateServiceCost();
        double totalCost = roomCost + serviceCost;

        // Output the final payment details
        cout << "Room cost: $" << roomCost << endl;
        cout << "Additional service cost: $" << serviceCost << endl;
        cout << "Total payment: $" << totalCost << endl;

        // Process payment based on the selected method
        processPaymentMethod(totalCost);
    }
};

int main() {
    Payment payment;
    payment.inputDetails();
    payment.processPayment();

    return 0;
}