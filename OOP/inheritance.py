class A:
    def f1(self):
        print("f1 works")

    def f2(self):
        print("f2 works")

    def show(self):
        print("show works A")

class B:
    def f3(self):
        print("f3 works")

    def f4(self):
        print("f4 works")

    def show(self):
        print("show works B")

class C(A,B):
    def f5(self):
        print("f5 works")

    def show(self):
        print("show works C")


obj1 = C()


# obj2 = C()
# obj1.f1()
# obj1.f2()
# obj1.f3()
# obj1.f4()
# obj1.f5()
# obj1.show()

print("calling B.show()...")
B.show(obj1)

# MRO - Method Resolution Order - order in which it is inherited