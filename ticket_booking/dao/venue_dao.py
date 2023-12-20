from abc import ABC, abstractmethod
from ticket_booking.entity.model import Venue
from ticket_booking.exception.custom_exception import CustomException

class VenueDAO(ABC):
    @abstractmethod
    def create_venue(self, venue):
        pass

    @abstractmethod
    def get_venue(self, venue_id):
        pass

    @abstractmethod
    def update_venue(self, venue_id, updated_venue):
        pass

    @abstractmethod
    def delete_venue(self, venue_id):
        pass

    @abstractmethod
    def get_all_venues(self):
        pass

class InMemoryVenueDAO(VenueDAO):
    # In-memory data to simulate the database
    venues_data = {}

    def create_venue(self, venue):
        if venue.venue_id in self.venues_data:
            raise CustomException("Venue with the same ID already exists")
        self.venues_data[venue.venue_id] = venue

    def get_venue(self, venue_id):
        return self.venues_data.get(venue_id)

    def update_venue(self, venue_id, updated_venue):
        if venue_id not in self.venues_data:
            raise CustomException("Venue not found")
        self.venues_data[venue_id] = updated_venue

    def delete_venue(self, venue_id):
        if venue_id not in self.venues_data:
            raise CustomException("Venue not found")
        del self.venues_data[venue_id]

    def get_all_venues(self):
        return list(self.venues_data.values())
