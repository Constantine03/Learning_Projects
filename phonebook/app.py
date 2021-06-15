choices = (
            "",
            "All contacts", 
            "Add contact", 
            "Show contact", 
            "Edit contact", 
            "Delete contact", 
            "Exit")
fields = ("name", "mobile", "address")

contacts = [] # or list() with constructor

def welcome():
    prompt = """
        Welcome to the phonebook!
            You have the following options:\n"""
    tip = "Your choice("
    for (index, item) in enumerate(choices):
        if index == 0: continue
        tip += F"{index}," 
        prompt += f"{' '*11} {index}. {item}\n"
    
    return input(prompt + f"{' '*11} {tip[:-1]}): ")

def addContact():
    contact = []
    for item in fields:
        field = input(f'Enter {item}: ')
        contact.append(field)
    return contact

def findContact():
    name = input(f'Enter {fields[0]} for search: ')
    for item in contacts:
        if name in item:
            return item
    return None

def main():
    
    while True:

        choice = welcome()

        choice = int(choice if choice.isdigit() else 0)

        if choice == 0:
            continue
        elif choice == 1: #show all list
            print(contacts)
        elif choice == 2: #add new element into the list
            contacts.append(addContact())
            print(contacts) 
        elif choice == 3: #show element
            res = findContact()
            contact = res if res else 'Not found'
            print(contact) 
        elif choice == 4: #edit element
            print(contacts)
        elif choice == 5: #delete element
            res = findContact()
            index = contacts.index(res)
            del contacts[index]
            print(contacts)
        elif choice == 6: #exit  
            print('Thank You for using our product! Bye!')
            break
        else:
            print('Incorrect choice')
main()
        