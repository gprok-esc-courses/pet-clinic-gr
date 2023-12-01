import csv

def add_pet():
    name = input("Pet name: ")
    species = input("Specie: ")
    breed = input("Breed: ")
    year = input("Year of birth: ")
    file = open("pets.csv")
    reader = csv.DictReader(file)
    pet_list = list(reader)
    id = len(pet_list) + 1
    file.close()
    file = open("pets.csv", "a")
    file.write(str(id) + ',' + name + ',' + species + 
               ',' + breed + ',' + year + '\n')
    file.close()

