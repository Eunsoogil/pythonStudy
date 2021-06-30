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