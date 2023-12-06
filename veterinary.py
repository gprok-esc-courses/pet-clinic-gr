import csv
import shutil
import os

def find_appointment_by_id(aid):
    file = open("appointments.csv")
    reader = csv.DictReader(file)
    for row in reader:
        if row['app_id'] == aid:
            return row 
    return None

def view_appointments():
    file = open("appointments.csv")
    reader = csv.DictReader(file)
    for row in reader:
        if row['completed'] == '0':
            print(row['app_id'], row['date'], row['time'], row['reason'])
    file.close()

def add_results():
    aid = input('Give appointment id: ')
    appointment = find_appointment_by_id(aid)
    if appointment is None:
        print("Invalid appointment. Try again")
    else:
        result = input("Give result: ")
        file = open("appointments.csv")
        reader = csv.DictReader(file)
        temp = open("temp_appointments.csv", "w")
        temp.write("app_id,pet_id,date,time,reason,completed,results\n")
        for row in reader:
            if row['app_id'] == aid:
                temp.write(row['app_id']+','+row['pet_id']+','+
                           row['date']+','+row['time']+','+
                           row['reason']+',1,'+result+'\n')
            else:
                temp.write(row['app_id']+','+row['pet_id']+','+
                           row['date']+','+row['time']+','+
                           row['reason']+','+row['completed']+
                           ','+row['results']+'\n')
        temp.close()
        file.close()
        shutil.copyfile("temp_appointments.csv", "appointments.csv")
        os.remove("temp_appointments.csv")


