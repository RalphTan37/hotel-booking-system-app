IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'hotelDB')
BEGIN
    CREATE DATABASE hotelDB;
END

USE hotelDB;


CREATE TABLE rooms (
    id INT IDENTITY(1,1) PRIMARY KEY,
    roomNumber INT NOT NULL UNIQUE,
    type VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    availabilityDate DATE NOT NULL
);

--Sample Data
INSERT INTO rooms (roomNumber, type, price, availabilityDate) VALUES (101, 'Single', 100.00, '2024-10-27');
INSERT INTO rooms (roomNumber, type, price, availabilityDate) VALUES (102, 'Double', 150.00, '2024-10-27');
INSERT INTO rooms (roomNumber, type, price, availabilityDate) VALUES (103, 'Suite', 250.00, '2024-10-28');
INSERT INTO rooms (roomNumber, type, price, availabilityDate) VALUES (104, 'Single', 100.00, '2024-10-28');

--Query rooms by type, price, and date
SELECT * FROM rooms
WHERE type = 'Single' AND price < 150.00 AND availabilityDate = '2024-10-27';
