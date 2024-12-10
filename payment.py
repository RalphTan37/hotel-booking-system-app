from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, 
                           QLabel, QPushButton, QLineEdit,
                           QFormLayout, QComboBox, QGroupBox,
                           QMessageBox, QStackedWidget, QRadioButton,
                           QButtonGroup)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class PaymentPanel(QWidget):
    def __init__(self, user_data, booking_info=None):
        super().__init__()
        self.user_data = user_data
        self.booking_info = booking_info
        self.setup_ui()
        self.setup_styles()

    def setup_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f6fa;
            }
            QGroupBox {
                background-color: white;
                border: 1px solid #dcdde1;
                border-radius: 8px;
                padding: 15px;
                margin-top: 10px;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #bdc3c7;
                border-radius: 4px;
                min-width: 200px;
            }
            QLineEdit:focus {
                border: 1px solid #3498db;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QRadioButton {
                padding: 5px;
            }
            QLabel {
                color: #2c3e50;
            }
        """)

    def setup_ui(self):
        layout = QVBoxLayout()

        # Booking Summary
        summary_group = QGroupBox("Booking Summary")
        summary_layout = QFormLayout()
        
        if self.booking_info:
            room_info = QLabel(f"Room: {self.booking_info.get('room_type', 'Standard Room')}")
            dates_info = QLabel(f"Dates: {self.booking_info.get('check_in', 'Not specified')} - {self.booking_info.get('check_out', 'Not specified')}")
            total_info = QLabel(f"Total: ${self.booking_info.get('total', '0.00')}")
            
            summary_layout.addRow("Room:", room_info)
            summary_layout.addRow("Dates:", dates_info)
            summary_layout.addRow("Total Amount:", total_info)
        else:
            summary_layout.addRow(QLabel("No booking information available"))
        
        summary_group.setLayout(summary_layout)
        layout.addWidget(summary_group)

        # Payment Method Selection
        payment_group = QGroupBox("Payment Method")
        payment_layout = QVBoxLayout()
        
        self.payment_stack = QStackedWidget()
        
        # Radio buttons for payment method selection
        method_layout = QHBoxLayout()
        self.payment_methods = QButtonGroup()
        
        credit_radio = QRadioButton("Credit Card")
        credit_radio.setChecked(True)
        credit_radio.clicked.connect(lambda: self.payment_stack.setCurrentIndex(0))
        self.payment_methods.addButton(credit_radio)
        method_layout.addWidget(credit_radio)
        
        debit_radio = QRadioButton("Debit Card")
        debit_radio.clicked.connect(lambda: self.payment_stack.setCurrentIndex(0))
        self.payment_methods.addButton(debit_radio)
        method_layout.addWidget(debit_radio)
        
        paypal_radio = QRadioButton("PayPal")
        paypal_radio.clicked.connect(lambda: self.payment_stack.setCurrentIndex(1))
        self.payment_methods.addButton(paypal_radio)
        method_layout.addWidget(paypal_radio)
        
        payment_layout.addLayout(method_layout)

        # Credit/Debit Card Form
        card_widget = QWidget()
        card_layout = QFormLayout()
        
        self.card_number = QLineEdit()
        self.card_number.setPlaceholderText("1234 5678 9012 3456")
        card_layout.addRow("Card Number:", self.card_number)
        
        self.card_name = QLineEdit()
        self.card_name.setPlaceholderText("John Doe")
        card_layout.addRow("Cardholder Name:", self.card_name)
        
        expiry_layout = QHBoxLayout()
        self.expiry_month = QComboBox()
        self.expiry_month.addItems([str(i).zfill(2) for i in range(1, 13)])
        self.expiry_year = QComboBox()
        self.expiry_year.addItems([str(i) for i in range(2024, 2035)])
        expiry_layout.addWidget(self.expiry_month)
        expiry_layout.addWidget(self.expiry_year)
        card_layout.addRow("Expiry Date:", expiry_layout)
        
        self.cvv = QLineEdit()
        self.cvv.setPlaceholderText("123")
        self.cvv.setMaxLength(3)
        card_layout.addRow("CVV:", self.cvv)
        
        card_widget.setLayout(card_layout)
        self.payment_stack.addWidget(card_widget)

        # PayPal Form
        paypal_widget = QWidget()
        paypal_layout = QFormLayout()
        
        self.paypal_email = QLineEdit()
        self.paypal_email.setPlaceholderText("email@example.com")
        paypal_layout.addRow("PayPal Email:", self.paypal_email)
        
        paypal_widget.setLayout(paypal_layout)
        self.payment_stack.addWidget(paypal_widget)

        payment_layout.addWidget(self.payment_stack)
        payment_group.setLayout(payment_layout)
        layout.addWidget(payment_group)

        # Billing Address
        address_group = QGroupBox("Billing Address")
        address_layout = QFormLayout()
        
        self.street = QLineEdit()
        address_layout.addRow("Street Address:", self.street)
        
        self.city = QLineEdit()
        address_layout.addRow("City:", self.city)
        
        self.state = QLineEdit()
        address_layout.addRow("State:", self.state)
        
        self.zip_code = QLineEdit()
        address_layout.addRow("ZIP Code:", self.zip_code)
        
        address_group.setLayout(address_layout)
        layout.addWidget(address_group)

        # Payment Buttons
        buttons_layout = QHBoxLayout()
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.cancel_payment)
        cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        
        pay_btn = QPushButton("Process Payment")
        pay_btn.clicked.connect(self.process_payment)
        
        buttons_layout.addWidget(cancel_btn)
        buttons_layout.addWidget(pay_btn)
        
        layout.addLayout(buttons_layout)
        self.setLayout(layout)

    def process_payment(self):
        # This would normally connect to the backend
        QMessageBox.information(self, "Payment Processing",
            "Payment processing will be implemented when backend is connected.\n\n"
            "Payment Details Preview:\n"
            f"- Payment Method: {self.payment_methods.checkedButton().text()}\n"
            f"- Amount: ${self.booking_info['total'] if self.booking_info else '0.00'}")

    def cancel_payment(self):
        reply = QMessageBox.question(self, "Cancel Payment",
            "Are you sure you want to cancel this payment?",
            QMessageBox.Yes | QMessageBox.No)
            
        if reply == QMessageBox.Yes:
            self.parent().stacked_widget.setCurrentIndex(0)  # Return to customer panel

    def validate_card_details(self):
        if len(self.card_number.text().replace(" ", "")) != 16:
            return False, "Invalid card number"
        if len(self.cvv.text()) != 3:
            return False, "Invalid CVV"
        if not self.card_name.text():
            return False, "Cardholder name is required"
        return True, "Valid"

    def validate_paypal(self):
        import re
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, self.paypal_email.text()):
            return False, "Invalid email address"
        return True, "Valid"
