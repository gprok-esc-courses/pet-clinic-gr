
from secretary import find_pet_by_id
import csv

def export_pet():
    pid = input("Give pet id: ")
    pet = find_pet_by_id(pid)
    if pet is None:
        print("Pet not found.")
    else:
        file = open("pet"+pid+".txt", "w")
        file.write("Name: " + pet['name'] + '\n')
        file.write("Specie: " + pet['specie'] + '\n')
        file.write("Breed: " + pet['breed'] + '\n')
        file.write("Year: " + pet['year'] + '\n')
        file.write("=================================\n")
        file.write("TREATMENTS\n")
        appointments = open("appointments.csv")
        reader = csv.DictReader(appointments)
        for row in reader:
            if row['pet_id'] == pid and row['completed'] == '1':
                file.write(row['app_id'] + " " + row['date'] + 
                           " " + row['time'] + " Reason:" + 
                           row['reason'] + ", Result:" + 
                           row['results'] + "\n")
        appointments.close()
        file.close()

def day_treatments():
    d = input("Give date (yyyy-mm-dd): ")
    file = open("appointments.csv")
    reader = csv.DictReader(file)
    for row in reader:
        if row['date'] == d:
            # print
            completed = "Completed" if row['completed'] == '1' else "Incomplete"
            print(row['app_id'], row['pet_id'], row['time'],
                  row['reason'], completed, row['results'])
    file.close()

def add_staff():
    pass

def remove_staff():
    pass