from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, 
                           QLabel, QPushButton, QCalendarWidget,
                           QComboBox, QSpinBox, QTableWidget, 
                           QTableWidgetItem, QMessageBox, QFrame,
                           QGridLayout, QScrollArea, QGroupBox, QDialog)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont, QColor
from backend import Backend
from payment import PaymentDialog

class CustomerPanel(QWidget):
    def __init__(self, user_data):
        super().__init__()
        self.user_data = user_data
        self.backend = Backend()
        self.setup_ui()
        self.setup_styles()

    def setup_ui(self):
        layout = QVBoxLayout()
        
        welcome_text = f"Welcome back, {self.user_data['username']}!"
        welcome_label = QLabel(welcome_text)
        layout.addWidget(welcome_label)

        if self.user_data['role'] == 'Guest':
            self.display_booking_info(layout)
        
        search_group = QGroupBox("Search Rooms")
        search_layout = QVBoxLayout()

        self.check_in_calendar = QCalendarWidget()
        self.check_in_calendar.setMinimumDate(QDate.currentDate())
        search_layout.addWidget(QLabel("Check-in Date:"))
        search_layout.addWidget(self.check_in_calendar)

        self.show_rooms_button = QPushButton("Show Available Rooms")
        self.show_rooms_button.clicked.connect(self.show_available_rooms)
        search_layout.addWidget(self.show_rooms_button)

        search_group.setLayout(search_layout)
        layout.addWidget(search_group)

        self.rooms_table = QTableWidget()
        self.rooms_table.setColumnCount(4)
        self.rooms_table.setHorizontalHeaderLabels(["Room Number", "Type", "Price", "Action"])
        layout.addWidget(self.rooms_table)

        self.setLayout(layout)

    def display_booking_info(self, layout):
        booking_info = self.backend.get_booking_by_user(self.user_data['username'])
        if booking_info:
            layout.addWidget(QLabel("Your Booking Information:"))
            for booking in booking_info:
                booking_label = QLabel(f"Room {booking[1]} ({booking[2]}) from {booking[3]} to {booking[4]}")
                layout.addWidget(booking_label)
                
                checkout_button = QPushButton("Check Out")
                checkout_button.clicked.connect(lambda _, booking_id=booking[0]: self.checkout(booking_id))
                layout.addWidget(checkout_button)

    def show_available_rooms(self):
        date = self.check_in_calendar.selectedDate().toString("yyyy-MM-dd")
        available_rooms = self.backend.get_available_rooms(date)
        if not available_rooms:
            QMessageBox.information(self, "No Available Rooms", f"No rooms are available on {date}.")
        else:
            self.rooms_table.setRowCount(len(available_rooms))
            for i, room in enumerate(available_rooms):
                for j, value in enumerate(room[:3]):
                    self.rooms_table.setItem(i, j, QTableWidgetItem(str(value)))

                book_button = QPushButton("Book")
                room_id = room[0]
                room_price = room[3]
                book_button.clicked.connect(lambda _, room_id=room_id, room_price=room_price: self.book_room(
                    room_id=room_id, 
                    room_price=room_price, 
                    check_in=date, 
                    check_out=date,  
                    user_name=self.user_data['username']
                ))
                self.rooms_table.setCellWidget(i, 3, book_button)

    def book_room(self, room_id, room_price, check_in, check_out, user_name):
        payment_dialog = PaymentDialog(room_price)
        if payment_dialog.exec_() == QDialog.Accepted:
            self.backend.book_room(room_id, check_in, check_out, user_name)
            QMessageBox.information(self, "Booking Success", "Your room has been successfully booked!")
            self.show_available_rooms()
        else:
            QMessageBox.warning(self, "Payment Failed", "Your payment was unsuccessful.")

    def checkout(self, booking_id):
        self.backend.delete_booking(booking_id)
        QMessageBox.information(self, "Check Out Success", "You have successfully checked out.")
        self.setup_ui()  # Reload UI to update booking information

    def setup_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f6fa;
            }
            QLabel {
                color: #2f3640;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
