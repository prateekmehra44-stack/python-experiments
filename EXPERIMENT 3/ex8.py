name = input("Enter Name: ")
roll = input("Enter Roll Number: ")
sapid = input("Enter SAPID: ")
sem = input("Enter Semester: ")
course = input("Enter Course: ")

pds = int(input("Enter PDS marks: "))
python = int(input("Enter Python marks: "))
chem = int(input("Enter Chemistry marks: "))
eng = int(input("Enter English marks: "))
phy = int(input("Enter Physics marks: "))

total = pds + python + chem + eng + phy
percentage = total / 5
cgpa = percentage / 10

if cgpa >= 0 and cgpa <= 3.4:
    grade = "F"
elif cgpa <= 5.0:
    grade = "C+"
elif cgpa <= 6.0:
    grade = "B"
elif cgpa <= 7.0:
    grade = "B+"
elif cgpa <= 8.0:
    grade = "A"
elif cgpa <= 9.0:
    grade = "A+"
else:
    grade = "O"

print("\nSample Gradesheet")
print("Name:", name)
print("Roll Number:", roll, "SAPID:", sapid)
print("Sem:", sem, "Course:", course)
print("Subject name: Marks")
print("PDS:", pds)
print("Python:", python)
print("Chemistry:", chem)
print("English:", eng)
print("Physics:", phy)
print("Percentage:", percentage, "%")
print("CGPA:", cgpa)
print("Grade:", grade)