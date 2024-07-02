import sys
from functools import singledispatchmethod


class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def showName(self):
        print("Person name=%s" % self.name)

    @staticmethod
    def showInfo():
        print("showInfo...")


class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def showName(self):
        print("Student name=%s" % self.name)
        # 显示调用父类方法
        # super(Student,self).showName()

    # 用于定义方法的函数重载singledispatchmethod
    # 根据第一个参数不同实现函数重载思想(但第一个参数相同时，则不能定义不同的参数重载函数)
    @singledispatchmethod
    def doSomeThing(self, arg):
        raise NotImplemented

    @doSomeThing.register
    def __(self, arg: int):
        print('int arg=', arg)

    # @doSomeThing.register
    # def __(self, arg: str):
    #     print('str arg=', arg)

    @doSomeThing.register
    def __(self, arg: str,arg2: int):
        print('str arg=', arg,arg2)

    #比较运算符(=)
    def __eq__(self, other):
        return self.score == other.score

    # 比较运算符(<)
    def __lt__(self, other):
        return self.score < other.score

def test1():
    print('sys.version_info=', sys.version_info)

    person = Person('Jim', 'male')
    person.showName()
    student = Student('Mary', 'female', 90)
    student.showName()

    student.doSomeThing(1)
    student.doSomeThing('str2', 10)

    Student.showInfo()

    # 显示类信息
    print(dir(student))

    stu1 = Student('Mary', 'female', 90)
    stu2 = Student('Jim', 'male', 92)
    # print(stu1 == stu2)
    print(stu1 < stu2)


if __name__ == '__main__':
    test1()
