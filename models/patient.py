from models.person import Person

class Patient(Person):
    def __init__(self, name, surname, age, phone, patientID, bloodGroup, medicalHistory):
        super().__init__(name, surname, age, phone)
        self.patientID = patientID # public
        self._bloodGroup = bloodGroup # protected 
        self.__medicalHistory = medicalHistory # private

    def showInfo(self):
        return (
            f"Patient #{self.patientID}: {super().showInfo()} | "
            f"Blood Group: {self._bloodGroup} | "
            f"Medical History: {self.__medicalHistory}"
        )

    def getMedicalHistory(self):
        pass

    def updateMedicalHistory(self):
        pass