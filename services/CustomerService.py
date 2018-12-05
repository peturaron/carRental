from repositories.CustomerRepository import CustomerRepository

class CustomerService:
    def __init__(self):
        self.__customer_repo = CustomerRepository()

    def add_customer(self, customer):
        if self.is_valid_customer(customer):
            self.__customer_repo.add_customer(customer)

    def is_valid_customer(self, customer):
        #here should be some code to
        #validate the customer
        return True

    def get_customers(self):
        return self.__customer_repo.get_customers()

    def get_customers_by_genre(self, name):
        pass
