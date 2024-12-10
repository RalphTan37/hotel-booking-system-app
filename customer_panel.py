from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, 
                           QLabel, QPushButton, QCalendarWidget,
                           QComboBox, QSpinBox, QTableWidget, 
                           QTableWidgetItem, QMessageBox, QFrame,
                           QGridLayout, QScrollArea, QGroupBox)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont, QColor
from backend import Backend


class RoomCard(QFrame):
    def __init__(self, room_type, price, features):
        self.backend = Backend()
        super().__init__()
        self.setFrameStyle(QFrame.Box | QFrame.Raised)
        self.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 8px;
                border: 1px solid #dcdde1;
                padding: 10px;
            }
            QLabel {
                color: #2f3640;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 5px 10px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        
        layout = QVBoxLayout()
        
        # Room type
        type_label = QLabel(room_type)
        type_font = QFont()
        type_font.setPointSize(14)
        type_font.setBold(True)
        type_label.setFont(type_font)
        layout.addWidget(type_label)
        
        # Price
        price_label = QLabel(f"${price}/night")
        price_label.setStyleSheet("color: #27ae60; font-weight: bold;")
        layout.addWidget(price_label)
        
        # Features
        features_layout = QVBoxLayout()
        for feature in features:
            feature_label = QLabel(f"• {feature}")
            features_layout.addWidget(feature_label)
        layout.addLayout(features_layout)
        
        # Book button
        book_button = QPushButton("View Details")
        book_button.clicked.connect(lambda: self.show_room_details(room_type))
        layout.addWidget(book_button)
        
        self.setLayout(layout)

    def show_room_details(self, room_type):
        QMessageBox.information(self, "Room Details", 
            f"Detailed information about {room_type} will be available when connected to backend.")

class CustomerPanel(QWidget):
    def __init__(self, user_data):
        super().__init__()
        self.user_data = user_data
        self.setup_ui()
        self.setup_styles()

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
            QComboBox {
                padding: 5px;
                border: 1px solid #bdc3c7;
                border-radius: 4px;
            }
            QSpinBox {
                padding: 5px;
                border: 1px solid #bdc3c7;
                border-radius: 4px;
            }
            QTableWidget {
                background-color: white;
                border: 1px solid #dcdde1;
                border-radius: 4px;
            }
            QGroupBox {
                background-color: white;
                border: 1px solid #dcdde1;
                border-radius: 8px;
                padding: 10px;
                margin-top: 10px;
            }
        """)

    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Welcome message
        welcome_text = f"Welcome back, {self.user_data['username']}!"
        welcome_label = QLabel(welcome_text)
        layout.addWidget(welcome_label)

        # Search Section
        search_group = QGroupBox("Search Rooms")
        search_layout = QVBoxLayout()

        # Date selection
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


    def show_available_rooms(self):
        self.backend = Backend()
        date = self.check_in_calendar.selectedDate().toString("yyyy-MM-dd")
        available_rooms = self.backend.get_available_rooms(date)
        
        if not available_rooms:
            QMessageBox.information(self, "No Available Rooms", f"No rooms are available on {date}.")
        else:
            self.rooms_table.setRowCount(len(available_rooms))
            for i, room in enumerate(available_rooms):
                for j, value in enumerate(room):
                    self.rooms_table.setItem(i, j, QTableWidgetItem(str(value)))
                
                book_button = QPushButton("Book")
                book_button.clicked.connect(lambda _, room_id=room[0]: self.book_room(room_id, date))
                self.rooms_table.setCellWidget(i, 3, book_button)

    def book_room(self, room_id, date):
        check_in = date
        check_out = (QDate.fromString(date, "yyyy-MM-dd").addDays(1)).toString("yyyy-MM-dd")
        user_name = self.user_data['username']
        self.backend.book_room(room_id, check_in, check_out, user_name)
        QMessageBox.information(self, "Booking Confirmed", f"Room has been booked from {check_in} to {check_out} for {user_name}.")
        self.show_available_rooms()


    def search_rooms(self):
        search_details = f"""
        Search Parameters:
        - Room Type: {self.room_type.currentText()}
        - Check-in Date: {self.check_in_calendar.selectedDate().toString()}
        - Number of Nights: {self.nights.value()}
        - Number of Guests: {self.guests.value()}
        """
        QMessageBox.information(self, "Search Results", 
            f"{search_details}\n\nRoom search will be implemented when backend is connected.")
