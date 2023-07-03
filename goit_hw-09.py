def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input. Please provide both name and phone number."
        except IndexError:
            return "Invalid input. Please provide both name and phone number."
    return inner

contacts = {}

@input_error
def add_contact(name, phone):
    contacts[name.lower()] = phone
    return "Contact added successfully."

@input_error
def change_phone(name, phone):
    matching_contacts = [contact_name for contact_name in contacts.keys() if contact_name.lower() == name.lower()]
    if matching_contacts:
        contacts[matching_contacts[0]] = phone
        return "Phone number updated successfully."
    else:
        return "Contact not found."

@input_error
def get_phone(name):
    matching_contacts = [f"The phone number for {contact_name.title()} is {phone}" for contact_name, phone in contacts.items() if name.lower() in contact_name.lower()]
    if matching_contacts:
        return "\n".join(matching_contacts)
    else:
        return "No contacts found with that name."

def show_all_contacts():
    if contacts:
        all_contacts = "\n".join([f"{name.title()}: {phone}" for name, phone in contacts.items()])
        return all_contacts
    else:
        return "No contacts found."
    

def main():
    

if __name__ == "__main__":
    main()