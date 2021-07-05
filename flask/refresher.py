x = 15
price = 9.99

discount = 0.2

result = price * (1 - discount)

print(result)

name = 'Rolf'

print(name * 2)

greeting = f'hello, {name}'

print(greeting)

name = 'Bob'

print(greeting)  # hello rolf로 나옴
print(f'hello, {name}')

with_name = greeting.format("Rolf")
print(with_name)

longer_phrase = "hello, {}. Today is {}"
formatted = longer_phrase.format("rolf", "monday")
print(formatted)

# name = input("enter your name: ")
# print(name)

# size_input = input("how big is your house (in square feet): ")
# square_feet = int(size_input)
# square_meters = square_feet / 10.8
# print(f"{square_feet} square feet is {square_meters:.2f} square meters.")

# user_age = int(input("enter your age: "))
# months = user_age * 12
# print(f"your age, {user_age}, is equal to {months} months")

l1 = ['bob', 'rolf', 'anne']
t1 = ('bob', 'rolf', 'anne')  # tuple : 값을 바꿀 수 없다
s1 = {'bob', 'rolf', 'anne'}  # 중복이 불가능하다

l1.append("smith")
l1.remove("smith")
print(l1)

t2 = ('bob',)  # 값 1개만 넣으러면 이런식으로 선언해야함 그냥 ()는 못읽음

s1.add("smith")
s1.add("smith")
print(s1)  # 중복 안됨

s2 = {'bob', 'anne'}
s3 = s1.difference(s2)
print(s3)
s3 = s1.union(s2)
print(s3)
s3 = s1.intersection(s2)
print(s3)

l1 = ["rolf", "bob"]
l2 = ["rolf", "bob"]

print(l1 == l2)  # 값 비교
print(l1 is l2)  # 주소 비교

day = "monday"

if day == "monday":
    print("monday")
elif day == "tuesday":
    print("tuesday")
else:
    print("no")

movies = {"matrix", "green book", "her"}
print("matrix" in movies)
print("eclipse" in movies)

friends = ['rolf', 'jen', 'bob', 'anne']

for friend in friends:
    print(f'{friend} is my friend')

for i in range(4):
    print(i)

grade = [35, 50, 11, 60]
total = sum(grade)
amount = len(grade)
print(total / amount)

numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]
print(doubled)

friends = ['rolf', 'jen', 'bob', 'anne', 'sam', 'samantha']
starts_s = [friend for friend in friends if friend.startswith("s")]
print(starts_s)

friend_ages = {'rolf': 24, 'adam': 30, 'anne': 27}
print(friend_ages['adam'])

friends = [
    {'name': 'rolf', 'age': 24},
    {'name': 'adam', 'age': 30},
    {'name': 'anne', 'age': 27}
]

print(friends[1]["name"])

for friend in friend_ages:
    print(f"{friend} : {friend_ages[friend]}")

# better way
for name, age in friend_ages.items():
    print(name, age)

total_age = friend_ages.values()
print(sum(total_age) / len(total_age))

print(list(friend_ages.items()))  # list 내의 tuple로 반환됨

people = [('bob', 42, 'mechanic'), ('james', 24, 'artist'), ('harry', 32, 'lecturer')]
for name, age, job in people:
    print(name, age, job)

# _는 신경쓰지 않는다는 이야기, 일종의 약속
for name, age, _ in people:
    print(name, age)

# head에 첫번째것만, tail에 나머지 들어감
head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)

*head, tail = [1, 2, 3, 4, 5]
print(head)
print(tail)


def hello():
    print("hello")


hello()


def user_age_in_seconds():
    user_age = 32
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"your age in senconds is {age_seconds}")


user_age_in_seconds()

friends = ['rolf', 'jen', 'bob', 'anne', 'sam', 'samantha']


def add_friend():
    friend_name = "jack"
    # 잘 동작함
    # friends.append(friend_name)

    # 반드시 아래처럼 선언을 해줘야 한다
    f = friends

    # 선언 없이 사용 안되는 코드, x = x + 1 만 있으면 함수 내부에 x가 선언이 안되어 있다고 생각함
    f = f + [friend_name]


add_friend()
print(friends)


# y = default parameter
def add(x, y=8):
    return x + y


print(add(3, 5))
# 이런식으로 파라미터 지정 가능
print(add(x=5, y=3))
print(add(5))

# 명명 가능
addlambda = lambda a, b: a + b

sequence = [1, 3, 5, 7]

# map보다 빠르다
doubled = [(lambda x: x * 2)(x) for x in sequence]
print(doubled)
doubled = list(map(lambda x: x * 2, sequence))
print(doubled)

users = [
    (0, 'bob', 'password'),
    (1, 'rolf', 'bob123'),
    (2, 'jose', 'longjkopq'),
    (3, 'username', '1234')
]

# username을 키 값으로
username_mapping = {user[1]: user for user in users}
print(username_mapping)


# *args : 매개변수를 tuple로 저장
def multiply(*args):
    print(args)
    totalmul = 1
    for arg in args:
        totalmul *= arg

    return totalmul


print(multiply(1, 3, 5))


def check(x, y):
    return x + y


nums = [3, 5]
# nums list의 값을 하나씩 넣는다 (unpacking)
print(check(*nums))

nums = {'x': 15, 'y': 25}
# key의 이름과 함수 파라미터에 정의된 이름이 같을때 사용 가능
print(check(**nums))


def apply(*args, operator):
    if operator == '*':
        # unpacking이 필요하다, 하지 않으면 tuple을 넣기 때문에 튜플안의 튜플
        return multiply(*args)
    else:
        return 'nono'


print(apply(1, 3, 5, 7, operator='*'))


def named(**kwargs):
    # kwargs : dictionary return
    print(kwargs)


named(name="bob", age=25)

details = {'check': 'checker', 'age': 11}

named(**details)


def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, name="bob", age=25)


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student("bob", (90, 80, 70))
print(student.name)
print(student.grades)
print(student.average())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person {self.name}, {self.age} years old"

    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"


bob = Person("bob", 35)
# 원래 주소값이 출력되지만, __str__때문에 __str__이 출력됨
print(bob)


class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        newItem = {'name': name, 'price': price}
        self.items.append(newItem)

    def stock_price(self):
        sum = 0
        for i in self.items:
            sum += i['price']
        return sum


test = Store('test')

test.add_item('test', 12)

print(test.stock_price())


class ClassTest:
    def instance_method(self):
        print(f"{self}")

    @classmethod
    def class_method(cls):
        print(f"{cls}")

    @staticmethod
    def static_method():
        print("called static_method")


# class 인스턴스를 호출하는 instance method, 인스턴스가 필요하다
# 대부분 사용하는 흔한 메소드
test = ClassTest()
test.instance_method()
ClassTest.instance_method(test)

# 자기 자신을 호출하는데 인스턴스가 필요없다
# factory pattern에서 사용
ClassTest.class_method()

# class내에 있지만 class와는 전혀 무관한 method
ClassTest.static_method()


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<{self.name}, {self.book_type}, {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        # cls를 사용하는 것이 더 좋다 (확장성, 유연성 면에서)
        # return Book(name, Book.TYPES[0], page_weight + 100)
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        # return Book(name, Book.TYPES[1], page_weight - 100)
        return cls(name, cls.TYPES[1], page_weight - 100)


book = Book("Harry Potter", "hardcover", 1500)
print(book)

book2 = Book.hardcover("Harry Potter2", 1500)
print(book2)

book3 = Book.paperback("Harry Potter3", 1500)
print(book3)


class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected")


# 상속
class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} page remaining)"

    def print(self, pages):
        if not self.connected:
            print("your printer is not connected")
            return
        print("print {pages} pages")
        self.remaining_pages -= pages


printer = Printer("Printer", "USB", 500)
printer.print(20)

print(printer)

printer.disconnect()


# class composition
# 연관관계이지만 별도의 class일때
class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books"


class Book2:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"book {self.name}"


book = Book2("Harry porter")
book2 = Book2("Harry porter2")
shelf = BookShelf(book, book2)

print(shelf)


# 힌트 기능, 타입이 잘못되면 IDE가 알려줌
# from에 . 혹은 .. 같이 상대경로 입력 가능
from typing import List


# class의 경우 -> "클래스명" 으로 해야함
def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)


# list_avg(123)

# import to refresher2
def divide(divided, divisor):
    if divisor == 0:
        # throw error, traceback 발생하며 stop
        raise ZeroDivisionError("cannot be 0, zerodivisionerror")

    return divided / divisor


# first class function
# operator에 사용할 메소드를 명시해줌으로써 사용 가능
def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 4, operator=divide)
print(result)


# traceback 발생하지 않음
try:
    # print(divide(15, 0))
    print(divide(15, 3))
except ZeroDivisionError as e:
    print(e)
    print("cannot be 0")
else:
    # exception 발생하지 않을 시 동작
    print("no error")
finally:
    print("module done")


class Book2:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>"

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesError(
                f"limitation of book pages is {self.page_count}"
            )
        self.pages_read += pages
        print(f"you have now read {self.pages_read} pages put of {self.page_count}")


# custom error
class TooManyPagesError(ValueError):
    pass


python101 = Book2("Python 101", 50)

try:
    python101.read(35)
    python101.read(50)
except TooManyPagesError as e:
    print(e)


user = {"username": "jose", "access_level": "guest"}


import functools


# factory pattern
def make_secure(access_level):
    # 함수를 파라미터로 넣는다, decorator pattern
    def decorator(func):

        # 함수 내의 다른 함수 정의
        # functool을 넣어 get_admin_password의 내용이 대채됨을 막는다
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                # 받아온 함수 파라미터를 실행
                return func(*args, **kwargs)
            else:
                return "no admin"

        # 함수내 정의된 함수를 돌려준다
        return secure_function

    return decorator


# 데코레이터를 넣어서 make_secure를 실행하게 한다
@make_secure("admin")
def get_admin_password():
    return "1234"


@ make_secure("guest")
def get_name():
    return "name"


# 함수가 재정의된다
# decorator를 넣으면 아래처럼 실행할 필요는 없다
# get_admin_password = make_secure(get_admin_password)
print(get_admin_password())
print(get_name())

# 함수가 overwrite되지 않음을 확인할 수 있음
print(get_admin_password.__name__)

# 파이썬은 몇가지를 제외하고 (string, integer, tuple..) 모두 mutable
# 파이썬은 primitive type이 없고 모두 objcet이다

# 주소값이 있음을 확인할 수 있다
# 다만, immutable의 경우 이미 고유의 주소값이 있으며 수정할 수 없다(유일함)
print(id(84626))


from typing import Optional


class MutableExample:
    # list의 default를 mutable로 하면 같은 주소를 참조하는 list를 생성하므로
    # 객체를 다르게 생성해도 같은 list를 참조한다
    # def __init__(self, name: str, list: List[int] = []):
    #     self.name = name
    #     self.list = list

    # 따라서 none를 활용하는게 좋다
    # optional을 사용하면 더 확실하다
    # 애초에 default를 mutable로 사용하는 것 자체가 좋지 않다(유일하지 않으므로 위처럼 같은 위치를 참고할 수 있다)
    def __init__(self, name: str, list: Optional[List[int]] = None):
        self.name = name
        self.list = list or []

    def set_list(self, value: int):
        self.list.append(value)


ex1 = MutableExample("ex1")
ex2 = MutableExample("ex2")
ex1.set_list(90)
print(ex1.list)
print(ex2.list)

