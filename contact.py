from file_handler import save_to_file, read_from_file

def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()

    contact = f"{name},{phone},{email}\n"
    save_to_file(contact)
    print("Contact added successfully!\n")

def view_contacts():
    contacts = read_from_file()
    if not contacts:
        print("No contacts found.\n")
        return

    print("\n--- Contact List ---")
    for contact in contacts:
        name, phone, email = contact.strip().split(",")
        print(f"Name: {name}, Phone: {phone}, Email: {email}")
    print()

def search_contact():
    search_name = input("Enter name to search: ").strip().lower()
    contacts = read_from_file()
    found = False

    for contact in contacts:
        name, phone, email = contact.strip().split(",")
        if search_name in name.lower():
            print(f"Found -> Name: {name}, Phone: {phone}, Email: {email}")
            found = True

    if not found:
        print("Contact not found.\n")
