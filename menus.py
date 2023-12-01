
def manager_menu():
    print("<< MANAGER MENU >>")
    print("1. Export Pet")
    print("2. Treatments of Day")
    print("3. Add Staff")
    print("4. Remove Staff")
    print("0. Exit")
    choice = input("Choose: ")
    return choice

def secretary_menu():
    print("<< SECRETARY MENU >>")
    print("1. Add Pet")
    print("2. Add Appointment")
    print("0. Exit")
    choice = input("Choose: ")
    return choice

def veterinary_menu():
    print("<< VETERINARY MENU >>")
    print("1. View Appointments")
    print("2. Add Results")
    print("0. Exit")
    choice = input("Choose: ")
    return choice