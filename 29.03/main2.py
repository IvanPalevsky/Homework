class Triangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        return new_x**2 + new_y**2

class Count(Triangle):
    def count(self):


A = Triangle(0, 0)
B = Triangle(3, 0)
C = Triangle(3, 3)

print(A)