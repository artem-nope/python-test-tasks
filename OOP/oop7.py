class A(object):
    def hello(self):
        print('Hello A')
    pass


class B(A):
    # def hello(self):
    #     print('Hello B')
    #     super().hello()
    pass


class C(B):
    def hello(self):
        print('Hello C')
        super().hello()
    pass


class D(A):
    def hello(self):
        print('Hello D')
        super().hello()
    pass


class F(C, D):
    def hello(self):
        print('Hello F')
        super().hello()
    pass


if __name__ == '__main__':
    f = F()
    f.hello()
    print(F.__mro__)
    c = C()
    c.hello()

