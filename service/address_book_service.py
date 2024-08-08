from model.record import Record
from model.address_book import AddressBook
from datetime import datetime, timedelta


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Enter the argument for the command"
        except ValueError:
            return "Enter the argument for the command"
        except KeyError:
            return "No such contact"

    return inner


class AddressBookService:

    def __init__(self):
        pass

    @staticmethod
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
            try:
                record.add_phone(phone)
            except ValueError:
                return "Wrong phone format"
        return message

    @staticmethod
    @input_error
    def change_contact_number(args, book: AddressBook):
        name, old_phone, new_phone, *_ = args
        record = book.find(name)
        if not record:
            return "No contact for such name"
        return record.edit_phone(old_phone, new_phone)

    @staticmethod
    @input_error
    def get_phones_for_contact(args, book: AddressBook):
        name, *_ = args
        record = book.find(name)
        if not record:
            return "No contact for such name"
        phones = ""
        for phone in record.phones:
            phones = phones + " " + phone.value
        return phones

    @staticmethod
    @input_error
    def add_birthday_to_contact(args, book: AddressBook):
        name, date_of_birth, *_ = args
        record = book.find(name)
        if not record:
            return "No contact for such name"
        try:
            datetime.strptime(date_of_birth, "%d.%m.%Y")
            record.add_birthday(date_of_birth)
            return "Date of birth added"
        except ValueError:
            return "Wrong data format"

    @staticmethod
    @input_error
    def get_birthday_for_contact(args, book: AddressBook):
        name, *_ = args
        record = book.find(name)
        if not record:
            return "No contact for such name"
        return record.birthday

    @staticmethod
    @input_error
    def get_birthdays_for_next_week(book: AddressBook):

        today = datetime.today().date()
        upcoming_birthdays = []
        end_date = today + timedelta(days=7)

        for record in book.data.values():
            name = record.name.value
            birthday_str = record.birthday
            birthday = datetime.strptime(birthday_str, '%d.%m.%Y').date()

            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday.replace(year=today.year + 1)

            if today <= birthday_this_year <= end_date:
                if birthday_this_year.weekday() in (5, 6):
                    birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

                upcoming_birthdays.append({
                    'name': name,
                    'congratulation_date': birthday_this_year.strftime('%d.%m.%Y')
                })

        return upcoming_birthdays
