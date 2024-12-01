CREATE DATABASE Hotel;

USE Hotel;

-- Login Credentials Table
CREATE TABLE LoginCredentials(
	ID INT PRIMARY KEY,
    Username VARCHAR(50) NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    BirthDate DATE NOT NULL
);

-- Sample Data for Login Credentials
INSERT INTO LoginCredentials (ID, Username, Password, Email, FirstName, LastName, BirthDate) VALUES 
(1, 'user_1', 'pass123', 'user1@example.com', 'John', 'Doe', '1990-01-01'),
(2, 'user_2', 'pass456', 'user2@example.com', 'Jane', 'Smith', '1992-02-02'),
(3, 'user_3', 'pass789', 'user3@example.com', 'Mike', 'Johnson', '1989-03-03'),
(4, 'user_4', 'pass123', 'user4@example.com', 'Emily', 'Davis', '1991-04-04'),
(5, 'user_5', 'pass456', 'user5@example.com', 'Chris', 'Brown', '1988-05-05'),
(6, 'user_6', 'pass789', 'user6@example.com', 'Jessica', 'Wilson', '1990-06-06'),
(7, 'user_7', 'pass123', 'user7@example.com', 'Daniel', 'Moore', '1993-07-07'),
(8, 'user_8', 'pass456', 'user8@example.com', 'Sarah', 'Taylor', '1987-08-08'),
(9, 'user_9', 'pass789', 'user9@example.com', 'Matthew', 'Anderson', '1994-09-09'),
(10, 'user_10', 'pass123', 'user10@example.com', 'Laura', 'Thomas', '1985-10-10');

-- Rooms Table
CREATE TABLE Rooms(
	RoomID INT PRIMARY KEY,
    RoomNumber INT NOT NULL UNIQUE,
    Type VARCHAR(50) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    AvailabilityDate DATE NOT NULL
);

-- Sample Data for Rooms
INSERT INTO Rooms (RoomID, RoomNumber, Type, Price, AvailabilityDate) VALUES
(1, 101, 'Single', 100.00, '2024-11-07'),
(2, 102, 'Double', 150.00, '2024-11-10'),
(3, 103, 'Suite', 300.00, '2024-11-15'),
(4, 104, 'Single', 120.00, '2024-11-08'),
(5, 105, 'Double', 180.00, '2024-11-12'),
(6, 106, 'Suite', 320.00, '2024-11-20'),
(7, 107, 'Single', 110.00, '2024-11-09'),
(8, 108, 'Double', 160.00, '2024-11-13'),
(9, 109, 'Suite', 340.00, '2024-11-18'),
(10, 110, 'Single', 115.00, '2024-11-08');

-- Payment Options Table
CREATE TABLE PaymentOptions (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT NOT NULL,
    CardHolderName VARCHAR(100),
    CardNumber VARCHAR(16),
    ExpirationDate DATE,
    CVV CHAR(3),
    PaymentType ENUM('Credit Card', 'Debit Card', 'PayPal') NOT NULL,
    PaymentDetails JSON,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (UserID) REFERENCES LoginCredentials(ID)
);

