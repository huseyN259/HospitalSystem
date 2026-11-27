from models.appointment import Appointment

class Hospital:
    def __init__(self, name):
        self.name = name
        self.doctors = []
        self.patients = []
        self.appointments = []

    def addDoctor(self, doctor):
        self.doctors.append(doctor)

    def addPatient(self, patient):
        self.patients.append(patient)

    def showDoctors(self):
        for doctor in self.doctors:
            print(doctor.showInfo())

    def showPatients(self):
        pass

    def createAppointment(self, doctorID, patientID, date):
        pass

    def showAppointments(self):
        pass