# -*- coding: utf-8 -*-
import json
import types


# 定义类
class Person(object):
    address = 'Earth'  # 定义类属性

    def __init__(self, name, **kwargs):
        self.name = name
        self.__count = 10  # 定义私有属性
        for k, v in kwargs.items():
            setattr(self, k, v)


jack = Person('jack', age=13)
queen = Person('queen', age=32)
king = Person('king', age=21)

# print(jack, queen)
print(jack == queen)
# 按照年龄大小对对象排序
L2 = sorted([jack, queen, king], key=lambda p: p.age)
for v in L2:
    print(v.name, v.age)
# print(Person.address)
try:
    print(Person.__count)
except AttributeError:
    print('AttributeError')

jack.job = 'coder'
del jack.job  # 删除实例属性


class Student(object):
    __count = 100

    __slots__ = ('__name', '__score', 'getScore')  # 限制类的属性列表

    @classmethod  # 定义类方法 cls指向类本身
    def count(cls):
        print(cls.__count)

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score > 100 or score < 0:
            raise ValueError('invalid score.')
        self.__score = score

    def __call__(self, *args, **kwargs):  # 该方法使得类的实例变成一个可调用对象
        print('My name is %s.' % (self.__name))


def fn_get_score(self):
    print(self.score)


near = Student('Near', 99)
# near.score = 10
# near.score = 101
# print(near.score)
# 动态为实例添加方法  types.MethodType() 把一个函数变为一个方法
near.score = 99
near.getScore = types.MethodType(fn_get_score, near)
near.getScore()

Student.count()  # 调用类方法
near()  # 调用实例


# 类的继承
class Animal(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '%s %s' % (str(self.__class__), self.name)

    __repr__ = __str__


class Dog(Animal):
    def __init__(self, name, color):
        # 函数super(Dog, self)将返回当前类继承的父类，即 Animal
        # self参数已在super()中传入，在__init__()中将隐式传递
        super(Dog, self).__init__(name)
        self.color = color


class Cat(Animal):
    def __init__(self, name, color):
        super(Cat, self).__init__(name)
        self.color = color


def show_info(obj):
    print(obj)


# 多态
animal = Animal('animal')
# show_info(animal)
dog = Dog('dog', 'blue')
# show_info(dog)
cat = Cat('cat', 'red')
# show_info(cat)

# 类型判断 isinstance
print(isinstance(dog, Animal))


# 任何对象，只要有read()方法，就称为File-like Object
class A(object):
    def read(self):
        return '["Tim", "Bob", "Alice"]'


a = A()
print(json.load(a))

# 获取对象信息
print(type(123))  # type()函数获取变量类型
print(type(dog))
print(dir(dog))  # dir()函数获取变量所有属性
setattr(dog, 'name', 'xixi')
print(getattr(dog, 'name'))
print(getattr(dog, 'age', 3))  # 获取age属性，如果属性不存在，就返回默认值, 否则报错
