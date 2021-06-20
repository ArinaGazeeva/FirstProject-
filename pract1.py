class room(object):
    def __init__(self,name):
        self.name=name
    
class zal(room):
    def __init__(self,name, number):
        self.Parent=True
        self.Student=True
        self.Teacher=True
        self.Director=True
        self.name=name
        self.number=number
        print('zal', name, number)

class study_room(room):
    def __init__(self,name, number):
        self.Parent=False
        self.Student=True
        self.Teacher=True
        self.Director=True
        self.name=name
        self.number=number
        print('study_room', name, number)

class uchitelskaia(room):
    def __init__(self, name, number):
        self.Parent=False
        self.Student=False
        self.Teacher=True
        self.Director=True
        self.name=name
        self.number=number
        print('uchitelskaia', name, number)

class directors_room(room):
    def __init__(self,name,number):
        self.Parent=False
        self.Student=False
        self.Teacher=False
        self.Director=True
        self.name=name
        self.number=number
        print('directors_room', name, number)
class people(object):
    def __init__(self):
        self.place="hall"


class Parent(people):
    place='hall'
    def __init__(self,name,job):
        self.isParent=True
        self.name=name
        self.job=job
        print('Parent', self.name, self.job)
    def visit(self,place):
        if place.Parent==True:
            print(f"Parent {self.name} зашел в {type(place).__name__} {place.name} {place.number}")
            self.place=place.name
        else:
            print(f"Parent {self.name} отказано в доступе в {type(place).__name__} {place.name} {place.number}")
    
class Student(people):
    place='hall'
    def __init__(self,name,game):
        self.isStudent=True
        self.name=name
        self.game=game
        print("Student", self.name, self.game)
    def visit(self,place):
        if place.Student==True:
            print(f"Student {self.name} ворвался в {type(place).__name__} {place.name} {place.number}")
            self.place=place.name
        else:
            print(f"Student {self.name} пытался проникнуть в {type(place).__name__} {place.name} {place.number}")

class Teacher (people):
    place='hall'
    def __init__(self,name,joke):
        self.isTeacher=True
        self.name=name
        self.joke=joke
        print("Teacher", self.name, self.joke)
    def visit(self,place):
        if place.Teacher==True and (type(place) is study_room or type(place) is zal):
            print(f"Teacher {self.name} грозно вошел в {type(place).__name__} {place.name} {place.number}")
            self.place=place.name
        elif place.Teacher==True:
            print(f"Teacher {self.name} вошел в {type(place).__name__} {place.name} {place.number}")
            self.place=place.name
        else:
            print(f"Teacher {self.name} не смог войти в {type(place).__name__} {place.name} {place.number}")

        
class Director (people):
    place='hall'
    def __init__(self,name,awards):
        self.isDirector=True
        self.name=name
        self.awards=awards
        print("Director", self.name, self.awards)
    def visit(self,place):
        if place.Director==True:
            print(f"Director {self.name} грозно вошел в {type(place).__name__} {place.name} {place.number}")
            self.place=place.name
        else:
            print(f"Director {self.name} не смог войти в {type(place).__name__} {place.name} {place.number}")



director=Director("Иванов Иван","*очень крутая награда*")
physicist=Teacher("Юрий Юрьев"," В телескоп на Солнце можно посмотреть всего два раза в жизни. Правым и левым глазом...")
student1=Student("Вася Васечкин", "Minecraft")
parent1=Parent("Олег Олегов","юрист")
print('')
zal1=zal("Зеленый зал", 101)
physics_room=study_room("Кабинет физики", 102)
math_room=study_room("Кабинет математики", 103)
uchit1=uchitelskaia("Учительская 1", 104)
Directors_room=directors_room("Кабинет директора", 105)
print('')
parent1.visit(zal1)
parent1.visit(physics_room)
parent1.visit(math_room)
parent1.visit(uchit1)
parent1.visit(Directors_room)
print('')
director.visit(zal1)
physicist.visit(zal1)
student1.visit(zal1)
parent1.visit(zal1)
print('')
student1.visit(Directors_room)
            
