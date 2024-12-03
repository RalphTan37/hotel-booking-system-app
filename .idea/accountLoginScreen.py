import sys
from homeScreen import HomeScreen
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QMessageBox, QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QFont

class AccountLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Account Login Screen")
        self.setFixedSize(1400, 950)
        self.setStyleSheet("background-color: #B1C29E;")

        main_layout = QVBoxLayout()
        layout = QFormLayout()

        spacer = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Fixed)  # Adjust height (50) as needed
        main_layout.addSpacerItem(spacer)

        accountFont = QFont("Times", 20)
        createAccount_label = QLabel("Let's get you signed in!")
        createAccount_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        createAccount_label.setFont(accountFont)
        createAccount_label.setStyleSheet("font-weight: bold;")

        main_layout.addWidget(createAccount_label)

        confirmFont = QFont("Times", 15)
        confirm_button = QPushButton("Continue")
        confirm_button.setFont(confirmFont)
        confirm_button.clicked.connect(self.confirm_button_clicked)

        self.email = QLineEdit()
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)

        layout.addRow("Email:", self.email)
        layout.addRow("Username:", self.username)
        layout.addRow("Password:", self.password)

        main_layout.addLayout(layout)
        main_layout.addWidget(confirm_button)

        self.setLayout(main_layout)

    def confirm_button_clicked(self):

        if not self.password.text() or not self.username.text() or not self.email.text():
            QMessageBox.warning(self, "Input Error", "Please fill in all account details.")
        else:
            accountFound = True
            #BINDING: Check to see if account is in database and update account Found
            if accountFound == True:
                QMessageBox.information(self, "Success!", "You've successfully logged in!")
                self.hide()
                self.home_screen = HomeScreen()
                self.home_screen.show()
            else:
                QMessageBox.warning(self, "Account not found", "Incorrect username, password, or email. Please try again.")

