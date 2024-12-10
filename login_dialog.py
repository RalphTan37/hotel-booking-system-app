from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QFormLayout, 
                           QLineEdit, QPushButton, QMessageBox,
                           QLabel, QCheckBox, QHBoxLayout, QFrame)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welcome to Urban Oasis Hotel")
        self.setModal(True)
        self.setStyleSheet("""
            QDialog {
                background-color: #f0f0f0;
            }
            QLabel {
                color: #2c3e50;
                font-size: 12px;
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
            QLineEdit {
                padding: 8px;
                border: 1px solid #bdc3c7;
                border-radius: 4px;
                min-width: 200px;
            }
            QLineEdit:focus {
                border: 1px solid #3498db;
            }
        """)
        self.setup_ui()
        self.user_data = None

    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Hotel Logo/Title
        title_label = QLabel("Urban Oasis Hotel")
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(24)
        title_font.setBold(True)
        title_label.setFont(title_font)
        layout.addWidget(title_label)
        
        # Welcome message
        welcome_label = QLabel("Welcome! Please sign in to continue")
        welcome_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(welcome_label)
        
        # Add some spacing
        layout.addSpacing(20)
        
        # Form layout for login fields
        form_layout = QFormLayout()
        
        self.username = QLineEdit()
        self.username.setPlaceholderText("Enter your username")
        self.password = QLineEdit()
        self.password.setPlaceholderText("Enter your password")
        self.password.setEchoMode(QLineEdit.Password)
        
        form_layout.addRow("Username:", self.username)
        form_layout.addRow("Password:", self.password)
        
        # Remember me checkbox
        self.remember_me = QCheckBox("Remember me")
        form_layout.addRow("", self.remember_me)
        
        layout.addLayout(form_layout)
        
        # Buttons layout
        buttons_layout = QHBoxLayout()
        
        login_button = QPushButton("Login")
        login_button.clicked.connect(self.handle_login)
        login_button.setDefault(True)
        
        guest_button = QPushButton("Continue as Guest")
        guest_button.clicked.connect(self.handle_guest_login)
        guest_button.setStyleSheet("""
            QPushButton {
                background-color: #95a5a6;
            }
            QPushButton:hover {
                background-color: #7f8c8d;
            }
        """)
        
        buttons_layout.addWidget(guest_button)
        buttons_layout.addWidget(login_button)
        
        layout.addLayout(buttons_layout)
        
        # Help text
        help_text = QLabel("Hint: Use any username/password. Prefix with 'admin_' for admin access")
        help_text.setAlignment(Qt.AlignCenter)
        help_text.setStyleSheet("color: #7f8c8d; font-size: 10px;")
        layout.addWidget(help_text)
        
        self.setLayout(layout)

    def handle_login(self):
        if self.username.text() and self.password.text():
            self.user_data = {
                'username': self.username.text(),
                'is_admin': self.username.text().startswith('admin_'),
                'remember_me': self.remember_me.isChecked()
            }
            self.accept()
        else:
            QMessageBox.warning(self, "Error", "Please enter both username and password")

    def handle_guest_login(self):
        self.user_data = {
            'username': 'Guest User',
            'is_admin': False,
            'is_guest': True
        }
        self.accept()
