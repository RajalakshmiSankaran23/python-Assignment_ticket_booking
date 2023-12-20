from abc import ABC, abstractmethod
from ticket_booking.entity.model import Booking
from ticket_booking.exception.custom_exception import CustomException

class BookingDAO(ABC):
    @abstractmethod
    def create_booking(self, booking):
        pass

    @abstractmethod
    def get_booking(self, booking_id):
        pass

    @abstractmethod
    def update_booking(self, booking_id, updated_booking):
        pass

    @abstractmethod
    def delete_booking(self, booking_id):
        pass

    @abstractmethod
    def get_all_bookings(self):
        pass

class InMemoryBookingDAO(BookingDAO):
    # In-memory data to simulate the database
    bookings_data = {}

    def create_booking(self, booking):
        if booking.booking_id in self.bookings_data:
            raise CustomException("Booking with the same ID already exists")
        self.bookings_data[booking.booking_id] = booking

    def get_booking(self, booking_id):
        return self.bookings_data.get(booking_id)

    def update_booking(self, booking_id, updated_booking):
        if booking_id not in self.bookings_data:
            raise CustomException("Booking not found")
        self.bookings_data[booking_id] = updated_booking

    def delete_booking(self, booking_id):
        if booking_id not in self.bookings_data:
            raise CustomException("Booking not found")
        del self.bookings_data[booking_id]

    def get_all_bookings(self):
        return list(self.bookings_data.values())
