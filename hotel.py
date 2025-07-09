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
            print(f"Room {self.room_number} ({self.room_type}) is booked from {start_date} to {end_date}.")
        else:
            print(f"Room {self.room_number} ({self.room_type}) is not avaliable for the selected dates.")

    def free_room(self):
        self.is_avaliable = True
        self.booked_dates = []
        self.guest = None
        print(f"Room {self.room_number} is now available.")

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
                if room.is_room_avaliable(start_date, end_date):
                    room.book_room(start_date, end_date, guest)
                else:
                    print(f"Room {room_number} is not available for the selected dates.")
                return
        print(f"Room {room_number} not found.")

    def free_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                room.free_room()
                return
        print(f"Room {room_number} not found.")

    def check_availability(self, start_date, end_date):
        available_rooms = [f"{room.room_number} ({room.room_type})" for room in self.rooms if room.is_room_avaliable(start_date, end_date)]
        if available_rooms:
            print("Available rooms:", available_rooms)
        else:
            print("No rooms available.")

    def show_booked_rooms(self):
        for room in self.rooms:
            if not room.is_avaliable:
                print(f"Room {room.room_number} ({room.room_type}) is booked by {room.guest.name} ({room.guest.phone_number}).")
                for booking in room.booked_dates:
                    print(f"    - From {booking['start_date']} to {booking['end_date']}")

def hotel_management_system():
    hotel = Hotel("Ocean View Hotel")

    hotel.add_room(Room(101, "Single"))
    hotel.add_room(Room(102, "Double"))
    hotel.add_room(Room(103, "Suite"))

    while True:
        print("\n--- Hotel Management System ---")
        print("1. Book a Room")
        print("2. Free a Room")
        print("3. Check Room Availability")
        print("4. Show Booked Rooms")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            guest_name = input("Enter guest name: ")
            phone_number = input("Enter guest phone number: ")
            room_number = int(input("Enter room number to book: "))
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
            guest = Guest(guest_name, phone_number)
            hotel.book_room(room_number, guest, start_date, end_date)
        elif choice == '2':
            room_number = int(input("Enter room number to free: "))
            hotel.free_room(room_number)
        elif choice == '3':
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
            hotel.check_availability(start_date, end_date)
        elif choice == '4':
            hotel.show_booked_rooms()
        elif choice == '5':
            print("Exiting the system...")
            break
        else:
            print("Invalid choice, please try again.")

hotel_management_system()
