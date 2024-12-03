import sys
from bookRoomScreen import BookRoomScreen
from manageBookingScreen import ManageBookingScreen
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class HomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hotel Booking System - Home")
        self.setFixedSize(1400, 950)
        self.setStyleSheet("background-color: #B1C29E;")

        # Main Layout
        layout = QVBoxLayout()

        # Welcome Label
        welcomeFont = QFont("Times", 20)
        welcome_label = QLabel("Welcome to the Hotel Booking System!")
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setFont(welcomeFont)
        welcome_label.setStyleSheet("font-weight: bold;")

        # Buttons for Navigation
        buttonFont = QFont("Times", 15)
        book_button = QPushButton("Book a Room")
        book_button.setFont(buttonFont)
        book_button.clicked.connect(self.book_room)

        manage_button = QPushButton("Manage Booking")
        manage_button.setFont(buttonFont)
        manage_button.clicked.connect(self.manage_booking)

        logout_button = QPushButton("Log Out")
        logout_button.setFont(buttonFont)
        logout_button.clicked.connect(self.log_out)

        # Add Widgets to Layout
        layout.addWidget(welcome_label)
        layout.addWidget(book_button)
        layout.addWidget(manage_button)
        layout.addWidget(logout_button)

        # Align buttons to center
        layout.setAlignment(Qt.AlignCenter)

        self.setLayout(layout)

    def book_room(self):
        # Logic to navigate to the booking screen
        print("Navigating to the booking screen...")
        self.hide()
        self.book_room_screen = BookRoomScreen(self)
        self.book_room_screen.show()

    def manage_booking(self):
        # Logic to navigate to the manage booking screen
        print("Navigating to the manage booking screen...")
        self.hide()
        self.manage_booking_screen = ManageBookingScreen(self)
        self.manage_booking_screen.show()

    def log_out(self):
        # Logic to log out and return to the login screen
        print("Logging out...")
        self.close()  # Close the home screen
