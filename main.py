from ui.SalesmanUi import SalesmanUi

def main():
        print("Welcome to Nordic Car Rental! \nPlease enter the number for following actions:\n")
        action = ""
        while (action != "4"):
            print()
            print("1. Bookings")
            print("2. Car")
            print("3. Customers")
            print("4. Quit")

            action = input("Choose an option: ")
            
            if action == "1":
                pass
            elif action == "2":
                pass
            elif action == "3":
                ui = SalesmanUi()
                ui.main_menu()
            elif action == "4":
                break
            else:
                print("Please enter valid number")
                print()
    
main()
