from models.person import Person

class Doctor(Person):
    def __init__(self, name, surname, age, phone, doctorID, specialization, experience):
        super().__init__(name, surname, age, phone)
        self.doctorID = doctorID
        self.specialization = specialization
        self.experience = experience

    def showInfo(self):
        pass