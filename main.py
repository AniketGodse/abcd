import json

def load_data():
    try:
        with open('data_file.json', 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    return data

def save_data(data):
    with open('data_file.json', 'w') as f:
        json.dump(data, f, indent=2)

def add_entry(data):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    entry_id = len(data) + 1
    data[entry_id] = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }

    save_data(data)
    print(f"Entry {name} added successfully!\n")

def display_entries(data):
    if not data:
        print("No entries found.")
        return

    print("======= Entries =======")
    for entry_id, entry_info in data.items():
        print(f"{entry_id}. {entry_info['name']} - {entry_info['phone']}")
    print("=======================\n")

def search_entry(data):
    query = input("Enter name or phone number to search: ")
    results = []

    for entry_id, entry_info in data.items():
        if query.lower() in entry_info['name'].lower() or query in entry_info['phone']:
            results.append((entry_id, entry_info))

    if not results:
        print("No matching entries found.\n")
    else:
        print("======= Search Results =======")
        for entry_id, entry_info in results:
            print(f"{entry_id}. {entry_info['name']} - {entry_info['phone']}")
        print("==============================\n")

def update_entry(data):
    display_entries(data)
    entry_id = input("Enter the ID of the entry to update: ")

    if entry_id in data:
        print("Update entry details:")
        data[entry_id]['name'] = input("Name: ")
        data[entry_id]['phone'] = input("Phone: ")
        data[entry_id]['email'] = input("Email: ")
        data[entry_id]['address'] = input("Address: ")
        save_data(data)
        print("Entry updated successfully!\n")
    else:
        print("Invalid entry ID. Please try again.\n")

def delete_entry(data):
    display_entries(data)
    entry_id = input("Enter the ID of the entry to delete: ")

    if entry_id in data:
        del data[entry_id]
        save_data(data)
        print("Entry deleted successfully!\n")
    else:
        print("Invalid entry ID. Please try again.\n")

def main_menu():
    data = load_data()

    while True:
        print("====== Entry Manager ======")
        print("1. Add Entry")
        print("2. Display Entries")
        print("3. Search Entry")
        print("4. Update Entry")
        print("5. Delete Entry")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_entry(data)
        elif choice == '2':
            display_entries(data)
        elif choice == '3':
            search_entry(data)
        elif choice == '4':
            update_entry(data)
        elif choice == '5':
            delete_entry(data)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
