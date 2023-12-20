from abc import ABC, abstractmethod
from datetime import datetime
from ticket_booking.entity.model import event
from ticket_booking.exception.custom_exception import CustomException

class EventDAO(ABC):
    @abstractmethod
    def create_event(self, event):
        pass

    @abstractmethod
    def get_event(self, event_id):
        pass

    @abstractmethod
    def update_event(self, event_id, updated_event):
        pass

    @abstractmethod
    def delete_event(self, event_id):
        pass

    @abstractmethod
    def get_all_events(self):
        pass

class InMemoryEventDAO(EventDAO):
    # In-memory data to simulate the database
    events_data = {}

    def create_event(self, event):
        if event.event_id in self.events_data:
            raise CustomException("Event with the same ID already exists")
        self.events_data[event.event_id] = event

    def get_event(self, event_id):
        return self.events_data.get(event_id)

    def update_event(self, event_id, updated_event):
        if event_id not in self.events_data:
            raise CustomException("Event not found")
        self.events_data[event_id] = updated_event

    def delete_event(self, event_id):
        if event_id not in self.events_data:
            raise CustomException("Event not found")
        del self.events_data[event_id]

    def get_all_events(self):
        return list(self.events_data.values())
