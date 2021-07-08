import csv
from os import path
import os
import shutil
TMP_FILE = 'phonebook/tmpPhoneBook.csv'
DB = 'phonebook/phonebook.csv'
HEADERS = ('Name', 'Number', 'Address')
CHOICES = ( 
            "Help",
            "All contacts", 
            "Add contact", 
            "Show contact", 
            "Edit contact", 
            "Delete contact", 
            "Exit")

def init_db(): #if we don't have DB in place, create new
    if not path.exists(DB):
        with open(DB, 'w', newline='') as pb:
            writer = csv.DictWriter(pb, fieldnames=HEADERS)
            writer.writeheader()

def welcome_msg(): #welcome and help message
    prompt = """
        Welcome to the phonebook!\n
            You have the following options:\n"""
    for (index, item) in enumerate(CHOICES):
        prompt += f"{' '*11} {index}. {item}\n"
    
    print(prompt)
    
def next_choice(): #choose an option
    tip = "Your choice ("
    for i in range(len(CHOICES)):
        tip += f"{i},"
    choice = input(f"{' '*11} {tip[:-1]}): ")
    return int(choice if choice.isdigit() else -1) #Convert choice input into a number

def finish_job(): #type a farewell message
    print(f"{' '*11} Thank You for using our product! Bye!")

def show_all_contacts():
    with open(DB, 'r', newline='') as pb:
        reader = csv.DictReader(pb)
        print(f"{reader.fieldnames[0]} {' '*12} {reader.fieldnames[1]} {' '*12} {reader.fieldnames[2]}")
        for row in reader:
            print(f"{row[reader.fieldnames[0]]} {' '*7} {row[reader.fieldnames[1]]} {' '*12} {row[reader.fieldnames[2]]}")

def get_name(suffix=""): #input a name
    return input(f"Provide a person's {suffix}name: ")

def get_number(suffix=""): #input a number
    return input(f"Provide a person's {suffix}number: ")

def get_address(suffix=""): #input a address
    return input(f"Provide a person's {suffix}address: ")

def add_contact():
    name = get_name()
    name_new = True
    with open(DB, 'r', newline='') as pb: #check if user exists
        reader = csv.DictReader(pb)
        for row in reader:
            if row[reader.fieldnames[0]] == name:
                print(f"Person {name} is already present in the phonebook\n")
                name_new = False
                break
    if name_new: #if person is new, add it
        number = get_number()
        address = get_address()
        with open(DB, "a", newline='') as pb:
            person = {HEADERS[0]:name, HEADERS[1]:number, HEADERS[2]:address}
            writer = csv.DictWriter(pb, fieldnames=HEADERS) 
            writer.writerow(person)
        print(f"Person {name} added\n")

def show_contact():
    name = get_name()
    not_found = True
    with open(DB, 'r', newline='') as pb:
        reader = csv.DictReader(pb)
        for row in reader:
            if row[reader.fieldnames[0]] == name:
                not_found = False
                print(f"{reader.fieldnames[0]} {' '*12} {reader.fieldnames[1]} {' '*12} {reader.fieldnames[2]}")
                print(f"{row[reader.fieldnames[0]]} {' '*7} {row[reader.fieldnames[1]]} {' '*12} {row[reader.fieldnames[2]]}\n")
                break
    if not_found:
        print(f"Person {name} was not found in the phonebook\n")

def edit_contact():
    name = get_name()
    not_found = True
    with open(TMP_FILE, 'w', newline='') as tempfile:
        writer = csv.DictWriter(tempfile, fieldnames=HEADERS)
        writer.writeheader()
        with open(DB, 'r', newline='') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                if row[HEADERS[0]] == name:
                    not_found = False
                    edited_contact = {}
                    print("Please, provide the following information (empty row to skip editing): ")
                    edited_contact[HEADERS[0]] = get_name("new ")
                    edited_contact[HEADERS[1]] = get_number("new ")
                    edited_contact[HEADERS[2]] = get_address("new ")
                    for i in range(3):
                        if edited_contact[HEADERS[i]] == "":
                            edited_contact[HEADERS[i]] = row[HEADERS[i]]
                    writer.writerow(edited_contact)
                    
                else:
                    writer.writerow(row)
    if not_found:
        print("User's not found.")
        os.remove(TMP_FILE)
    else:
        print("Contact was edited")
        shutil.move(TMP_FILE, DB)

def delete_contact():
    name = get_name()
    not_found = True
    with open(TMP_FILE, 'w', newline='') as tempfile:
        writer = csv.DictWriter(tempfile, fieldnames=HEADERS)
        writer.writeheader()
        with open(DB, 'r', newline='') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                if row[HEADERS[0]] == name:
                    not_found = False
                else:
                    writer.writerow(row)
    if not_found:
        print("User's not found.")
        os.remove(TMP_FILE)
    else:
        print("Contact was deleted")
        shutil.move(TMP_FILE, DB)






def main():
    init_db()
    welcome_msg()
    
    while True:

        choice = next_choice()
            
        if choice == 0:
            welcome_msg()
        elif choice == 1: #show all list
            show_all_contacts()
            
        elif choice == 2: #add new element into the list
            add_contact() 
            
        elif choice == 3: #show element
            show_contact() 
            
        elif choice == 4: #edit element
            edit_contact()
            
        elif choice == 5: #delete element
            delete_contact()
            
        elif choice == 6: #exit  
            finish_job()
            break
        else:
            print('Incorrect choice')
            continue
if __name__ == '__main__':
    main()