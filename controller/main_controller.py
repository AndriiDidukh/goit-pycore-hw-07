from model.address_book import AddressBook
from service.address_book_service import AddressBookService


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


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
            print(AddressBookService.add_contact(args, book))

        elif command == "change":
            print(AddressBookService.change_contact_number(args, book))

        elif command == "phone":
            print(AddressBookService.get_phones_for_contact(args, book))

        elif command == "all":
            book.show_all()

        elif command == "add-birthday":
            print(AddressBookService.add_birthday_to_contact(args, book))

        elif command == "show-birthday":
            print(AddressBookService.get_birthday_for_contact(args, book))

        elif command == "birthdays":
            print(AddressBookService.get_birthdays_for_next_week(book))

        else:
            print("Invalid command.")


main()
