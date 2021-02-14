# generator
# print(list(range(10000000000)))  #매우 오래 걸릴뿐더러 메모리 소모가 크다
# range() : 대표적인 generator

def make_list(num):
    result = []
    for i in range(num):
        result.append(i)
    return result


def generator_function(num):
    for i in range(num):
        yield i  # return과 같다


for i in generator_function(1000):
    print(i)

g = generator_function(100)
print(g)
print(next(g))
print(next(g))
# stopIteration Error : next가 범위를 넘어가면 나옴


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
def long_time1():
    print('1')
    for i in range(100000000):
        i * 5


@performance
def long_time2():
    print('2')
    for i in list(range(100000000)):
        i * 5


# long_time1()  # 3초
# long_time2()  # 9초
# generator는 메모리를 소비하지 않는다

def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            next(iterator)
        except StopIteration:
            break


special_for([1, 2, 3, 4, 5, 6])


class MyGen:
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(0, 100)
for i in gen:
    print(i)


def fb(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fb(10):
    print(x)
