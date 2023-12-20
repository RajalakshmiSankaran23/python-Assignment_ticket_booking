from ticket_booking.entity.model import Event
from ticket_booking.dao.venue_dao import InMemoryVenueDAO
from ticket_booking.dao.event_dao import InMemoryEventDAO
from ticket_booking.dao.customer_dao import InMemoryCustomerDAO
from ticket_booking.dao.booking_dao import InMemoryBookingDAO
from ticket_booking.util.db_conn_util import DBConnUtil
from ticket_booking.exception.custom_exception import CustomException
from datetime import datetime


db_util=DBConnUtil()
conn=db_util.getconn()
class MainModule:
    def __init__(self):
        # Instantiate DAO classes (you may replace these with database DAOs)
        self.venue_dao = InMemoryVenueDAO()
        self.event_dao = InMemoryEventDAO()
        self.customer_dao = InMemoryCustomerDAO()
        self.booking_dao = InMemoryBookingDAO()

    def display_menu(self):
        print("\nTicket Booking System Menu:")
        print("1. Create Event")
        print("2. View Event Details")
        print("3. Update Event Details")
        print("4. Delete Event")
        print("5. View All Events")
        print("6. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.create_event()
            elif choice == '2':
                self.view_event_details()
            elif choice == '3':
                self.update_event_details()
            elif choice == '4':
                self.delete_event()
            elif choice == '5':
                self.view_all_events()
            elif choice == '6':
                print("Exiting the Ticket Booking System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def create_event(self):
        try:
            # You can get user input or use sample data for demonstration
            event_id = input("Enter Event ID: ")
            event_name = input("Enter Event Name: ")
            event_date = datetime.strptime(input("Enter Event Date (YYYY-MM-DD): "), '%Y-%m-%d').date()
            event_time = datetime.strptime(input("Enter Event Time (HH:MM:SS): "), '%H:%M:%S').time()
            venue_id = input("Enter Venue ID: ")
            total_seats = int(input("Enter Total Seats: "))
            available_seats = int(input("Enter Available Seats: "))
            ticket_price = float(input("Enter Ticket Price: "))
            event_type = input("Enter Event Type (Movie/Sports/Concert): ")

            event = Event(event_id, event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type, None)
            self.event_dao.create_event(event)

            print("Event created successfully!")
        except CustomException as e:
            print(f"Error: {e}")

    def view_event_details(self):
        event_id = input("Enter Event ID: ")
        event = self.event_dao.get_event(event_id)

        if event:
            print("\nEvent Details:")
            print(f"Event ID: {event.event_id}")
            print(f"Event Name: {event.event_name}")
            print(f"Event Date: {event.event_date}")
            print(f"Event Time: {event.event_time}")
            print(f"Venue ID: {event.venue_id}")
            print(f"Total Seats: {event.total_seats}")
            print(f"Available Seats: {event.available_seats}")
            print(f"Ticket Price: {event.ticket_price}")
            print(f"Event Type: {event.event_type}")
        else:
            print("Event not found.")

    def update_event_details(self):
        event_id = input("Enter Event ID to update: ")
        event = self.event_dao.get_event(event_id)

        if event:
            # Get updated details from the user or use sample data for demonstration
            event_name = input("Enter Updated Event Name: ")
            event_date = datetime.strptime(input("Enter Updated Event Date (YYYY-MM-DD): "), '%Y-%m-%d').date()
            event_time = datetime.strptime(input("Enter Updated Event Time (HH:MM:SS): "), '%H:%M:%S').time()
            venue_id = input("Enter Updated Venue ID: ")
            total_seats = int(input("Enter Updated Total Seats: "))
            available_seats = int(input("Enter Updated Available Seats: "))
            ticket_price = float(input("Enter Updated Ticket Price: "))
            event_type = input("Enter Updated Event Type (Movie/Sports/Concert): ")

            updated_event = Event(event_id, event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type, None)
            self.event_dao.update_event(event_id, updated_event)

            print("Event details updated successfully!")
        else:
            print("Event not found.")

    def delete_event(self):
        event_id = input("Enter Event ID to delete: ")
        event = self.event_dao.get_event(event_id)

        if event:
            self.event_dao.delete_event(event_id)
            print("Event deleted successfully!")
        else:
            print("Event not found.")

    def view_all_events(self):
        events = self.event_dao.get_all_events()

        if events:
            print("\nAll Events:")
            for event in events:
                print(f"Event ID: {event.event_id}, Event Name: {event.event_name}, Event Type: {event.event_type}")
        else:
            print("No events available.")

if __name__ == "__main__":
    main_module = MainModule()
    main_module.run()
