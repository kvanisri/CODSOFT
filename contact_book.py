contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Contact added successfully!\n")


def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return

    print("\n--- Contact List ---")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}")
    print()


def search_contact():
    key = input("Enter name or phone number to search: ")

    found = False
    for contact in contacts:
        if key.lower() in contact["name"].lower() or key in contact["phone"]:
            print("\nContact Found:")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])
            found = True

    if not found:
        print("Contact not found.\n")


def update_contact():
    phone = input("Enter phone number of contact to update: ")

    for contact in contacts:
        if contact["phone"] == phone:
            print("Leave blank to keep old value")

            new_name = input("New Name: ")
            new_email = input("New Email: ")
            new_address = input("New Address: ")

            if new_name:
                contact["name"] = new_name
            if new_email:
                contact["email"] = new_email
            if new_address:
                contact["address"] = new_address

            print("Contact updated successfully!\n")
            return

    print("Contact not found.\n")


def delete_contact():
    phone = input("Enter phone number of contact to delete: ")

    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return

    print("Contact not found.\n")


def menu():
    while True:
        print("===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


menu()
