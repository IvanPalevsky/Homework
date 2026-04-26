class Book:
    def __init__(self, name, author, page_num, year):
        self.name = name
        self.author = author
        self.page_num = page_num
        self.year = year

class Pupil:
    def __init__(self, name, surname, age, grades=[]):
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = grades

    def count_grades(self):
        return sum(self.grades)/len(self.grades)

pupil = Pupil('Mike', 'Black', 16, [9, 8, 7, 6, 9])