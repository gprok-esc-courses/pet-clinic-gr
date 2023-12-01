import csv

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

if role == 'manager':
    print("<< MANAGER MENU >>")
elif role == 'secretary':
    print("<< SECRETARY MENU >>")
elif role == 'veterinary':
    print("<< VETERINARY MENU >>")   
else:
    print("Invalid role or user")

