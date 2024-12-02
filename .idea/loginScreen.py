import sys
from createAccountScreen import CreateAccount
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QFont

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Screen")
        self.setFixedSize(1400, 950)
        self.setStyleSheet("background-color: #EBC0AB;")

        layout = QVBoxLayout()

        loginFont = QFont("Times", 20)
        login_label = QLabel("Have you booked with us before?")
        login_label.setAlignment(Qt.AlignCenter)
        login_label.setFont(loginFont)
        login_label.setStyleSheet("font-weight: bold;")

        optionsFont = QFont("Times", 15)
        yes_button = QPushButton("Yes")
        yes_button.setFont(optionsFont)
        yes_button.clicked.connect(self.yes_button_clicked)

        no_button = QPushButton("No")
        no_button.setFont(optionsFont)
        no_button.clicked.connect(self.no_button_clicked)

        layout.addWidget(login_label)
        layout.addWidget(yes_button)
        layout.addWidget(no_button)

        self.setLayout(layout)

    def yes_button_clicked(self):  # if they've booked before
        self.hide()
        self.payment_screen = PaymentScreen()
        self.payment_screen.show()

    def no_button_clicked(self):  # if they've not booked before
        self.hide()
        self.createAccount_screen = CreateAccount()
        self.createAccount_screen.show()
