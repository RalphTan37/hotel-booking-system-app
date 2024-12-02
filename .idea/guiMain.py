import sys
from paymentGUI import PaymentScreen
from createAccountScreen import CreateAccount
from loginScreen import Login
from welcomeScreen import WelcomeScreen
from homeScreen import HomeScreen
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QFont

# Main application
app = QApplication(sys.argv)
window = WelcomeScreen()
window.show()  # Show the Welcome Screen first
sys.exit(app.exec_())