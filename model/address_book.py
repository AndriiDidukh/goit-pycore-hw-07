from collections import UserDict
from model.record import Record


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def find(self, name: str) -> Record:
        for k, v in self.data.items():
            if k == name:
                return v

    def add_record(self, record):
        self.data.update({record.name.value: record})

    def delete(self, name: str):
        del self.data[name]

    def show_all(self):
        for record in self.data.values():
            print(str(record))
