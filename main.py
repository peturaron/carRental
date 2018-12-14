from ui.CustomerUi import CustomerUi
from ui.CarUi import CarUi
from ui.BookingUi import BookingUi

def main():
        carUi = CarUi()
        carUi.clear()
        print("\n\nWelcome to Nordic Car Rental!\n")
        action = ""
        while (action != "4"):
            print("\nMAIN MENU")
            carUi.lineInHeader()
            print("Please enter the number for following actions:\n")
            mainMenu = "\t{:<30}\n\t{:<30}\n\t{:<30}\n\t{:<30}\n\t".format("1 - Bookings", "2 - Car", "3 - Customers", "4 - Quit")
            print(mainMenu)

            action = input("Choose an option: ")
            
            if action == "1":
                bookingUi = BookingUi()
                bookingUi.mainMenu()
            elif action == "2":
                carUi.mainMenu()
            elif action == "3":
                ui = CustomerUi()
                ui.customerMenu()
            elif action == "4":
                break
            else:
                print("Please enter valid number")
                print()
    
main()