class A:
    def method1(self):
        print("Inside method 1")

    def method2(self):
        print("Inside method 2")


class B(A):   # Inheriting class A
    def method3(self):
        print("Inside method 3")

    def method4(self):
        print("Inside method 4")


class Inh1:
    @staticmethod
    def main():
        obj = B()
        obj.method1()
        obj.method2()
        obj.method3()
        obj.method4()


# Calling main method
Inh1.main()