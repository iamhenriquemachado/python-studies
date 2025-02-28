import json
import fileinput as fi


# 1. View contacts list
def view_contacts():
    with open('contacts.json', 'r') as contacts:
        data = json.load(contacts)
    print(data)

# 2. Search by name
def search_by_contact_name(contact_name):
    user_search = str(input("Search by name: \n"))
    contact_name = user_search
    with open('contacts.json', 'r') as contacts:
        data = json.load(contacts)
    contact_data = next(
        (item for item in data if item["name"] == contact_name), None
    )
    if contact_data:
        return json.dumps(contact_data)

# 3. Uodate contacts information
def update_contact_by_id():
    # Load JSON file
    with open("contacts.json", "r", encoding="utf-8") as file:
        try:
            data = json.load(file)  # Load JSON data
        except json.JSONDecodeError:
            print("Error: Invalid JSON format")
            exit()

    # ID to update
    target_id = int(input("insert and ID to update\n"))
    updated = False  

    # Update data by ID
    for item in data:
        if isinstance(item, dict) and item.get("id") == target_id:
            item["name"] = str(input("Insert a new name: \n"))
            updated = True  # Mark as updated

    # If ID was not found, print a message
    if not updated:
        print(f"ID {target_id} not found in JSON")
    else:
        # Write back to JSON file only once (outside the loop)
        with open("contacts.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print("Update successful!")

# 4. Delete contact     
def delete_contact_by_id():
    with open('contacts.json', 'r', encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError: 
            print("Error: Invalid JSON format")
            exit()

    target_id = int(input("Insert an ID do delete: "))
    deleted = False

    for item in data:
        if isinstance(item, dict) and item.get("id") == target_id:
            data.remove(item)
            deleted = True
            break
    
    if not deleted:
        print(f"ID {target_id} not found in JSON")
    else:
        with open('contacts.json', 'w', encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print(f"Contact deleted {target_id} from JSON file")
