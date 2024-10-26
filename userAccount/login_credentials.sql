--Checks if database exists
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'userDB')
BEGIN
    CREATE DATABASE userDB;
END

--User the DB
USE userDB;

CREATE TABLE users (
    id INT IDENTITY(1 ,1) PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

--Sample Data
INSERT INTO users (username, password) VALUES ('user1', 'password1');
INSERT INTO users (username, password) VALUES ('user2', 'password2');
