Contacts = [
    {
        "name": "Toria Sow",
        "phone": "025 780 6345",
        "email": "toriaso@gmail.com",
        "role": "Project Manager"
    },
    {
        "name": "Arnold Heather",
        "phone": "022 790 6145",
        "email": "arnoldhe@hotmail.com",
        "role": "Developer"
    },
    {
        "name": "Jessie May",
        "phone": "022 790 6145",
        "email": "Jessiem@email.com",
        "role": "Designer"
    }
]
#List all contacts
def list_contacts(contact_list):
    print("")
    print("=" * 35)
    print("   CONTACT BOOK")
    print("=" * 35)

    if len(contact_list)== 0:
        print("No contacts yet! You're lonely!")
    else: 
        for i, contact in enumerate (contact_list):
            print (f"{i + 1}. {contact ['name']} - {contact ['role']}")
    print (f" Total Contacts: {len (contact_list)}")
    print("=" * 35)

def add_contact (contact_list, name, phone, email, role):
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "role": role
    }
    contact_list.append(new_contact)
    print(f"\n ✔️ contact added: {name}")

def find_contact(contact_list,search_name):
    print (f"\n Searching for: {search_name}")
    print("-" * 35)

    for contact in contact_list:
        if search_name.lower() in contact ["name"].lower():
            print (f" ✔️ Found! Yay! ")
            print(f" Name: {contact['name']}")
            print(f" Phone: {contact['phone']}")
            print(f" Email: {contact['email']}")
            print(f" Role: {contact['role']}")
            return
    print(f" x No contact found for: {search_name} ")

def delete_contact (contact_list, name):
    for contact in contact_list:
        if name.lower() == contact["name"].lower():
            contact_list.remove(contact)
            print(f"\n ✔️ Contact deleted: {name}")
            return
    print(f"\n x Contact not found: {name}")

list_contacts(Contacts)
add_contact(Contacts, "Joy Yao", "050 004 232", "joyy@email.com", "Engineer")
list_contacts(Contacts)
find_contact(Contacts, "Toria")
find_contact(Contacts, "Arnold")
find_contact(Contacts, "Jessie")
find_contact(Contacts, "John")
delete_contact(Contacts, "Arnold Heather")
list_contacts (Contacts)

def update_contact (contact_list, name, new_phone):
    for contact in contact_list:
        if name.lower() == contact ["name"].lower():
            old_phone = contact["phone"]
            contact["phone"] = new_phone
            print(f"\n Updated {name}'s phone")
            print(f" Old: {old_phone}")
            print(f" New: {new_phone}")
            return
    print(f"\n x Contact not found: {name}")

update_contact(Contacts, "Toria Sow", "0258705343")
find_contact(Contacts, "Toria")