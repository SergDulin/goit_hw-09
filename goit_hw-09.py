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
    

@input_error
def change_phone(name, phone):
    
@input_error
def get_phone(name):
   

def show_all_contacts():
    

def main():
    

if __name__ == "__main__":
    main()