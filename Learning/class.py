class SchoolMember:
    '''Будь яка людина в школі'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Створений SchoolMember {0})'.format(self.name))

    def tell(self):
        '''Вивести інформацію.'''
        print('Имя: "{0}" Вік: "{1}"'.format(self.name, self.age, ), end=" ")


class Teacher(SchoolMember):
    '''Презентація викладача'''

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print(f"(Создан Teacher: {name})")

    def tell(self):
        SchoolMember.tell(self)
        print(f"(Зарплата: '{self.salary}')")


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print(f'(Створений студент : {name})')

    def tell(self):
        SchoolMember.tell(self)
        print(f'Оцінки студента: {self.marks}')


t = Teacher('Mr. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print()

members = [t, s]
for member in members:
    member.tell()
