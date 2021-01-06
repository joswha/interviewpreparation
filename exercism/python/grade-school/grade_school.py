from collections import defaultdict

class School:
    def __init__(self):
        self.students = defaultdict(list)

    def add_student(self, name, grade):
        self.students[grade].append(name)

    def roster(self):
        return sum((self.grade(g) for g in sorted(self.students)), [])

    def grade(self, grade_number):
        return sorted(self.students[grade_number])