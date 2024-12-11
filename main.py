import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, 
                           QVBoxLayout, QHBoxLayout, QPushButton,
                           QStackedWidget, QLabel, QDialog,
                           QStatusBar, QMenuBar, QMenu, QAction)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from login_dialog import LoginDialog
from customer_panel import CustomerPanel
from admin_panel import AdminPanel
from backend import Backend


class HotelBookingSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Urban Oasis Hotel")
        self.setMinimumSize(1200, 800)
        
        # Show login dialog first
        self.show_login()

    def show_login(self):
        login_dialog = LoginDialog()
        if login_dialog.exec_() == QDialog.Accepted:
            self.user_data = login_dialog.user_data
            self.setup_ui()
            self.show()
        else:
            sys.exit()

    def setup_ui(self):
        # Setup menubar
        self.create_menubar()
        
        # Setup statusbar
        self.statusBar().showMessage(f"Logged in as: {self.user_data['username']}")
        
        # Setup central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # Create header with navigation
        self.create_header()
        
        # Create stacked widget for panels
        self.stacked_widget = QStackedWidget()
        
        # Create and add panels
        self.customer_panel = CustomerPanel(self.user_data)
        self.stacked_widget.addWidget(self.customer_panel)
        
        if self.user_data.get('is_admin', False):
            self.admin_panel = AdminPanel(self.user_data)
            self.stacked_widget.addWidget(self.admin_panel)
        
        self.main_layout.addWidget(self.stacked_widget)

        self.setup_styles()

    def create_menubar(self):
        menubar = self.menuBar()
        
        # File Menu
        file_menu = menubar.addMenu("&File")
        
        logout_action = QAction("Logout", self)
        logout_action.setStatusTip("Logout from the application")
        logout_action.triggered.connect(self.handle_logout)
        file_menu.addAction(logout_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("Exit", self)
        exit_action.setStatusTip("Exit the application")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Help Menu
        help_menu = menubar.addMenu("&Help")
        
        about_action = QAction("About", self)
        about_action.setStatusTip("About Urban Oasis Hotel")
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def create_header(self):
        header_layout = QHBoxLayout()
        
        welcome_label = QLabel(f"Welcome, {self.user_data['username']}!")
        welcome_font = QFont()
        welcome_font.setPointSize(12)
        welcome_label.setFont(welcome_font)
        header_layout.addWidget(welcome_label)
        
        header_layout.addStretch()
        
        self.customer_button = QPushButton("Customer Panel")
        self.customer_button.clicked.connect(self.show_customer_panel)
        header_layout.addWidget(self.customer_button)
        
        if self.user_data.get('is_admin', False):
            self.admin_button = QPushButton("Admin Panel")
            self.admin_button.clicked.connect(self.show_admin_panel)
            header_layout.addWidget(self.admin_button)
        
        self.main_layout.addLayout(header_layout)

    def setup_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f6fa;
            }
            QMenuBar {
                background-color: #2c3e50;
                color: white;
            }
            QMenuBar::item:selected {
                background-color: #34495e;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QLabel {
                color: #2c3e50;
            }
            QStatusBar {
                background-color: #2c3e50;
                color: white;
            }
        """)

    def show_customer_panel(self):
        self.stacked_widget.setCurrentIndex(0)
        self.statusBar().showMessage("Customer Panel")

    def show_admin_panel(self):
        if hasattr(self, 'admin_panel'):
            self.stacked_widget.setCurrentIndex(1)
            self.statusBar().showMessage("Admin Panel")

    def handle_logout(self):
        self.hide()
        self.show_login()

    def show_about(self):
        from PyQt5.QtWidgets import QMessageBox
        QMessageBox.about(self, "About Urban Oasis Hotel",
            """Urban Oasis Hotel Management System
            Version 1.0
            
            A comprehensive hotel management solution
            featuring customer bookings and administrative
            controls.""")

if __name__ == '__main__':
    backend = Backend()

    app = QApplication(sys.argv)
    window = HotelBookingSystem()
    sys.exit(app.exec_())
