IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'userDB')
BEGIN
    CREATE DATABASE userDB;
END

USE userDB;

CREATE TABLE users (
    id INT IDENTITY(1 ,1) PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100),
    firstname VARCHAR(100),
    lastname VARCHAR(100),
    birthdate DATE
);

--Sample Data
INSERT INTO users (username, password, email, firstname, lastname, birthdate) VALUES ('user1', 'password1', 'user1@example.com', 'John', 'Doe', '1990-01-01');
INSERT INTO users (username, password, email, firstname, lastname, birthdate) VALUES ('user2', 'password2', 'user2@example.com', 'Jane', 'Smith', '1992-02-02');
