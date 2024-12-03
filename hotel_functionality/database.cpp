#include "database.h"
#include <mysql.h>
#include <iostream>

MYSQL* connectDatabase() {
    MYSQL* conn = mysql_init(0);
    if (!conn) {
        std::cerr << "MySQL Initialization Failed" << std::endl;
        return nullptr;
    }

    conn = mysql_real_connect(conn, "localhost", "root", "password", "Hotel", 3306, NULL, 0);
    if (conn) {
        std::cout << "Connected to the Hotel Database!" << std::endl;
        return conn;
    }

    std::cerr << "Database Connection Failed: " << mysql_error(conn) << std::endl;
    return nullptr;
}
