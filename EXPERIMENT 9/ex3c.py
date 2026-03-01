class Grandparent:
    def show1(self):
        print("Grandparent")

class Parent(Grandparent):
    def show2(self):
        print("Parent")

class Child(Parent):
    def show3(self):
        print("Child")

obj = Child()
obj.show1()
obj.show2()
obj.show3()