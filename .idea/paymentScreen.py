from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QComboBox, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class PaymentScreen(QWidget):
    def __init__(self, home_screen, room_details, total_price):
        super().__init__()
        self.home_screen = home_screen
        self.room_details = room_details
        self.total_price = total_price

        self.setWindowTitle("Payment Screen")
        self.setFixedSize(1400, 950)
        self.setStyleSheet("background-color: #B1C29E;")

        layout = QVBoxLayout()

        # Title Label
        title = QLabel(f"Payment for ${total_price}")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Times", 20))
        title.setStyleSheet("font-weight: bold;")
        layout.addWidget(title)

        # Payment Method Selection
        self.payment_method = QComboBox()
        self.payment_method.addItems(["Select Payment Method", "Cash", "Credit Card", "Debit Card"])
        self.payment_method.currentIndexChanged.connect(self.toggle_payment_fields)

        form_layout = QFormLayout()
        form_layout.addRow("Payment Method:", self.payment_method)

        # Credit/Debit Card Details
        self.card_number = QLineEdit()
        self.card_number.setPlaceholderText("Card Number")
        self.expiry_date = QLineEdit()
        self.expiry_date.setPlaceholderText("MM/YY")
        self.cvv = QLineEdit()
        self.cvv.setPlaceholderText("CVV")
        self.cvv.setEchoMode(QLineEdit.Password)

        form_layout.addRow("Card Number:", self.card_number)
        form_layout.addRow("Expiry Date:", self.expiry_date)
        form_layout.addRow("CVV:", self.cvv)

        # Initially Hide Card Details
        self.card_number.hide()
        self.expiry_date.hide()
        self.cvv.hide()

        layout.addLayout(form_layout)

        # Pay Button
        pay_button = QPushButton("Pay Now")
        pay_button.clicked.connect(self.process_payment)
        layout.addWidget(pay_button)

        self.setLayout(layout)

    def toggle_payment_fields(self):

        payment_method = self.payment_method.currentText()

        if payment_method == "Credit Card" or payment_method == "Debit Card":
            self.card_number.show()
            self.expiry_date.show()
            self.cvv.show()
        else:  # Hide for other payment methods
            self.card_number.hide()
            self.expiry_date.hide()
            self.cvv.hide()

    def process_payment(self):

        payment_method = self.payment_method.currentText()

        if payment_method == "Select Payment Method":
            QMessageBox.warning(self, "Payment Error", "Please select a payment method.")
            return

        if payment_method == "Cash":
            QMessageBox.information(self, "Cash Payment", "Please pay at the desk to complete your booking.")
            self.hide()
            self.home_screen.show()
            return

        # Process Card Payment
        if payment_method in ["Credit Card", "Debit Card"]:
            if not self.card_number.text() or not self.expiry_date.text() or not self.cvv.text():
                QMessageBox.warning(self, "Input Error", "Please fill in all card details.")
                return


            payment_success = self.validate_payment(self.card_number.text(), self.expiry_date.text(), self.cvv.text())

            if payment_success:
                QMessageBox.information(self, "Payment Successful", "Your payment was processed successfully! Returning to home page.")
                self.hide()
                self.home_screen.show()
            else:
                QMessageBox.warning(self, "Payment Failed", "Invalid payment details. Please try again.")
                return

    def validate_payment(self, card_number, expiry_date, cvv):
        #BINDING: Validate payment details with the database

        valid_cards = {
            "1234567812345678": {"expiry_date": "12/23", "cvv": "123"},
            "9876543298765432": {"expiry_date": "01/25", "cvv": "456"},
        }

        if card_number in valid_cards:
            card_details = valid_cards[card_number]
            return card_details["expiry_date"] == expiry_date and card_details["cvv"] == cvv

        return False

    def close_payment_screen(self):

        self.hide()
        self.home_screen.show()
