from abc import ABC, abstractmethod
from ticket_booking.entity.model import customer
from ticket_booking.exception.custom_exception import CustomException


class CustomerDAO(ABC):
    @abstractmethod
    def create_customer(self, customer):
        pass

    @abstractmethod
    def get_customer(self, customer_id):
        pass

    @abstractmethod
    def update_customer(self, customer_id, updated_customer):
        pass

    @abstractmethod
    def delete_customer(self, customer_id):
        pass

    @abstractmethod
    def get_all_customers(self):
        pass


class InMemoryCustomerDAO(CustomerDAO):
    # In-memory data to simulate the database
    customers_data = {}

    def create_customer(self, customer):
        if customer.customer_id in self.customers_data:
            raise CustomException("Customer with the same ID already exists")
        self.customers_data[customer.customer_id] = customer

    def get_customer(self, customer_id):
        return self.customers_data.get(customer_id)

    def update_customer(self, customer_id, updated_customer):
        if customer_id not in self.customers_data:
            raise CustomException("Customer not found")
        self.customers_data[customer_id] = updated_customer

    def delete_customer(self, customer_id):
        if customer_id not in self.customers_data:
            raise CustomException("Customer not found")
        del self.customers_data[customer_id]


