# -----------------------------------------------------------
# FIND YOUR DOMICILE - Real Estate Management Program
# Demonstrates while loops, for loops, if/else, break, pass,
# getpass, tabulate, and basic file read/write operations
# -----------------------------------------------------------

#import statements
from tabulate import tabulate
import getpass

print("\n=====================================================")
print("        WELCOME TO FIND YOUR DOMICILE.COM")
print("=====================================================")
print("WHERE YOUR HOME BECOMES YOUR HOUSE\n")

# --- DATA ---
dresi = {
    "AD": [
        ['Al Ain','1BHK',750,55000,'free gym',14111],
        ['Saadiyat Island','Studio Flat',480, 70000,'sea view, furnished',14019],
        ['Al Reem Island','3BHK',1200,150000,'parking for 2 vehicles', 14318]],
    "DXB": [
        ['Muhaisnah 4','1BHK',800,   45000,  '1 parking', 413],
        ['Barsha','3BHK',1400,120000, 'gym + free parking for 2 vehicles',432],
        ['Deira', '2BHK',900,60000,  '2 parking spaces', 424]],
    "SHJ": [
        ['Rolla', '3BHK', 900,35000, 'None',19318],
        ['Naif',  '2BHK', 650,25000,'None', 19214]],
    "AJ": [
        ['Al Aseer','5BHK Villa',2000,110000, 'garden + swimming pool', 15011],
        ['Valhalla','2BHK',700, 28000,'1 free parking',15222]],
    "UAQ": [
        ['Industrial-City', '3BHK',850,30000,'None',21119],
        ['Dreamland','2BHK', 600,20000,'swimming pool',21111]],
    "RAK": [
        ['Marina Heights','1BHK',550,22000,'None', 18111],
        ['Al Hamra','2BHK',900,40000,'Swimming pool', 18121]],
    "FJ": [   # Fujairah
        ['Corniche-Beach','1BHK',650,30000,'Sea view',62110],
        ['Airport Road','2BHK',800,45000,'None',68111]]
}

dcomm = {
    "AD": [
        ['Al Wahda','Office',1200, 140000, 'Central AC, underground parking',301],
        ['Corniche','Showroom',1800, 200000, 'Sea view, high football', 302]
    ],
    "DXB": [
        ['Business Bay','Office', 900,130000, 'Furnished, premium floor',401],
        ['Deira', 'Shop',600,80000, 'Main road access, high visibility',402]
    ],
    "SHJ": [
        ['Al Qasimia','Office',700, 60000, 'Parking included',501]
    ],
    "AJ": [
        ['Ajman Corniche', 'Retail Shop', 500,35000, 'Sea front, busy area', 601]
    ],
    "UAQ": [
        ['UAQ Freezone','Warehouse',2000,  90000, 'High ceiling, logistics friendly',701]
    ],
    "RAK": [
        ['RAK Business Bay','Office',800,55000, 'New building, easy access',801]
    ],
    "FJ": [
        ['Fujairah Port Area','Warehouse',2500,120000,'Sea access, cargo friendly',901]
    ]
}

# MAIN MENU

while True:
    print("\n1. User")
    print("2. Admin")
    print("3. Exit")
    option = eval(input("Enter choice: "))

    # ------------------- USER SECTION -------------------
    if option == 1:
        print("\nWelcome User!")
        while True:
            print("\n1. About Us")
            print("2. View Residential Properties")
            print("3. View Commercial Properties")
            print("4. Exit")
            choice = eval(input("Enter your choice: "))

            if choice == 1:
                print("\nAt FindYourDomicile, we connect you with ideal homes and office spaces across the UAE.")
                print("Our listings cover Abu Dhabi, Dubai, and Sharjah.\n")

            elif choice == 2:
                while True:
                    print("\nChoose City:")
                    print("1. Abu Dhabi")
                    print("2. Dubai")
                    print("3. Sharjah")
                    print("4. Go Back")
                    citych = eval(input("Enter choice: "))

                    if citych == 1:
                        temp = dresi["AD"]
                    elif citych == 2:
                        temp = dresi["DXB"]
                    elif citych == 3:
                        temp = dresi["SHJ"]
                    elif citych == 4:
                        break
                    else:
                        print("Invalid input! Try again.")
                        continue

                    print("\nApartment Types:")
                    print("1. Studio Flat")
                    print("2. 1BHK")
                    print("3. 2BHK")
                    print("4. 3BHK")
                    print("5. Show All")
                    print("6. Go Back")

                    apt_choice = eval(input("Enter your choice: "))

                    if apt_choice == 6:
                        break

                    table = [['Area', 'Type', 'Size (sqft)', 'Rent', 'Facilities', 'Code']]

                    for i in temp:
                        if apt_choice == 1 and i[1].upper() == 'STUDIO FLAT':
                            table.append(i)
                        elif apt_choice == 2 and i[1].upper() == '1BHK':
                            table.append(i)
                        elif apt_choice == 3 and i[1].upper() == '2BHK':
                            table.append(i)
                        elif apt_choice == 4 and i[1].upper() == '3BHK':
                            table.append(i)
                        elif apt_choice == 5:
                            table.append(i)

                    if len(table) > 1:
                        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
                        proceed = input("\nWould you like to book one? (yes/no): ")
                        if proceed.lower() == "yes":
                            code = eval(input("Enter code of the property: "))
                            print("Booking successful! Our agent will contact you soon.")
                            with open("bookings.txt", "a") as f:
                                f.write(f"Residential Booking - Code: {code}\n")
                            break
                        else:
                            print("Returning to previous menu...")
                    else:
                        print("No properties found of this type.")

            elif choice == 3:
                while True:
                    print("\nChoose City:")
                    print("1. Abu Dhabi")
                    print("2. Dubai")
                    print("3. Sharjah")
                    print("4. Go Back")
                    citych = eval(input("Enter choice: "))

                    if citych == 1:
                        temp = dcomm["AD"]
                    elif citych == 2:
                        temp = dcomm["DXB"]
                    elif citych == 3:
                        temp = dcomm["SHJ"]
                    elif citych == 4:
                        break
                    else:
                        print("Invalid input! Try again.")
                        continue

                    print(tabulate(temp, headers=['Area', 'Type', 'Size (sqft)', 'Rent', 'Facilities', 'Code'], tablefmt='fancy_grid'))
                    proceed = input("\nWould you like to book one? (yes/no): ")
                    if proceed.lower() == "yes":
                        code = eval(input("Enter code of the property: "))
                        print("Booking successful! Our commercial agent will contact you soon.")
                        with open("bookings.txt", "a") as f:
                            f.write(f"Commercial Booking - Code: {code}\n")
                        break
                    else:
                        print("Returning to previous menu...")

            elif choice == 4:
                print("\nThank you for visiting FindYourDomicile.com!")
                break
            else:
                print("Invalid input! Try again.")

    # ------------------- ADMIN SECTION -------------------
    elif option == 2:
        print("\nWelcome Admin")
        while True:
            print("\n1. Login")
            print("2. Exit")
            adchoice = eval(input("Enter choice: "))

            if adchoice == 1:
                username = input("Enter your username: ")
                password = getpass.getpass("Enter your password: ")

                if password == "11SCB":
                    print("\nLogin successful! Welcome,", username)
                    while True:
                        print("\nAdmin Menu:")
                        print("1. Add Residential Property")
                        print("2. Add Commercial Property")
                        print("3. Remove Property")
                        print("4. View All Listings")
                        print("5. Logout")

                        admch = eval(input("Enter choice: "))

                        if admch == 1:
                            city = input("Enter city code (AD/DXB/SHJ): ").upper()
                            if city in dresi:
                                area = input("Enter area name: ")
                                typ = input("Enter type: ")
                                size = eval(input("Enter size (sqft): "))
                                rent = eval(input("Enter rent: "))
                                facility = input("Enter facilities: ")
                                code = eval(input("Enter unique code: "))
                                dresi[city].append([area, typ, size, rent, facility, code])
                                print("Residential property added successfully.")
                                with open("data.txt", "a") as f:
                                    f.write(f"Residential - {city} - {area} - {typ} - {rent}\n")
                            else:
                                print("Invalid city code.")

                        elif admch == 2:
                            city = input("Enter city code (AD/DXB/SHJ): ").upper()
                            if city in dcomm:
                                area = input("Enter area name: ")
                                typ = input("Enter type (Office/Shop/Showroom): ")
                                size = eval(input("Enter size (sqft): "))
                                rent = eval(input("Enter rent: "))
                                facility = input("Enter facilities: ")
                                code = eval(input("Enter unique code: "))
                                dcomm[city].append([area, typ, size, rent, facility, code])
                                print("Commercial property added successfully.")
                                with open("data.txt", "a") as f:
                                    f.write(f"Commercial - {city} - {area} - {typ} - {rent}\n")
                            else:
                                print("Invalid city code.")

                        elif admch == 3:
                            city = input("Enter city code (AD/DXB/SHJ): ").upper()
                            code = eval(input("Enter property code to remove: "))
                            found = False

                            for dataset in [dresi, dcomm]:
                                if city in dataset:
                                    for i in dataset[city]:
                                        if i[5] == code:
                                            dataset[city].remove(i)
                                            print("Property removed successfully.")
                                            found = True
                                            break
                            if not found:
                                print("No property found with this code.")

                        elif admch == 4:
                            print("\n--- RESIDENTIAL LISTINGS ---")
                            for c in dresi:
                                print("\nCity:", c)
                                print(tabulate(dresi[c], headers=['Area', 'Type', 'Size', 'Rent', 'Facilities', 'Code'], tablefmt='grid'))

                            print("\n--- COMMERCIAL LISTINGS ---")
                            for c in dcomm:
                                print("\nCity:", c)
                                print(tabulate(dcomm[c], headers=['Area', 'Type', 'Size', 'Rent', 'Facilities', 'Code'], tablefmt='grid'))

                        elif admch == 5:
                            print("Logging out...\n")
                            break
                        else:
                            print("Invalid choice.")
                else:
                    print("Incorrect password. Try again.\n")
                    pass

            elif adchoice == 2:
                print("Returning to main menu...\n")
                break
            else:
                print("Invalid input.")

    # ------------------- EXIT PROGRAM -------------------
    elif option == 3:
        print("\nProgram ended. Thank you for using FindYourDomicile.com!")
        break
    else:
        print("\nInvalid option. Try again.")
