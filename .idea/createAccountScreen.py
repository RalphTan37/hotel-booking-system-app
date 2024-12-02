import sys
from homeScreen import HomeScreen
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QMessageBox, QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QFont

class CreateAccount(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create an account")
        self.setFixedSize(1400, 950)
        self.setStyleSheet("background-color: #EBC0AB;")

        main_layout = QVBoxLayout()
        layout = QFormLayout()

        spacer = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Fixed)  # Adjust height (50) as needed
        main_layout.addSpacerItem(spacer)

        accountFont = QFont("Times", 20)
        createAccount_label = QLabel("Let's create an account for you!")
        createAccount_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        createAccount_label.setFont(accountFont)
        createAccount_label.setStyleSheet("font-weight: bold;")

        main_layout.addWidget(createAccount_label)

        confirmFont = QFont("Times", 15)
        confirm_button = QPushButton("Continue")
        confirm_button.setFont(confirmFont)
        confirm_button.clicked.connect(self.confirm_button_clicked)

        self.first_name = QLineEdit()
        self.last_name = QLineEdit()
        self.birthday = QLineEdit()
        self.birthday.setPlaceholderText("12/34/1234")
        self.email = QLineEdit()
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.passwordConfirm = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.passwordConfirm.setEchoMode(QLineEdit.Password)

        layout.addRow("First Name:", self.first_name)
        layout.addRow("Last Name:", self.last_name)
        layout.addRow("Birthday:", self.birthday)
        layout.addRow("Email:", self.email)
        layout.addRow("Create Username:", self.username)
        layout.addRow("Create Password:", self.password)
        layout.addRow("Confirm Password:", self.passwordConfirm)

        main_layout.addLayout(layout)
        main_layout.addWidget(confirm_button)

        self.setLayout(main_layout)

    def confirm_button_clicked(self):
        # Logic for confirming payment
        if not self.first_name.text() or not self.last_name.text() or not self.birthday.text() or not self.password.text() or not self.passwordConfirm.text() or not self.username.text() or not self.email.text():
            QMessageBox.warning(self, "Input Error", "Please fill in all account details.")
        elif self.password.text() != self.passwordConfirm.text():
            QMessageBox.warning(self, "Password Input Error", "Please ensure passwords match.")
        else:
            QMessageBox.information(self, "Success!", "Account Creation Successful!")
            self.hide()
            self.home_screen = HomeScreen()
            self.home_screen.show()

