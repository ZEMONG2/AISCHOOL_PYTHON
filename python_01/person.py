class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_name(self):
        print('제 이름은 %s입니다.' % self.name)
    def get_age(self):
        print('제 나이는 %s세 입니다.' % self.age)

class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade
    def get_grade(self):
        print('제 학점은 %.1f입니다.' % self.grade)

if __name__ == "__main__":
    obj = Student('이기자',27,3.3)
    obj.get_name()
    obj.get_age()
    obj.get_grade()