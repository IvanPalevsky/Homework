# class A:
#     def hello(self):
#         print('hello')
# class B(A):
#     def hi(self):
#         pass
# a = B()
# a.hello()

# class A:
#     def hello(self):
#         print('hello')
# class B:
#     def hello(self):
#         print('hi')
# class C:
#     def hello(self):
#         print('welcome')
# a = A()
# a.hello()
# b = B()
# b.hello()
# c = C()
# c.hello()

class A:
    def __init__(self, x):
        self.__x = x
    def print(self):
        print(self.__x)
a = A(100)
a.print()
print(a.__x)
