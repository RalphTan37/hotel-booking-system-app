#include "user_account.h"
#include <sstream>

bool UserAccount::verifyCredentials(MYSQL* conn, const std::string& username, 
                                  const std::string& password) {
    std::stringstream query;
    query << "SELECT COUNT(*) FROM LoginCredentials WHERE "
          << "Username = '" << username << "' AND Password = '" << password << "'";
    
    if (mysql_query(conn, query.str().c_str()) != 0) {
        return false;
    }
    
    MYSQL_RES* result = mysql_store_result(conn);
    MYSQL_ROW row = mysql_fetch_row(result);
    bool verified = (std::stoi(row[0]) > 0);
    mysql_free_result(result);
    return verified;
}

User UserAccount::getUserDetails(MYSQL* conn, const std::string& username) {
    User user;
    std::stringstream query;
    query << "SELECT * FROM LoginCredentials WHERE Username = '" << username << "'";
    
    if (mysql_query(conn, query.str().c_str()) != 0) {
        return user;
    }
    
    MYSQL_RES* result = mysql_store_result(conn);
    MYSQL_ROW row = mysql_fetch_row(result);
    
    if (row) {
        user.id = std::stoi(row[0]);
        user.username = row[1];
        user.email = row[3];
        user.firstName = row[4];
        user.lastName = row[5];
        user.isAdmin = user.username.find("admin_") == 0;
    }
    
    mysql_free_result(result);
    return user;
}

bool UserAccount::updatePassword(MYSQL* conn, const std::string& username, 
                               const std::string& newPassword) {
    std::stringstream query;
    query << "UPDATE LoginCredentials SET Password = '" << newPassword 
          << "' WHERE Username = '" << username << "'";
    return (mysql_query(conn, query.str().c_str()) == 0);
}
