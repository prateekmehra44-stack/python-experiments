class Parent:
    def show(self):
        print("Parent Class")

class Child(Parent):
    def display(self):
        print("Child Class")

c = Child()
c.show()
c.display()