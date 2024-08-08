from model.field import Field


class Phone(Field):
    def __init__(self, value: str):
        if len(str(value)) == 10:
            super().__init__(value)
        else:
            raise ValueError("Wrong phone format")