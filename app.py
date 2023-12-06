import csv
from menus import manager_menu, secretary_menu, veterinary_menu
from secretary import add_pet, add_appointment
from veterinary import view_appointments, add_results
from manager import *

def find_user_role(username, password):
    """
    Checks if username and password exist in the users.csv file.
    Also, if the account is active.
    If yes, returns the role of the user, otherwise None.
    """
    file = open("users.csv")
    reader = csv.DictReader(file)
    for row in reader:
        if row['username'] == username \
            and row['password'] == password and row['active'] == '1':
            return row['role']
    return None



username = input("Give username: ")
password = input("Give password: ")

role = find_user_role(username, password)

choice = '0'
while True:
    if role == 'manager':
        choice = manager_menu()
        if choice == '1':
            export_pet()
        elif choice == '2':
            day_treatments()
        elif choice == '3':
            add_staff()
        elif choice == '4':
            remove_staff()
    elif role == 'secretary':
        choice = secretary_menu()
        if choice == '1':
            add_pet()
        elif choice == '2':
            add_appointment()
    elif role == 'veterinary':
        choice = veterinary_menu() 
        if choice == '1':
            view_appointments()
        elif choice == '2':
            add_results()
    else:
        print("Invalid role or user")
    if choice == '0':
        break

