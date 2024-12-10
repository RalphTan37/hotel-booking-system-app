from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, 
                             QPushButton, QTableWidget, QTableWidgetItem, 
                             QLabel, QScrollArea, QGroupBox, QFormLayout, QDialog)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from backend import Backend

class AdminPanel(QWidget):
    def __init__(self, user_data):
        super().__init__()
        self.user_data = user_data
        self.backend = Backend()
        self.setup_ui()
        self.setup_styles()

    def setup_ui(self):
        layout = QVBoxLayout()
        
        tabs = QTabWidget()
        
        # Create Bookings Tab
        bookings_tab = self.create_bookings_tab()
        tabs.addTab(bookings_tab, "Bookings Management")
        
        # Create Users Tab
        users_tab = self.create_users_tab()
        tabs.addTab(users_tab, "User Management")
        
        layout.addWidget(tabs)
        self.setLayout(layout)

    def create_bookings_tab(self):
        """Create the tab that shows bookings made by users."""
        tab = QWidget()
        layout = QVBoxLayout()
        
        # Bookings Table
        self.bookings_table = QTableWidget()
        self.bookings_table.setColumnCount(6)
        self.bookings_table.setHorizontalHeaderLabels([
            "Booking ID", "Room Number", "Type", "Check-in", "Check-out", "User Name"
        ])
        
        # Refresh button to reload bookings
        self.refresh_button = QPushButton("Refresh Bookings")
        self.refresh_button.clicked.connect(self.load_bookings)
        
        self.load_bookings()
        
        layout.addWidget(self.bookings_table)
        layout.addWidget(self.refresh_button)
        tab.setLayout(layout)
        return tab

    def create_users_tab(self):
        """Create the tab that shows all users in the system."""
        tab = QWidget()
        layout = QVBoxLayout()
        
        # User Management Table
        self.users_table = QTableWidget()
        self.users_table.setColumnCount(5)
        self.users_table.setHorizontalHeaderLabels(["ID", "Name", "Email", "Role", "Status"])
        
        # Connect click event to display user details
        self.users_table.cellClicked.connect(self.display_user_details)
        
        self.load_users()
        
        layout.addWidget(self.users_table)
        tab.setLayout(layout)
        return tab

    def load_bookings(self):
        """Load all bookings from the backend and display them in the table."""
        bookings = self.backend.get_all_bookings()
        self.bookings_table.setRowCount(len(bookings))
        for i, booking in enumerate(bookings):
            for j, value in enumerate(booking):
                self.bookings_table.setItem(i, j, QTableWidgetItem(str(value)))

    def load_users(self):
        """Load all users from the backend and display them in the User Management tab."""
        users = self.backend.get_all_users()
        self.users_table.setRowCount(len(users))
        for i, user in enumerate(users):
            for j, value in enumerate(user):
                self.users_table.setItem(i, j, QTableWidgetItem(str(value)))

    def display_user_details(self, row, column):
        """Show user details and booking information when a user is clicked."""
        user_id = int(self.users_table.item(row, 0).text())
        user = self.backend.get_user_by_id(user_id)
        booking = self.backend.get_booking_by_user(user[1])

        dialog = QDialog(self)
        dialog.setWindowTitle(f"{user[1]}'s Details")
        
        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"Name: {user[1]}"))
        layout.addWidget(QLabel(f"Email: {user[2]}"))
        layout.addWidget(QLabel(f"Role: {user[3]}"))
        layout.addWidget(QLabel(f"Status: {user[4]}"))

        if booking:
            layout.addWidget(QLabel(f"Room Booked: {booking[1]} ({booking[2]})"))
            layout.addWidget(QLabel(f"Check-in: {booking[3]}"))
            layout.addWidget(QLabel(f"Check-out: {booking[4]}"))
        else:
            layout.addWidget(QLabel("No bookings found for this user."))

        dialog.setLayout(layout)
        dialog.exec_()

    def setup_styles(self):
        """Apply styles for the entire Admin Panel."""
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f6fa;
            }
            QTabWidget::pane {
                border: 1px solid #dcdde1;
                border-radius: 4px;
                background-color: white;
            }
            QTabBar::tab {
                background-color: #f1f2f6;
                padding: 8px 20px;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                background-color: white;
                border-bottom: 2px solid #3498db;
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
            QTableWidget {
                background-color: white;
                border: 1px solid #dcdde1;
                border-radius: 4px;
            }
            QTableWidget::item {
                padding: 10px;
            }
            QGroupBox {
                background-color: white;
                border: 1px solid #dcdde1;
                border-radius: 8px;
                padding: 15px;
                margin-top: 10px;
            }
            QLabel {
                color: #2c3e50;
                font-size: 14px;
            }
        """)

