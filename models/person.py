class Person:
    def __init__(self, name, surname, age, phone):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone

    def showInfo(self):
        return f"{self.name} {self.surname}, Age: {self.age}, Phone: {self.phone}"