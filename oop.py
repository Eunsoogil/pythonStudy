# oop
print('\n------------------------oop-----------------------\n')
print(type(None))
print(type(True))
print(type(5))


# object임
class BigObject:
    # code
    pass


print(type(BigObject))

objTest = BigObject()  # instanciate

print(objTest)  # 주소


class PlayerCharacter:
    # Class Object Attribute
    # static, 바꿀 수 있음
    membership = True

    # __ dunder method
    # name에 첫번째 파라미터가 들어감
    def __init__(self, name='annoymous', age=0):
        if self.membership:
            if age > 18:
                self.name = name
                self.age = age

    def run(self):
        print('run')

    def shout(self):
        print(f'my name is {self.name}')

    # 일종의 전역 method
    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    # 이런식으로도 사용 가능
    @classmethod
    def start(cls, num1, num2):
        return cls('default', num1 + num2)

    # 일종의 전역 method
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('cindy', 44)
# player1이 self가 된다
player2 = PlayerCharacter('tom', 22)

print(player1)
print(player1.name)
print(player1.age)
print(player2.name)
print(player2.age)
print(player1.run())  # function이 return이 없으면 none return
print(player1.membership)
print(player1.shout())

player3 = PlayerCharacter('jack', 10)
# print(player3.shout()) # 생성자 제한으로 안됨

print(player1.adding_things(2, 3))
print(PlayerCharacter.adding_things(2, 3))

player4 = PlayerCharacter.start(10, 9)
print(player4.age)

player1.membership = False
print(player1.membership)


# Encapsulation : 1. data fields와 methods를 하나로 묶고, 2. 이를 외부에 감춘다

# Abstraction : 객체의 정보와 기능들을 담아 명명하여 쉽게 접근하기 위함
# public인 경우, player1.speak = 'booo' 같은 것이 가능하다
# Abstraction 기능을 위해 private이 이상적이지만 python에는 그런 기능이 없음
# 앞에 _를 붙어 있으면 private라는 의미, 하지만 접근은 가능(???)

# Inheritance : 상속, 재사용성
class User:
    def sign_in(self):
        print('logged in')


# __init__이 반드시 필요한 것은 아님


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print('fire ball')


wizard1 = Wizard('merlin', 50)
wizard1.attack()
print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))

# Polymorphism : 다형성, 재사용성

# exercise
print('\n------------------------exercise-----------------------\n')


class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 1 Add another Cat
class John(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Simon('simon', 2), Sally('sally', 1), John('john', 3)]
print(my_cats)

# 3 Instantiate the Pet class with all your cats use variable my_pets
pets = Pets(my_cats)
print(Pets)

# 4 Output all of the cats walking using the my_pets instance
pets.walk()

# super
print('\n------------------------super-----------------------\n')
# 상속시 부모class.__init__.함수(self, *args) 식이였음
# 이젠 상속시 super.__init__.함수(self, *args) 가능(매우 불편..)

# introspection
print(dir(wizard1))  # 뭐 있는지 나옴


# 내부에 dunder method가 있음을 알 수 있음
# 당연히 수정 가능, class를 위한 기능들이 내장되어 있다

class SuperList(list):  # 매개변수 형이 list가 됨
    def __len__(self):
        return 1000


super_list1 = SuperList();

print(len(super_list1))
super_list1.append(5)
print(super_list1)
print(issubclass(SuperList, list))  # true나옴, 상속받음


# multiple inheritance : 그냥 매개변수를 넣으면 됨..
class HybridBorg(Simon, Sally, John):
    pass


hb1 = HybridBorg('hb1', 50)
print(hb1.sing('work?'))


# MRO - Method Resolution Order
class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


# A -> B, C -> D, D는 multiple inheritance
print(D.num)
print(D.__mro__)  # 상속 순서 보여줌
# 상속이 심하게 꼬이면 유지보수 불가
