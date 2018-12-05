from models.Customer import Customer

class CustomerRepository:

    def __init__(self):
        self.__customers = []

    def add_customer(self, customer):
        # first add to file then to private list
        with open("./data/customers.txt", "a+") as customers_file:
            email = customer.get_email()
            name = customer.get_name()
            dateOfBirth = customer.get_dateOfBirth()
            gender = customer.get_gender()
            dateOfReg = customer.get_dateOfReg()
            payMethod = customer.get_payMethod()
            customers_file.write("{},{},{},{},{},{}\n".format(email, name, dateOfBirth, gender, dateOfReg, payMethod))

    def get_customers(self):
        if self.__customers == []:
            with open("./data/customers.txt", "r") as customer_file:
                for line in customer_file.readlines():
                    email, name, dateOfBirth, gender, dateOfReg, payMethod = line.split(",")
                    new_customer = Customer(email, name, dateOfBirth, gender, dateOfReg, payMethod)
                    self.__customers.append(new_customer)

        return self.__customers
