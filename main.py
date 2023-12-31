class TravelBookingSystem:
    def __init__(self):
        self.bookings = []
    
    def make_booking(self, name, destination, departure_date, return_date):
        booking = {
            'name': name,
            'destination': destination,
            'departure_date': departure_date,
            'return_date': return_date
        }
        self.bookings.append(booking)
        print("Booking successfully made!")

    def display_bookings(self):
        print("Current bookings:")
        for idx, booking in enumerate(self.bookings, start=1):
            print(f"{idx}. {booking['name']} - {booking['destination']} ({booking['departure_date']} to {booking['return_date']})")

def main():
    travel_system = TravelBookingSystem()

    while True:
        print("1. Make Booking")
        print("2. Display Bookings")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter your name: ")
            destination = input("Enter the destination: ")
            departure_date = input("Enter departure date: ")
            return_date = input("Enter return date: ")
            travel_system.make_booking(name, destination, departure_date, return_date)
        
        elif choice == '2':
            travel_system.display_bookings()
        
        elif choice == '3':
            print("Exiting the booking system.")
            break
        
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
