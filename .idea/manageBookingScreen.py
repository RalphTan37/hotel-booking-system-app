import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, QHBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class ManageBookingScreen(QWidget):
    def __init__(self, home_screen):
        super().__init__()
        self.home_screen = home_screen

        self.setWindowTitle("Manage Your Bookings")
        self.setFixedSize(1400, 950)
        self.setStyleSheet("background-color: #B1C29E;")


        layout = QVBoxLayout()


        titleFont = QFont("Times", 20)
        title_label = QLabel("Manage Your Bookings")
        title_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        title_label.setFont(titleFont)
        title_label.setStyleSheet("font-weight: bold;")

        buttonFont = QFont("Times", 15)
        back_button = QPushButton("Back")
        back_button.setFont(buttonFont)
        back_button.clicked.connect(self.go_back)

        # Booking Search Section
        search_layout = QFormLayout()
        self.booking_id = QLineEdit()
        self.booking_id.setPlaceholderText("Enter your Booking ID")
        search_button = QPushButton("Search Booking")
        search_button.clicked.connect(self.search_booking)

        search_layout.addRow("Booking ID:", self.booking_id)
        search_layout.addRow("", search_button)

        # Booking Details Section
        self.details_table = QTableWidget()
        self.details_table.setRowCount(1)
        self.details_table.setColumnCount(4)
        self.details_table.setHorizontalHeaderLabels(["Room Type", "Check-In Date", "Check-Out Date", "Price"])
        self.details_table.setEditTriggers(QTableWidget.NoEditTriggers)  # Make it read-only
        self.details_table.hide()  # Hide table until a booking is found

        # Buttons for Updating/Canceling Booking
        self.cancel_button = QPushButton("Cancel Booking")
        self.cancel_button.setFont(buttonFont)
        self.cancel_button.clicked.connect(self.cancel_booking)
        self.cancel_button.hide()

        # Add Widgets to Layout
        layout.addWidget(title_label)
        layout.addLayout(search_layout)
        layout.addWidget(self.details_table)
        layout.addWidget(self.cancel_button, alignment=Qt.AlignCenter)
        layout.addWidget(back_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def search_booking(self):
        booking_id = self.booking_id.text()

        if not booking_id:
            QMessageBox.warning(self, "Input Error", "Please enter a Booking ID to search.")
            return

        # Simulated booking search logic
        booking = self.get_booking(booking_id)

        if booking:
            # Populate the details table with booking data
            self.cancel_button.show()
            self.details_table.show()
            self.details_table.setItem(0, 0, QTableWidgetItem(booking["room_type"]))
            self.details_table.setItem(0, 1, QTableWidgetItem(booking["check_in_date"]))
            self.details_table.setItem(0, 2, QTableWidgetItem(booking["check_out_date"]))
            self.details_table.setItem(0, 3, QTableWidgetItem(f"${booking['price']}"))
        else:
            self.details_table.hide()
            self.cancel_button.hide()
            QMessageBox.information(self, "No Booking Found", "No booking found with the provided Booking ID.")

    def get_booking(self, booking_id):
        #BINDING: Search to see if booking is currently in database
        mock_bookings = {
            "B123": {"room_type": "Suite", "check_in_date": "01/15/2024", "check_out_date": "01/20/2024", "price": 1200},
            "B456": {"room_type": "Single", "check_in_date": "01/10/2024", "check_out_date": "01/12/2024", "price": 300},
        }
        return mock_bookings.get(booking_id)


    def cancel_booking(self):
        if self.details_table.isHidden():
            QMessageBox.warning(self, "No Booking Selected", "Please search and select a booking to cancel.")
            return
        confirmation = QMessageBox.question(
            self, "Cancel Booking", "Are you sure you want to cancel this booking?", QMessageBox.Yes | QMessageBox.No
        )
        if confirmation == QMessageBox.Yes:
            self.details_table.hide()
            #BINDING: delete booking from database
            QMessageBox.information(self, "Booking Canceled", "Your booking has been successfully canceled. Returning to home page.")
            self.hide()
            self.home_screen.show()


    def go_back(self):
        self.hide()
        self.home_screen.show()