class GroupFullException(Exception):
    def __init__(self, message="Неможливо додати студента: група повна (максимум 10 студентів)."):
        self.message = message
        super().__init__(self.message)

class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} years old"

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.record_book == other.record_book
        return False

    def __hash__(self):
        return hash(self.record_book)

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupFullException()
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Group Number: {self.number}\n{all_students}'




students = [
    Student('Male', 20 + i, f'Name{i+1}', f'Surname{i+1}', f'RB{i+1}') for i in range(11)
]

group = Group('PD1')


for st in students:
    try:
        group.add_student(st)
        print(f"✅ Додано: {st.first_name} {st.last_name}")
    except GroupFullException as e:
        print(f"❌ Помилка: {e}")

print("\n📋 Склад групи:")
print(group)
