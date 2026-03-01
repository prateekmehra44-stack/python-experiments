class Student:
    def set_data(self, name, sapid, phy, chem, maths):
        self.name = name
        self.sapid = sapid
        self.phy = phy
        self.chem = chem
        self.maths = maths

    def display(self):
        print("Name:", self.name)
        print("SAP ID:", self.sapid)
        print("Physics:", self.phy)
        print("Chemistry:", self.chem)
        print("Maths:", self.maths)
        print()

students = []

for i in range(3):
    name = input("Enter name: ")
    sapid = input("Enter SAP ID: ")
    phy = int(input("Enter Physics marks: "))
    chem = int(input("Enter Chemistry marks: "))
    maths = int(input("Enter Maths marks: "))
    
    s = Student()
    s.set_data(name, sapid, phy, chem, maths)
    students.append(s)

for s in students:
    s.display()