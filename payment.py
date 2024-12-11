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
        self.card_number_input.setStyleSheet("padding: 10px; border: 2px solid #3498db; border-radius: 8px;")
        form_layout.addRow("Card Number:", self.card_number_input)
        
        self.expiry_date_input = QLineEdit()
        self.expiry_date_input.setPlaceholderText("MM/YY")
        self.expiry_date_input.setStyleSheet("padding: 10px; border: 2px solid #3498db; border-radius: 8px;")
        form_layout.addRow("Expiry Date:", self.expiry_date_input)
        
        self.cvv_input = QLineEdit()
        self.cvv_input.setPlaceholderText("CVV")
        self.cvv_input.setEchoMode(QLineEdit.Password)
        self.cvv_input.setStyleSheet("padding: 10px; border: 2px solid #3498db; border-radius: 8px;")
        form_layout.addRow("CVV:", self.cvv_input)
        
        self.cardholder_name_input = QLineEdit()
        self.cardholder_name_input.setPlaceholderText("Cardholder Name")
        self.cardholder_name_input.setStyleSheet("padding: 10px; border: 2px solid #3498db; border-radius: 8px;")
        form_layout.addRow("Name on Card:", self.cardholder_name_input)
        
        layout.addLayout(form_layout)
        
        # Payment summary
        amount_label = QLabel(f"Payment Amount: ${self.amount}")
        amount_label.setStyleSheet("font-weight: bold; font-size: 16px; color: #2c3e50;")
        layout.addWidget(amount_label)
        
        # Buttons
        button_layout = QHBoxLayout()
        self.pay_button = QPushButton("Pay")
        self.pay_button.setStyleSheet("background-color: #27ae60; color: white; padding: 10px 20px; font-weight: bold; border-radius: 8px;")
        self.pay_button.clicked.connect(self.process_payment)
        
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setStyleSheet("background-color: #e74c3c; color: white; padding: 10px 20px; font-weight: bold; border-radius: 8px;")
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

