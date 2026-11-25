from models.person import Person

class Patient(Person):
    def __init__(self, name, surname, age, phone, patientID, bloodGroup, medicalHistory):
        super().__init__(name, surname, age, phone)
        self.patientID = patientID # public
        self._bloodGroup = bloodGroup # protected 
        self.__medicalHistory = medicalHistory # private

    def showInfo(self):
        pass

    def getMedicalHistory(self):
        pass

    def updateMedicalHistory(self):
        pass