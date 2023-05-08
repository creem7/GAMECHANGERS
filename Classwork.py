class Mathematics():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def sub(self):
        return self.a - self.b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
obj = Mathematics(a, b)
choice = 1
while choice != 0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Result: ", obj.add())
    elif choice == 2:
        print("Result: ", obj.sub())
    elif choice == 3:
        print("Result: ", obj.mul())
    elif choice == 4:
        print("Result: ", round(obj.div(), 2))
    elif choice == 0:
        print("Exiting!")
    else:
        print("Invalid choice!!")

print()


class Physics():
    def __int__(self, m, g, h, t, k):
        self.m = m
        self.g = g
        self.h = h
        self.t = t
        self.k = k

    def mul(self):
        return self.m * self.g

    def mul2(self):
        return self.m * self.g * self.h

    def div(self):
        return self.m * self.g * self.h / self.t

    def equal(self):
        return self.k == self.m * self.g * self.h / self.t


m = int(input("Enter the mass: "))
g = int(input("Enter the gravity: "))
h = int(input("Enter the height: "))
t = int(input("Enter the time: "))
k = int(input("Enter the force constant: "))
obj = Physics(m, g, h, t, k)
choice = 1
while choice != 0:
    print("0. Exit")
    print("1. multiplication of two variables")
    print("2. multiplication of three variables")
    print("3. Division and multiplication")
    print("4. equating variable")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Result: ", obj.mul())
    elif choice == 2:
        print("Result: ", obj.mul2())
    elif choice == 3:
        print("Result: ", obj.div())
    elif choice == 4:
        print("Result: ", round(obj.equal(), 2))
    elif choice == 0:
        print("Exiting!")
    else:
        print("Invalid choice!!")

print()




