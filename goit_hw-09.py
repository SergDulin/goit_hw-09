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
    while True:
        command = input("Enter a command: ").lower().split()
        if command[0] == "hello":
            print("How can I help you?")
        elif command[0] == "add":
            if len(command) >= 3:
                name = " ".join(command[1:-1])
                phone = command[-1]
                print(add_contact(name, phone))
            else:
                print("Invalid input. Please provide both name and phone number.")
        elif command[0] == "change":
            if len(command) >= 3:
                name = " ".join(command[1:-1])
                phone = command[-1]
                print(change_phone(name, phone))
            else:
                print("Invalid input. Please provide both name and phone number.")
        elif command[0] == "phone":
            if len(command) >= 2:
                name = " ".join(command[1:])
                print(get_phone(name))
            else:
                print("Invalid input. Please provide a name.")
        elif command[0] == "show":
            if len(command) >= 2 and command[1] == "all":
                print(show_all_contacts())
            else:
                print("Invalid input. Please provide a valid command.")
        elif command[0] in ["good", "bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")    

if __name__ == "__main__":
    main()