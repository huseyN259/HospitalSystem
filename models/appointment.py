class Appointment():
    def __init__(self, appointmentID, doctor, patient, date):
        self.appointmentID = appointmentID
        self.doctor = doctor
        self.patient = patient
        self.date = date

    def showInfo(self):
        return (
            f"Appointment #{self.appointmentID}: {self.date} | "
            f"Doctor: {self.doctor.name} {self.doctor.surname} "
            f"({self.doctor.specialization}) | "
            f"Patient: {self.patient.name} {self.patient.surname}"
        )