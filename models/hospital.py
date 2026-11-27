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
        for patient in self.patients:
            print(patient.showInfo())

    def createAppointment(self, doctorID, patientID, date):
        doctor = None
        patient = None

        for doctorItem in self.doctors:
            if doctorItem.doctorID == doctorID:
                doctor = doctorItem
                break

        for patientItem in self.patients:
            if patientItem.patientID == patientID:
                patient = patientItem
                break

        if doctor is None:
            print(f"Doctor with ID {doctorID} not found")
            return None

        if patient is None:
            print(f"Patient with ID {patientID} not found")
            return None

        appointmentID = len(self.appointments) + 1
        appointment = Appointment(appointmentID, doctor, patient, date)
        self.appointments.append(appointment)
        return appointment

    def showAppointments(self):
        pass