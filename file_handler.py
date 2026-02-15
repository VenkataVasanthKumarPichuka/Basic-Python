FILE_NAME = "contacts.txt"

def save_to_file(contact):
    with open(FILE_NAME, "a") as file:
        file.write(contact)

def read_from_file():
    try:
        with open(FILE_NAME, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []
