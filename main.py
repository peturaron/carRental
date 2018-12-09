from ui.SalesmanUi import SalesmanUi
from ui.CarUi import CarUi

def main():
        print("\n\nWelcome to Nordic Car Rental! \nPlease enter the number for following actions:\n")
        action = ""
        while (action != "4"):
            print("\nMAIN MENU")
            print("_"*40,"\n")
            mainMenu = "\t{:<30}\n\t{:<30}\n\t{:<30}\n\t{:<30}\n\t".format("1 - Bookings", "2 - Car", "3 - Customers", "4 - Quit")
            print(mainMenu)

            action = input("Choose an option: ")
            
            if action == "1":
                pass
            elif action == "2":
                carUi = CarUi()
                carUi.mainMenu()
            elif action == "3":
                ui = SalesmanUi()
                ui.main_menu()
            elif action == "4":
                break
            else:
                print("Please enter valid number")
                print()
    
main()
