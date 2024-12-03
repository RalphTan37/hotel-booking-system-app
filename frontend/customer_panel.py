from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, 
                           QLabel, QPushButton, QCalendarWidget,
                           QComboBox, QSpinBox, QTableWidget, 
                           QTableWidgetItem, QMessageBox, QFrame,
                           QGridLayout, QScrollArea, QGroupBox)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont, QColor

class RoomCard(QFrame):
    def __init__(self, room_type, price, features):
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
        if self.user_data.get('is_guest', False):
            welcome_text = "Welcome, Guest! Browse our available rooms"
        else:
            welcome_text = f"Welcome back, {self.user_data['username']}!"
        
        welcome_label = QLabel(welcome_text)
        welcome_font = QFont()
        welcome_font.setPointSize(16)
        welcome_label.setFont(welcome_font)
        layout.addWidget(welcome_label)
        
        # Search Section
        search_group = QGroupBox("Search Rooms")
        search_layout = QGridLayout()
        
        # Room type selection
        self.room_type = QComboBox()
        self.room_type.addItems([
            "Any Type",
            "Standard Room",
            "Deluxe Room",
            "Executive Suite",
            "Presidential Suite"
        ])
        search_layout.addWidget(QLabel("Room Type:"), 0, 0)
        search_layout.addWidget(self.room_type, 0, 1)
        
        # Date selection
        self.check_in_calendar = QCalendarWidget()
        self.check_in_calendar.setMinimumDate(QDate.currentDate())
        search_layout.addWidget(QLabel("Check-in Date:"), 1, 0)
        search_layout.addWidget(self.check_in_calendar, 1, 1)
        
        # Number of nights
        self.nights = QSpinBox()
        self.nights.setRange(1, 30)
        search_layout.addWidget(QLabel("Number of Nights:"), 2, 0)
        search_layout.addWidget(self.nights, 2, 1)
        
        # Number of guests
        self.guests = QSpinBox()
        self.guests.setRange(1, 4)
        search_layout.addWidget(QLabel("Number of Guests:"), 3, 0)
        search_layout.addWidget(self.guests, 3, 1)
        
        # Search button
        search_button = QPushButton("Search Available Rooms")
        search_button.clicked.connect(self.search_rooms)
        search_layout.addWidget(search_button, 4, 0, 1, 2)
        
        search_group.setLayout(search_layout)
        layout.addWidget(search_group)
        
        # Available Rooms Section
        rooms_scroll = QScrollArea()
        rooms_scroll.setWidgetResizable(True)
        rooms_container = QWidget()
        rooms_layout = QGridLayout()
        
        # Add sample room cards
        sample_rooms = [
            ("Standard Room", 100, ["Queen Bed", "City View", "Free WiFi"]),
            ("Deluxe Room", 150, ["King Bed", "Ocean View", "Minibar", "Free WiFi"]),
            ("Executive Suite", 250, ["King Bed", "Living Room", "Ocean View", "Premium Amenities"]),
            ("Presidential Suite", 500, ["Multiple Rooms", "Private Balcony", "Personal Butler", "Luxury Amenities"])
        ]
        
        for i, (room_type, price, features) in enumerate(sample_rooms):
            room_card = RoomCard(room_type, price, features)
            rooms_layout.addWidget(room_card, i // 2, i % 2)
        
        rooms_container.setLayout(rooms_layout)
        rooms_scroll.setWidget(rooms_container)
        layout.addWidget(rooms_scroll)
        
        self.setLayout(layout)

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
