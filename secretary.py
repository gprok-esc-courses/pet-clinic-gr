import csv

def get_next_pet_id():
    file = open("pets.csv")
    reader = csv.DictReader(file)
    pet_list = list(reader)
    id = len(pet_list) + 1
    file.close()
    return id

def get_next_appointment_id():
    file = open("appointments.csv")
    reader = csv.DictReader(file)
    app_list = list(reader)
    id = len(app_list) + 1
    file.close()
    return id

def find_pet_by_id(pid):
    file = open("pets.csv")
    reader = csv.DictReader(file)
    for row in reader:
        if row['id'] == pid:
            return row 
    return None

def add_pet():
    name = input("Pet name: ")
    species = input("Specie: ")
    breed = input("Breed: ")
    year = input("Year of birth: ")
    id = get_next_pet_id()
    file = open("pets.csv", "a")
    file.write(str(id) + ',' + name + ',' + species + 
               ',' + breed + ',' + year + '\n')
    file.close()

def add_appointment():
    id = input("Give pet id: ")
    pet = find_pet_by_id(id)
    if pet is None:
        print("Invalid id. Try again.")
    else:
        aid = get_next_appointment_id()
        app_date = input("Give date (yyyy-mm-dd): ")
        app_time = input("Give time (hh:mm): ")
        reason = input("Give appointment reason: ")
        file = open("appointments.csv", "a")
        file.write(str(aid) + ',' + id + ',' + app_date + ',' + app_time + ',' + 
                   reason + ',0,-\n')  # last 0 means incomplete
        file.close()



if __name__ == '__main__':
    add_appointment()
