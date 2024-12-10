from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, 
                           QLabel, QPushButton, QCalendarWidget,
                           QComboBox, QSpinBox, QTableWidget, 
                           QTableWidgetItem, QMessageBox, QFrame,
                           QGridLayout, QScrollArea, QGroupBox, QDialog, QLineEdit, QFormLayout)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont, QColor
from backend import Backend

class PaymentDialog(QDialog):
    def __init__(self, amount):
        super().__init__()
        self.amount = amount
        self.setWindowTitle("Payment")
        self.setModal(True)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Payment form
        form_layout = QFormLayout()
        self.card_number_input = QLineEdit()
        self.card_number_input.setPlaceholderText("Enter card number")
        form_layout.addRow("Card Number:", self.card_number_input)
        
        self.expiry_date_input = QLineEdit()
        self.expiry_date_input.setPlaceholderText("MM/YY")
        form_layout.addRow("Expiry Date:", self.expiry_date_input)
        
        self.cvv_input = QLineEdit()
        self.cvv_input.setPlaceholderText("CVV")
        self.cvv_input.setEchoMode(QLineEdit.Password)
        form_layout.addRow("CVV:", self.cvv_input)
        
        self.cardholder_name_input = QLineEdit()
        self.cardholder_name_input.setPlaceholderText("Cardholder Name")
        form_layout.addRow("Name on Card:", self.cardholder_name_input)
        
        layout.addLayout(form_layout)
        
        # Payment summary
        amount_label = QLabel(f"Payment Amount: ${self.amount}")
        layout.addWidget(amount_label)
        
        # Buttons
        button_layout = QHBoxLayout()
        self.pay_button = QPushButton("Pay")
        self.pay_button.clicked.connect(self.process_payment)
        
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.pay_button)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)

    def process_payment(self):
        card_number = self.card_number_input.text()
        expiry_date = self.expiry_date_input.text()
        cvv = self.cvv_input.text()
        cardholder_name = self.cardholder_name_input.text()
        
        if not card_number or not expiry_date or not cvv or not cardholder_name:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
            return
        
        if len(card_number) < 16 or not card_number.isdigit():
            QMessageBox.warning(self, "Card Error", "Invalid card number.")
            return
        
        if len(cvv) != 3 or not cvv.isdigit():
            QMessageBox.warning(self, "CVV Error", "Invalid CVV.")
            return
        
        QMessageBox.information(self, "Payment Success", "Payment was successfully processed!")
        self.accept()

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
        
        type_label = QLabel(room_type)
        type_font = QFont()
        type_font.setPointSize(14)
        type_font.setBold(True)
        type_label.setFont(type_font)
        layout.addWidget(type_label)
        
        price_label = QLabel(f"${price}/night")
        price_label.setStyleSheet("color: #27ae60; font-weight: bold;")
        layout.addWidget(price_label)
        
        features_layout = QVBoxLayout()
        for feature in features:
            feature_label = QLabel(f"• {feature}")
            features_layout.addWidget(feature_label)
        layout.addLayout(features_layout)
        
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
        self.backend = Backend()
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
        """)

    def setup_ui(self):
        layout = QVBoxLayout()
        
        welcome_text = f"Welcome back, {self.user_data['username']}!"
        welcome_label = QLabel(welcome_text)
        layout.addWidget(welcome_label)

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

