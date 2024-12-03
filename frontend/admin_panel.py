from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, 
                           QPushButton, QTableWidget, QTableWidgetItem,
                           QMessageBox, QLabel, QComboBox, QSpinBox,
                           QGroupBox, QFormLayout, QLineEdit, QCalendarWidget,
                           QCheckBox, QGridLayout, QScrollArea)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont, QColor

class AdminPanel(QWidget):
    def __init__(self, user_data):
        super().__init__()
        self.user_data = user_data
        self.setup_ui()
        self.setup_styles()

    def setup_styles(self):
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
            QGroupBox {
                background-color: white;
                border: 1px solid #dcdde1;
                border-radius: 8px;
                padding: 15px;
                margin-top: 10px;
            }
            QLineEdit, QComboBox, QSpinBox {
                padding: 5px;
                border: 1px solid #bdc3c7;
                border-radius: 4px;
                min-width: 150px;
            }
        """)

    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Create dashboard header
        header = QHBoxLayout()
        title = QLabel("Admin Dashboard")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title.setFont(title_font)
        header.addWidget(title)
        
        # Add quick action buttons
        quick_actions = QHBoxLayout()
        add_room_btn = QPushButton("Add New Room")
        add_room_btn.clicked.connect(self.add_new_room)
        quick_actions.addWidget(add_room_btn)
        
        view_reports_btn = QPushButton("View Reports")
        view_reports_btn.clicked.connect(self.view_reports)
        quick_actions.addWidget(view_reports_btn)
        
        header.addLayout(quick_actions)
        layout.addLayout(header)
        
        # Create tab widget
        tabs = QTabWidget()
        
        # Bookings Management Tab
        bookings_tab = self.create_bookings_tab()
        tabs.addTab(bookings_tab, "Bookings Management")
        
        # Rooms Management Tab
        rooms_tab = self.create_rooms_tab()
        tabs.addTab(rooms_tab, "Rooms Management")
        
        # User Management Tab
        users_tab = self.create_users_tab()
        tabs.addTab(users_tab, "User Management")
        
        # Settings Tab
        settings_tab = self.create_settings_tab()
        tabs.addTab(settings_tab, "Settings")
        
        layout.addWidget(tabs)
        self.setLayout(layout)

    def create_bookings_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        # Filters
        filters_group = QGroupBox("Filters")
        filters_layout = QHBoxLayout()
        
        self.booking_status = QComboBox()
        self.booking_status.addItems(["All", "Active", "Completed", "Cancelled"])
        filters_layout.addWidget(QLabel("Status:"))
        filters_layout.addWidget(self.booking_status)
        
        self.date_range = QComboBox()
        self.date_range.addItems(["Today", "This Week", "This Month", "All Time"])
        filters_layout.addWidget(QLabel("Date Range:"))
        filters_layout.addWidget(self.date_range)
        
        filters_group.setLayout(filters_layout)
        layout.addWidget(filters_group)
        
        # Bookings Table
        self.bookings_table = QTableWidget()
        self.bookings_table.setColumnCount(6)
        self.bookings_table.setHorizontalHeaderLabels([
            "Booking ID", "Guest Name", "Room", "Check-in", "Check-out", "Status"
        ])
        
        # Add sample data
        self.populate_sample_bookings()
        
        layout.addWidget(self.bookings_table)
        
        # Action Buttons
        actions = QHBoxLayout()
        refresh_btn = QPushButton("Refresh")
        refresh_btn.clicked.connect(self.refresh_bookings)
        actions.addWidget(refresh_btn)
        
        export_btn = QPushButton("Export")
        export_btn.clicked.connect(self.export_bookings)
        actions.addWidget(export_btn)
        
        layout.addLayout(actions)
        
        tab.setLayout(layout)
        return tab

    def create_rooms_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        # Room Management Controls
        controls_group = QGroupBox("Room Controls")
        controls_layout = QHBoxLayout()
        
        self.room_type_filter = QComboBox()
        self.room_type_filter.addItems(["All Types", "Standard", "Deluxe", "Suite"])
        controls_layout.addWidget(QLabel("Type:"))
        controls_layout.addWidget(self.room_type_filter)
        
        self.room_status_filter = QComboBox()
        self.room_status_filter.addItems(["All Status", "Available", "Occupied", "Maintenance"])
        controls_layout.addWidget(QLabel("Status:"))
        controls_layout.addWidget(self.room_status_filter)
        
        controls_group.setLayout(controls_layout)
        layout.addWidget(controls_group)
        
        # Rooms Table
        self.rooms_table = QTableWidget()
        self.rooms_table.setColumnCount(5)
        self.rooms_table.setHorizontalHeaderLabels([
            "Room Number", "Type", "Status", "Price", "Last Cleaned"
        ])
        
        # Add sample data
        self.populate_sample_rooms()
        
        layout.addWidget(self.rooms_table)
        
        tab.setLayout(layout)
        return tab

    def create_users_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        # User Management Table
        self.users_table = QTableWidget()
        self.users_table.setColumnCount(5)
        self.users_table.setHorizontalHeaderLabels([
            "User ID", "Name", "Email", "Role", "Status"
        ])
        
        # Add sample data
        self.populate_sample_users()
        
        layout.addWidget(self.users_table)
        
        tab.setLayout(layout)
        return tab

    def create_settings_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        
        settings_form = QFormLayout()
        
        # Hotel Information
        hotel_name = QLineEdit("Urban Oasis Hotel")
        settings_form.addRow("Hotel Name:", hotel_name)
        
        hotel_address = QLineEdit("123 Paradise Street")
        settings_form.addRow("Address:", hotel_address)
        
        # Booking Settings
        max_booking_days = QSpinBox()
        max_booking_days.setRange(1, 365)
        max_booking_days.setValue(30)
        settings_form.addRow("Max Booking Days:", max_booking_days)
        
        # Features
        enable_online_booking = QCheckBox()
        enable_online_booking.setChecked(True)
        settings_form.addRow("Enable Online Booking:", enable_online_booking)
        
        enable_guest_accounts = QCheckBox()
        enable_guest_accounts.setChecked(True)
        settings_form.addRow("Allow Guest Accounts:", enable_guest_accounts)
        
        # Save Button
        save_btn = QPushButton("Save Settings")
        save_btn.clicked.connect(self.save_settings)
        
        layout.addLayout(settings_form)
        layout.addWidget(save_btn)
        
        tab.setLayout(layout)
        return tab

    # Helper methods to populate sample data
    def populate_sample_bookings(self):
        sample_data = [
            ("B001", "John Doe", "101", "2024-12-05", "2024-12-07", "Active"),
            ("B002", "Jane Smith", "102", "2024-12-06", "2024-12-08", "Confirmed"),
            ("B003", "Bob Wilson", "103", "2024-12-07", "2024-12-10", "Pending")
        ]
        
        self.bookings_table.setRowCount(len(sample_data))
        for i, row in enumerate(sample_data):
            for j, value in enumerate(row):
                self.bookings_table.setItem(i, j, QTableWidgetItem(str(value)))

    def populate_sample_rooms(self):
        sample_data = [
            ("101", "Standard", "Available", "$100", "2024-12-01"),
            ("102", "Deluxe", "Occupied", "$150", "2024-12-02"),
            ("103", "Suite", "Maintenance", "$250", "2024-12-03")
        ]
        
        self.rooms_table.setRowCount(len(sample_data))
        for i, row in enumerate(sample_data):
            for j, value in enumerate(row):
                self.rooms_table.setItem(i, j, QTableWidgetItem(str(value)))

    def populate_sample_users(self):
        sample_data = [
            ("U001", "John Admin", "john@hotel.com", "Admin", "Active"),
            ("U002", "Mary Staff", "mary@hotel.com", "Staff", "Active"),
            ("U003", "Bob Guest", "bob@email.com", "Guest", "Inactive")
        ]
        
        self.users_table.setRowCount(len(sample_data))
        for i, row in enumerate(sample_data):
            for j, value in enumerate(row):
                self.users_table.setItem(i, j, QTableWidgetItem(str(value)))

    # Action handlers
    def add_new_room(self):
        QMessageBox.information(self, "Add Room", 
            "Room addition will be implemented when backend is connected.")

    def view_reports(self):
        QMessageBox.information(self, "Reports", 
            "Reporting functionality will be implemented when backend is connected.")

    def refresh_bookings(self):
        QMessageBox.information(self, "Refresh", 
            "Refresh functionality will be implemented when backend is connected.")

    def export_bookings(self):
        QMessageBox.information(self, "Export", 
            "Export functionality will be implemented when backend is connected.")

    def save_settings(self):
        QMessageBox.information(self, "Settings", 
            "Settings will be saved when backend is connected.")
