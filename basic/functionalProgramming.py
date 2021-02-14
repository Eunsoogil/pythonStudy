# functional programming
# pure function
def multiple_by2(*args):
    new_list = []
    for item in args:
        new_list.append(item * 2)
    return new_list


print(multiple_by2(1, 2, 3, 4, 5, 6))


# map, filter, zip, reduce
def multiple_by22(i):
    return i * 2


print(list(map(multiple_by22, [1, 2, 3])))

my_list = [1, 2, 3]
print(list(map(multiple_by22, my_list)))


# map - iterable한 객체를 받아 알아서 함수에 iterate함

def only_odd(i):
    return i % 2 != 0


print(list(filter(only_odd, my_list)))
# return이 true, false여야한다

your_list = [10, 20, 30]
print(list(zip(your_list, my_list)))
# iterable한 2가지 data를 합쳐줌

their_list = (5, 4, 3, 2)
print(list(zip(your_list, my_list, their_list)))
# 2는 잘라버림

from functools import reduce


# reduce는 import해야함

def accumulator(acc, i):
    print(acc, i)
    return acc + i


print(reduce(accumulator, my_list, 0))

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def cap(i):
    return i.capitalize()


print(list(map(cap, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

my_numbers.reverse()
print(list(zip(my_strings, my_numbers)))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def checkPass(i):
    return i > 50


print(list(filter(checkPass, scores)))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def reduceAnswer(acc, i):
    return acc + i


print(reduce(reduceAnswer, my_numbers, reduce(reduceAnswer, scores, 0)))
# print(reduce(accumulator, (my_numbers + scores))) # 더 나은 방법

# lambda expressions
print(list(map(lambda item: item * 2, my_list)))
print(reduce(lambda acc, item: acc + item, my_list))

my_list = [5, 4, 3]
print(list(map(lambda i: i * i, my_list)))
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)

# list comprehensions

my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

my_list2 = [i for i in 'hello']
my_list3 = [i * 2 for i in range(0, 100)]
my_list4 = [i ** 2 for i in range(0, 100) if i % 2 == 0]

print(my_list2)
print(my_list3)
print(my_list4)

# set comprehensions

# list에서 쓰는 것과 동일

# my_list2 = {i for i in 'hello'}
# my_list3 = {i*2 for i in range(0,100)}
# my_list4 = {i**2 for i in range(0,100) if i % 2 == 0}
#
# print(my_list2)
# print(my_list3)
# print(my_list4)

# dict comprehensions
simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {key: value ** 2 for key, value in simple_dict.items() if value % 2 == 0}
print(my_dict)

my_dict2 = {num: num ** 2 for num in list(range(1, 10))}
print(my_dict2)

# exercise
some_list = ['a', 'b', 'b', 'c', 'd', 'm', 'n', 'n']
result_list = []
for i in some_list:
    if some_list.count(i) >= 2 and result_list.count(i) == 0:
        result_list.append(i)

# 다른방법 if i not in result_list
print(result_list)

result_list = list(set([i for i in some_list if some_list.count(i) >= 2]))
print(result_list)


# higher order function HOC
# 함수 내부에 함수를 선언하여 돌려주거나 함수를 파라미터로 받는 함수를 HOC라함
def greet(func):
    func()


def greet2():
    def greeter():
        return 5

    return greeter


# decorator
def hello():
    print('helloooo')


greeting = hello  # 주소 복사
del hello  # hello 지움

print(greeting)
greeting()


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*******')
        func(*args, **kwargs)
        print('*******')

    return wrap_func


@my_decorator
def hello():
    print('hellooooo')


@my_decorator
def bye(message, emoji=':('):
    print(f'{message} bbyyyeee')


hello()
bye('sad')
my_decorator(hello)()  # 이렇게해도 되지만 가독성 떨어짐

from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'tooks {t2 - t1} ms')
        return result

    return wrapper


@performance
def long_time():
    for i in range(1000000):
        i * 5


long_time()

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True  # changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        # print(args)
        # print(args[0])
        if 'valid' in args[0]:
            if args[0]['valid']:
                result = fn(*args, **kwargs)
                return result
            return False
        return False

    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
message_friends('?')  # 폼검증
