import re

def validate_phone_number(number):
    """Function to validate phone number"""
    # Regular expression to match a valid phone number
    pattern = re.compile(r"^[6-9]\d{9}$")
    if pattern.match(number):
        return True
    else:
        return False

def validate_email(email):
    """Function to validate email address"""
    # Regular expression to match a valid email address
    pattern = re.compile(r"^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$")
    if pattern.match(email):
        return True
    else:
        return False

def add_contact():
    """Function to add a new contact to the address book"""
    # Take input from the user
    name = input("Enter the name of the contact: ")
    while True:
        number = input("Enter the phone number of the contact: ")
        if validate_phone_number(number):
            break
        else:
            print("Invalid phone number. Please try again.")
    while True:
        email = input("Enter the email address of the contact: ")
        if validate_email(email):
            break
        else:
            print("Invalid email address. Please try again.")
    # Add the contact to the address book
    contacts[name] = {"phone": number, "email": email}
    print("Contact added successfully")

def view_contacts():
    """Function to display all contacts in the address book"""
    if not contacts:
        print("No contacts in the address book")
    else:
        for name, info in contacts.items():
            print("Name:", name)
            print("Phone:", info["phone"])
            print("Email:", info["email"])
            print("")
        
        

def modify_contact():
    """Function to modify contact in the address book"""
    name = input("Enter name of contact to modify: ")
    #check if the contact exists which you want to modify
    if name in contacts:
        print("Current Name: ", name)
        print("Current Phone: ", contacts[name]['phone'])
        print("Current Email: ", contacts[name]['email'])
        #Take input from user to modify contact
        new_name = input("Enter new name (leave blank to keep current value): ")
        new_phone = input("Enter new phone number (leave blank to keep current value): ")
        new_email = input("Enter new email address (leave blank to keep current value): ")
        if new_name != "":
            contacts[new_name] = contacts.pop(name)
            name = new_name
        if new_phone != "":
            contacts[name]['phone'] = new_phone
        if new_email != "":
            contacts[name]['email'] = new_email
        print("Contact updated successfully.")
    else:
        print("Contact not found.")


def search_contact():
    """Function to search for a contact in the address book"""
    # Take input from the user
    name = input("Enter the name of the contact to search for: ")
    # Check if the contact exists
    if name in contacts:
        info = contacts[name]
        print("Name:", name)
        print("Phone:", info["phone"])
        print("Email:", info["email"])
    else:
        print("Contact not found")


def delete_contact():
    """Function to delete a contact from the address book"""
    # Take input from the user
    name = input("Enter the name of the contact to delete: ")
    # Check if the contact exists
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully")
    else:
        print("Contact not found")

# Initialize an empty dictionary to store the contacts
contacts = {}

# Loop to display the menu and take input from the user
while True:
    print("Menu:")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Modify Contacts")
    print("4. Search for a contact")
    print("5. Delete a contact")
    print("6. Exit")
    choice = input("Enter your choice: ")
    # Perform the selected action
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        modify_contact()
    elif choice == "4":
        search_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Thank You for using our system")
        break
    else:
        print("Invalid choice. Please try again.")
