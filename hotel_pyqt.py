from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox, QLineEdit, QLabel, QListWidget, QInputDialog
from datetime import datetime

class Room:
    def __init__(self, room_number, room_type):
        self.room_number = room_number
        self.room_type = room_type
        self.is_avaliable = True
        self.booked_dates = []
        self.guest = None

    def is_room_avaliable(self, start_date, end_date):
        for booking in self.booked_dates:
            if start_date <= booking['end_date'] and end_date >= booking['start_date']:
                return False
        return True

    def book_room(self, start_date, end_date, guest):
        if self.is_room_avaliable(start_date, end_date):
            self.is_avaliable = False
            self.guest = guest
            self.booked_dates.append({'start_date': start_date, 'end_date': end_date})
            return True
        return False

    def free_room(self):
        self.is_avaliable = True
        self.booked_dates = []
        self.guest = None

class Guest:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def book_room(self, room_number, guest, start_date, end_date):
        for room in self.rooms:
            if room.room_number == room_number:
                return room.book_room(start_date, end_date, guest)
        return False

    def free_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                room.free_room()
                return True
        return False

    def check_availability(self, start_date, end_date):
        return [f"{room.room_number} ({room.room_type})" for room in self.rooms if room.is_room_avaliable(start_date, end_date)]

    def show_booked_rooms(self):
        booked_rooms = []
        for room in self.rooms:
            if not room.is_avaliable:
                room_info = f"Room {room.room_number} ({room.room_type}) - Guest: {room.guest.name}, Phone: {room.guest.phone_number}"
                bookings = [f"From {b['start_date']} to {b['end_date']}" for b in room.booked_dates]
                booked_rooms.append((room_info, bookings))
        return booked_rooms

class HotelManagementSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.hotel = Hotel("Ocean View Hotel")
        self.hotel.add_room(Room(101, "Single"))
        self.hotel.add_room(Room(102, "Double"))
        self.hotel.add_room(Room(103, "Suite"))

        self.setWindowTitle("Hotel Management System")
        self.setGeometry(300, 300, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.book_room_button = QPushButton("Book a Room")
        self.book_room_button.clicked.connect(self.book_room)
        layout.addWidget(self.book_room_button)

        self.free_room_button = QPushButton("Free a Room")
        self.free_room_button.clicked.connect(self.free_room)
        layout.addWidget(self.free_room_button)

        self.check_availability_button = QPushButton("Check Room Availability")
        self.check_availability_button.clicked.connect(self.check_availability)
        layout.addWidget(self.check_availability_button)

        self.show_booked_rooms_button = QPushButton("Show Booked Rooms")
        self.show_booked_rooms_button.clicked.connect(self.show_booked_rooms)
        layout.addWidget(self.show_booked_rooms_button)

        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.close)
        layout.addWidget(self.exit_button)

        self.central_widget.setLayout(layout)

    def book_room(self):
        room_number, ok = QInputDialog.getInt(self, "Book a Room", "Enter Room Number:")
        if not ok:
            return
        guest_name, ok = QInputDialog.getText(self, "Book a Room", "Enter Guest Name:")
        if not ok or not guest_name:
            return
        phone_number, ok = QInputDialog.getText(self, "Book a Room", "Enter Phone Number:")
        if not ok or not phone_number:
            return
        start_date, ok = QInputDialog.getText(self, "Book a Room", "Enter Start Date (YYYY-MM-DD):")
        if not ok or not start_date:
            return
        end_date, ok = QInputDialog.getText(self, "Book a Room", "Enter End Date (YYYY-MM-DD):")
        if not ok or not end_date:
            return

        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid date format. Use YYYY-MM-DD.")
            return

        guest = Guest(guest_name, phone_number)
        if self.hotel.book_room(room_number, guest, start_date, end_date):
            QMessageBox.information(self, "Success", f"Room {room_number} booked successfully!")
        else:
            QMessageBox.warning(self, "Error", f"Room {room_number} is not available for the selected dates.")

    def free_room(self):
        room_number, ok = QInputDialog.getInt(self, "Free a Room", "Enter Room Number:")
        if not ok:
            return

        if self.hotel.free_room(room_number):
            QMessageBox.information(self, "Success", f"Room {room_number} is now available!")
        else:
            QMessageBox.warning(self, "Error", f"Room {room_number} not found or already available.")

    def check_availability(self):
        start_date, ok = QInputDialog.getText(self, "Check Availability", "Enter Start Date (YYYY-MM-DD):")
        if not ok or not start_date:
            return
        end_date, ok = QInputDialog.getText(self, "Check Availability", "Enter End Date (YYYY-MM-DD):")
        if not ok or not end_date:
            return

        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid date format. Use YYYY-MM-DD.")
            return

        available_rooms = self.hotel.check_availability(start_date, end_date)
        if available_rooms:
            QMessageBox.information(self, "Available Rooms", "\n".join(available_rooms))
        else:
            QMessageBox.information(self, "Available Rooms", "No rooms available for the selected dates.")

    def show_booked_rooms(self):
        booked_rooms = self.hotel.show_booked_rooms()
        if booked_rooms:
            details = ""
            for room_info, bookings in booked_rooms:
                details += room_info + "\n" + "\n".join(f"  - {b}" for b in bookings) + "\n\n"
            QMessageBox.information(self, "Booked Rooms", details)
        else:
            QMessageBox.information(self, "Booked Rooms", "No rooms are currently booked.")

if __name__ == "__main__":
    app = QApplication([])
    window = HotelManagementSystem()
    window.show()
    app.exec_()