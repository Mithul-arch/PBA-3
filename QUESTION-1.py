
class Resident:
    def __init__(self, name, flat_no, fee, status):
        self.name = name
        self.flat_no = flat_no
        self.fee = fee
        self.status = status

    def display_details(self):
        print("Resident Name:", self.name)
        print("Flat Number:", self.flat_no)
        print("Maintenance Fee:", self.fee)
        print("Payment Status:", self.status)
        print("------------------------")


class Society:
    def __init__(self):
        self.residents = []

    def add_resident(self, resident):
        self.residents.append(resident)
        print("Resident record added successfully!")

    def display_all(self):
        print("\nAPARTMENT MAINTENANCE RECORDS")
        print("============================")
        for resident in self.residents:
            resident.display_details()

society = Society()

r1 = Resident("Mithul Krishna", 101, 2500, "Paid")
r2 = Resident("Rahul", 102, 2500, "Pending")
r3 = Resident("Amit", 103, 2500, "Paid")

society.add_resident(r1)
society.add_resident(r2)
society.add_resident(r3)

society.display_all()
