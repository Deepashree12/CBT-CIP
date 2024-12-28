contacts = []

# a function to add contacts
def add_contact():
    name = input('Enter Name: ').lower()
    number = int(input('Enter Phone Number (without Country Code): '))
    contacts.append({'Name': name, 'Phone Number': number})
    print('Contact successfully added!')

# a function to delete the required contact
def delete_contact():
    name = input('Enter the contact you would like to DELETE: ').lower()
    for contact in contacts:
        if contact['Name'].lower() == name.lower():
            contacts.remove(contact)
            print('Contact successfully deleted!')
            return
    print('Contact not found!')

# a function to search for a contact
def search_contact():
    name = input('Enter the contact you would like to SEARCH:').lower()
    for contact in contacts:
        if contact['Name'] == name:
            print(f'\nContact Found : {contact['Name']} - {contact['Phone Number']}')
            return 
            
    print('Contact not Found!')

# a function to display all the contacts
def display_contacts():
    print('\nContact List:')
    print('Name \t Phone Number')
    for contact in contacts:
        print(f'{contact['Name']} \t {contact['Phone Number']}')

# NOTE to select the choices 
def contact_manager():
    print('\nSimple Contact Manager')
    print('Below are the choices you should select \n')
    print('1. Add Contact')
    print('2. Delete Contact')
    print('3. Search Contact')
    print('4. Display Contacts')
    print('5. Exit')
        
contact_manager()

# enter a choice to perform contact manager
while True:
    choice = input('\nEnter your choice --> ')
    
    if choice == "1":
        add_contact()

    elif choice == "2":
        delete_contact()

    elif choice == "3":
        search_contact()
        
    elif choice == "4":
        display_contacts()

    elif choice == "5":
        print('You are exited from the Contact Manager')
        break

    else:
        print('Invalid Input! Enter the choice again')    