#include <iostream>

using namespace std;

int main() {
    string choice;
    string username;
    string password;

    cout << "Welcome to Urban Oasis Hotel!" << endl;
    cout << endl;
    cout << "Do you have an account with us? (Y/N)" << endl;
    cin >> choice;

    if (choice == "Yes" || "yes" || "y") {
        cout << "Perfect! Please login with your credentials:" << endl;
    } else {
        cout << "Please create an account to ensure your data is saved." << endl;
    }
}
