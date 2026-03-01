class Student:
    def __init__(self, name, sapid, phy, chem, maths):
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

    def find_marks_percentage(self):
        total = self.phy + self.chem + self.maths
        return total / 3

    def display_result(self):
        if self.phy > 40 and self.chem > 40 and self.maths > 40:
            print("Result: Pass")
        else:
            print("Result: Fail")

def class_average(students):
    total = 0
    for s in students:
        total += s.find_marks_percentage()
    return total / len(students)

n = int(input("Enter number of students: "))
students = []

for i in range(n):
    name = input("Enter name: ")
    sapid = input("Enter SAP ID: ")
    phy = int(input("Enter Physics marks: "))
    chem = int(input("Enter Chemistry marks: "))
    maths = int(input("Enter Maths marks: "))
    students.append(Student(name, sapid, phy, chem, maths))

for s in students:
    s.display()
    print("Percentage:", s.find_marks_percentage())
    s.display_result()
    print()

print("Class Average:", class_average(students))