import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

"""
 for future work I would like to create bindings for our backend

 create Python bindings for the C++ code

 import cpp_backend
"""

class HotelBookingSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hotel Booking System")
        self.setFixedSize(1920, 1080)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.label = QLabel("Book Reservation")
        self.label.setAlignment(Qt.AlignCenter)
        font = self.label.font()
        font.setPointSize(24)
        self.label.setFont(font)

        self.button = QPushButton("Reserve Room")
        self.button.setFixedSize(200, 50)
        self.button.clicked.connect(self.on_button_clicked)

        layout.addWidget(self.label, alignment=Qt.AlignCenter)
        layout.addWidget(self.button, alignment=Qt.AlignCenter)
        layout.setSpacing(20)

    def on_button_clicked(self):
        self.label.setText("Room(s) Reserved!")
        # Here you would call your C++ backend
        # For example: cpp_backend.book_room()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HotelBookingSystem()
    window.show()
    sys.exit(app.exec_())
