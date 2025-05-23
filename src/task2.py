from task import AddressBook, Record

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except KeyError as e:
            return str(e)
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.lower()
    return cmd, *args

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact_phone(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        return "Contact not found."
    if old_phone:
        record.remove_phone(old_phone)
    if new_phone:
        record.add_phone(new_phone)
    return message

@input_error
def show_contact_phones(args, book):
    name, *_ = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    return f"Phones: {'; '.join(p.value for p in record.phones)}"

@input_error
def show_all_contacts(args, book):
    return book.list_records()

@input_error
def add_birthday(args, book):
    name, birthday, *_ = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    record.add_birthday(birthday)
    return "Birthday added."

@input_error
def show_birthday(args, book):
    name, *_ = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    return f"Birthday: {record.birthday.value.strftime('%d.%m.%Y')}"

@input_error
def birthdays(args, book):
    upcoming_birthdays = book.get_upcoming_birthdays()
    print(f"Список привітань на цей робочий тиждень:")
    for user in upcoming_birthdays:
        print(f"{user['name']} - {user['congratulation_date'].strftime('%d.%m.%Y')}")
    
def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact_phone(args, book))

        elif command == "phone":
            print(show_contact_phones(args, book))

        elif command == "all":
            print(show_all_contacts(args, book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()