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
(10, 'user_10', 'pass123', 'user10@example.com', 'Laura', 'Thomas', '1985-10-10'),
(11, 'user_11', 'pass456', 'user11@example.com', 'David', 'Jackson', '1996-11-11'),
(12, 'user_12', 'pass789', 'user12@example.com', 'Lisa', 'White', '1986-12-12'),
(13, 'user_13', 'pass123', 'user13@example.com', 'James', 'Harris', '1992-01-13'),
(14, 'user_14', 'pass456', 'user14@example.com', 'Olivia', 'Martin', '1989-02-14'),
(15, 'user_15', 'pass789', 'user15@example.com', 'Michael', 'Thompson', '1995-03-15'),
(16, 'user_16', 'pass123', 'user16@example.com', 'Sophia', 'Garcia', '1988-04-16'),
(17, 'user_17', 'pass456', 'user17@example.com', 'Anthony', 'Martinez', '1990-05-17'),
(18, 'user_18', 'pass789', 'user18@example.com', 'Emma', 'Robinson', '1987-06-18'),
(19, 'user_19', 'pass123', 'user19@example.com', 'Ryan', 'Clark', '1991-07-19'),
(20, 'user_20', 'pass456', 'user20@example.com', 'Hannah', 'Rodriguez', '1993-08-20'),
(21, 'user_21', 'pass789', 'user21@example.com', 'Jack', 'Lewis', '1986-09-21'),
(22, 'user_22', 'pass123', 'user22@example.com', 'Grace', 'Walker', '1995-10-22'),
(23, 'user_23', 'pass456', 'user23@example.com', 'Zachary', 'Hall', '1989-11-23'),
(24, 'user_24', 'pass789', 'user24@example.com', 'Ava', 'Allen', '1994-12-24'),
(25, 'user_25', 'pass123', 'user25@example.com', 'Nathan', 'Young', '1988-01-25')

-- Rooms Table
CREATE TABLE Rooms(
	RoomID INT PRIMARY KEY,
    RoomNumber INT NOT NULL UNIQUE,
    Type VARCHAR(50) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    AvailabilityDate DATE NOT NULL
)

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
(10, 110, 'Single', 115.00, '2024-11-08'),
(11, 111, 'Double', 165.00, '2024-11-14'),
(12, 112, 'Suite', 330.00, '2024-11-17'),
(13, 113, 'Single', 105.00, '2024-11-10'),
(14, 114, 'Double', 175.00, '2024-11-19'),
(15, 115, 'Suite', 310.00, '2024-11-22'),
(16, 116, 'Single', 95.00, '2024-11-08'),
(17, 117, 'Double', 155.00, '2024-11-12'),
(18, 118, 'Suite', 315.00, '2024-11-25'),
(19, 119, 'Single', 125.00, '2024-11-09'),
(20, 120, 'Double', 185.00, '2024-11-14'),
(21, 121, 'Suite', 305.00, '2024-11-18'),
(22, 122, 'Single', 130.00, '2024-11-11'),
(23, 123, 'Double', 190.00, '2024-11-15'),
(24, 124, 'Suite', 325.00, '2024-11-21'),
(25, 125, 'Single', 102.00, '2024-11-16')

