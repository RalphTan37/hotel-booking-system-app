CREATE DATABASE Hotel;

USE Hotel;

CREATE TABLE LoginCredentials(
	ID INT PRIMARY KEY,
    Username VARCHAR(50) NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    BirthDate DATE
);

CREATE TABLE Rooms(
	RoomID INT PRIMARY KEY,
    RoomNumber INT NOT NULL UNIQUE,
    Type VARCHAR(50) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    AvailabilityDate DATE NOT NULL
)