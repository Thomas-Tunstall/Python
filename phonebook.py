from time import sleep
import pickle
import os.path

if os.path.isfile("phonebook.pickle"):
    with open("phonebook.pickle", "rb") as fh:
        Phonebook = pickle.load(fh)        
else:
    Phonebook = {}

def menu():
    print("Booting Phonebook App...")
    sleep(1)
    print("Press 1 to look-up an entry")
    print("Press 2 to set an entry")
    print("Press 3 to delete an entry")
    print("Press 4 to list all entries")
    print("Press 5 to exit phonebook")

user_input = 0

while user_input != "5":
    user_input = (input("Which option would you like? 1-5 "))
    if user_input == "1":
        name_wanted = input("Name ")
        if name_wanted not in Phonebook:
            print("Entry not Found) ")
            menu()
        else: 
            print(f'Found entry for {name_wanted} : {Phonebook[name_wanted]}')
            menu()
    elif user_input == "2": 
        print("Set an entry ")
        sleep(1)
        name = (input("Enter contact's name "))
        phone = (input("Enter a phone number "))
        Phonebook[name] = phone
        print (f'Entry stored for {name}')
        menu()
    elif user_input == "3":
        print("Delete an entry ")
        deleteentry = input("Pick an contact to delete ")
        sleep(1)
        if len(Phonebook.keys()) < 1:
            print("You have no entries to delete! ")
            menu()
        else:
            del Phonebook[deleteentry]
            print("Entry deleted")
        print("Which entry would you like to delete ")
        menu()
    elif user_input == "4":       
        print("List all entries ")
        item_pairs = Phonebook.items()
        for key, value in item_pairs:
            print(f'Found entry for {key} : {value}')
        menu()
    else:
        print("Enter a valid value ")
        menu()        

if user_input == '5':
    with open('phonebook.pickle', 'wb') as fh:
        pickle.dump(Phonebook, fh)
    print("Shutting Down...")
