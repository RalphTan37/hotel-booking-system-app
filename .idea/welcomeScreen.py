import sys
from loginScreen import Login
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QFont

class WelcomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welcome to Hotel Booking")
        self.setFixedSize(1400, 950)
        self.setStyleSheet("background-color: #B1C29E;")

        layout = QVBoxLayout()

        welcomeFont = QFont("Times", 20)
        welcome_label = QLabel("Welcome to the Hotel Booking System!")
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setFont(welcomeFont)
        welcome_label.setStyleSheet("font-weight: bold;")

        continueFont = QFont("Times", 15)
        continue_button = QPushButton("Continue")
        continue_button.setFont(continueFont)
        continue_button.clicked.connect(self.continue_button_clicked)

        layout.addWidget(welcome_label)
        layout.addWidget(continue_button)

        self.setLayout(layout)

    def continue_button_clicked(self):
        # Close the Welcome Screen and open the Login Screen
        self.hide()  # Use hide() to hide the WelcomeScreen, not close it.
        self.login_screen = Login()
        self.login_screen.show()  # Show the Login Screen

