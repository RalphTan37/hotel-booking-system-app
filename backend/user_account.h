#pragma once
#include <string>
#include <mysql.h>

struct User {
    int id;
    std::string username;
    std::string email;
    std::string firstName;
    std::string lastName;
    bool isAdmin;
};

class UserAccount {
public:
    static bool verifyCredentials(MYSQL* conn, const std::string& username, 
                                const std::string& password);
    static User getUserDetails(MYSQL* conn, const std::string& username);
    static bool updatePassword(MYSQL* conn, const std::string& username, 
                             const std::string& newPassword);
};
