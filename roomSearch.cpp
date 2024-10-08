#include <iostream>
#include <numeric>
#include <algorithm>
#include <ranges>
#include <vector>
using namespace std;

void roomSearch(vector<bool> vacants, vector<string> roomTypes, vector<float> roomPrices, string roomType, string hasMax, float maxBudget) {
    vector<int> currRooms; //Rooms suitable for the current customer
    for (int i = 0; i < 100; i++) {
        if (vacants[i]) {
            if (roomTypes[i] == roomType) {
                if (hasMax == "Yes") {
                    if (roomPrices[i] <= maxBudget) {
                        currRooms.push_back(i + 1);
                    }
                } else {
                    currRooms.push_back(i + 1);
                }
            }
        }
    }

    if (currRooms.size() == 0) {
        cout << "Unfortunately, we don't have any rooms with those specifications for the dates entered, would you like to see other options?" << endl;
        string option;
        cin >> option;
        if (option == "Yes" || option == "yes") {
            cout << "The room types we have available for the dates entered are:" << endl;
            vector<string> currTypes;
            for (int i = 0; i < 100; i++) {
                if (vacants[i] == true) {
                    auto it = find(currTypes.begin(), currTypes.end(), roomTypes[i]);
                    if (it == currTypes.end()) {
                        currTypes.push_back(roomTypes[i]);
                        cout << roomTypes[i] << endl;
                    }
                }
            }
        }
    } else {
        cout << "There are " << currRooms.size() << " rooms that match you preferences. Here are the available rooms that match your preferences:" << endl;
        for (int i = 0; i < currRooms.size(); i++) {
            cout << currRooms[i];
            if (i != currRooms.size() - 1) {
                std::cout << ", ";
            }
        }
        cout << endl;
    }
}

void bookRoom(vector<bool> vacants, vector<string> roomTypes, vector<float> roomPrices, int roomNum) {
    vacants[roomNum - 1] = false;
    cout << "Got it! Room " << roomNum << " is booked for you! This room is a " << roomTypes[roomNum -1] << " room and costs $" << roomPrices[roomNum - 1] << " per night. Thank you!" << endl;
}

int main() {
    vector<int> roomNums(100);
    iota(roomNums.begin(), roomNums.end(), 1); //Fills vector with nums 1-100

    vector<string> roomTypes(100);
    fill(roomTypes.begin(), roomTypes.begin() + 29, "Single");
    fill(roomTypes.begin() + 29, roomTypes.begin() + 49, "Double");
    fill(roomTypes.begin() + 49, roomTypes.begin() + 69, "Queen");
    fill(roomTypes.begin() + 69, roomTypes.begin() + 79, "King");
    fill(roomTypes.begin() + 79, roomTypes.begin() + 89, "Suite");
    fill(roomTypes.begin() + 89, roomTypes.begin() + 94, "Presidential");
    fill(roomTypes.begin() + 94, roomTypes.begin() + 99, "Deluxe");

    vector<float> roomPrices(100);
    fill(roomPrices.begin(), roomPrices.begin() + 29, 80.00);
    fill(roomPrices.begin() + 29, roomPrices.begin() + 49, 90.00);
    fill(roomPrices.begin() + 49, roomPrices.begin() + 69, 100.00);
    fill(roomPrices.begin() + 69, roomPrices.begin() + 79, 110.00);
    fill(roomPrices.begin() + 79, roomPrices.begin() + 89, 140.00);
    fill(roomPrices.begin() + 89, roomPrices.begin() + 94, 200.00);
    fill(roomPrices.begin() + 94, roomPrices.begin() + 99, 300.00);

    vector<bool> vacants(100);
    fill(vacants.begin(), vacants.end(), true);

    string roomType;
    int startDate;
    int endDate;
    string hasMax;
    float maxBudget;

    cout << "Enter start date: (MMDDYYYY) " << endl;
    cin >> startDate;
    cout << "Enter end date: (MMDDYYYY) " << endl;
    cin >> endDate;

    cout << "What room type would you like?" << endl;
    cin >> roomType;

    cout << "Do you have a maximum amount you would like to spend today?" << endl;
    cin >> hasMax;
    if (hasMax == "Yes" || hasMax == "yes") {
        cout << "What is that maximum?" << endl;
        cin >> maxBudget;
    }

    roomSearch(vacants, roomTypes, roomPrices, roomType, hasMax, maxBudget);

    int roomWanted;

    cout << "Would you like to book one of these rooms?" << endl;
    string wantBook;
    cin >> wantBook;
    if (wantBook == "Yes" || wantBook == "yes") {
        cout << "Which room would you like to book?" << endl;
        cin >> roomWanted;
        bookRoom(vacants, roomTypes, roomPrices, roomWanted);
    } else {
        cout << "Have a great day!" << endl;
    }

    return 0;
}
