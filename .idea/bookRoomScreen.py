import sys
from paymentScreen import PaymentScreen
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QListWidget, QPushButton, QVBoxLayout, QFormLayout, QComboBox, QHBoxLayout, QLineEdit, QMessageBox, QCalendarWidget
)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont

class BookRoomScreen(QWidget):
    def __init__(self, home_screen):
        super().__init__()
        self.home_screen = home_screen

        self.setWindowTitle("Book a Room")
        self.setFixedSize(1400, 950)
        self.setStyleSheet("background-color: #B1C29E;")

        # Main Layout
        layout = QVBoxLayout()

        # Title Label
        titleFont = QFont("Times", 20)
        title_label = QLabel("Search for Available Rooms")
        title_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        title_label.setFont(titleFont)
        title_label.setStyleSheet("font-weight: bold;")

        buttonFont = QFont("Times", 15)
        back_button = QPushButton("Back")
        back_button.setFont(buttonFont)
        back_button.clicked.connect(self.go_back)

        # Form Layout for Search Preferences
        form_layout = QFormLayout()
        self.room_type = QComboBox()
        self.room_type.addItems(["Single", "Double", "Queen", "King", "Suite", "Presidential", "Deluxe"])

        self.check_in_date = QCalendarWidget()
        self.check_in_date.setGridVisible(True)
        self.check_in_date.setMinimumDate(QDate.currentDate())

        self.check_out_date = QCalendarWidget()
        self.check_out_date.setGridVisible(True)
        self.check_out_date.setMinimumDate(QDate.currentDate())

        self.budget = QLineEdit()
        self.budget.setPlaceholderText("Enter your budget in $")

        form_layout.addRow("Room Type:", self.room_type)
        form_layout.addRow("Check-In Date:", self.check_in_date)
        form_layout.addRow("Check-Out Date:", self.check_out_date)
        form_layout.addRow("Budget:", self.budget)

        search_button = QPushButton("Search")
        search_button.setFont(buttonFont)
        search_button.clicked.connect(self.search_rooms)

        layout.addWidget(title_label)
        layout.addLayout(form_layout)
        layout.addWidget(search_button, alignment=Qt.AlignCenter)
        layout.addWidget(back_button, alignment=Qt.AlignCenter)


        self.results_label = QLabel("")
        self.results_label.setFont(QFont("Times", 15))
        layout.addWidget(self.results_label)

        # Room Selection
        self.room_list = QListWidget()
        self.room_list.hide()  # Hidden until search is performed
        layout.addWidget(self.room_list)

        # Confirm Booking Button
        self.confirm_button = QPushButton("Confirm Booking")
        self.confirm_button.setFont(buttonFont)
        self.confirm_button.clicked.connect(self.proceed_to_payment)
        self.confirm_button.hide()  # Hidden until a room is selected
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)

    def search_rooms(self):
        room_type = self.room_type.currentText()
        check_in_date = self.check_in_date.selectedDate().toString("MM/dd/yyyy")
        check_out_date = self.check_out_date.selectedDate().toString("MM/dd/yyyy")
        budget = self.budget.text()

        if not check_in_date or not check_out_date or not budget:
            QMessageBox.warning(self, "Input Error", "Please fill in all fields to search for rooms.")
            return

        try:
            budget = float(budget)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Budget must be a valid number.")
            return

        if QDate.fromString(check_in_date, "MM/dd/yyyy") >= QDate.fromString(check_out_date, "MM/dd/yyyy"):
            QMessageBox.warning(self, "Date Error", "Check-out date must be after the check-in date.")
            return

        available_rooms = self.get_available_rooms(room_type, check_in_date, check_out_date, budget)

        if available_rooms:
            self.room_list.clear()
            self.room_list.addItems(available_rooms)
            self.room_list.show()
            self.confirm_button.show()
            self.results_label.setText("")
        else:
            self.room_list.hide()
            self.confirm_button.hide()
            self.results_label.setText("No rooms available matching your preferences.")

    def get_available_rooms(self, room_type, check_in_date, check_out_date, budget):
        #BINDING: find available rooms function
        mock_rooms = [
            f"{room_type} Room - ${price}/night"
            for price in [100, 150, 200, 250] if price <= float(budget)
        ]
        return mock_rooms

    def proceed_to_payment(self):
        selected_room = self.room_list.currentItem()
        if not selected_room:
            QMessageBox.warning(self, "Selection Error", "Please select a room to proceed.")
        else:
            room_details = selected_room.text()
            price_per_night = int(room_details.split("$")[-1].split("/")[0])  # Extract the price
            check_in_date = self.check_in_date.selectedDate()
            check_out_date = self.check_out_date.selectedDate()
            nights = check_in_date.daysTo(check_out_date)  # Calculate nights
            total_price = price_per_night * nights

            QMessageBox.information(self, "Room Selected", f"You selected: {room_details}\nTotal Price: ${total_price}")
            self.payment_screen = PaymentScreen(self.home_screen, room_details, total_price)
            self.hide()
            self.payment_screen.show()

    def go_back(self):
        self.hide()
        self.home_screen.show()