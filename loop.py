is_old = True
is_licenced = False

if is_old:
    print('you are old enough to drive!')
elif is_licenced:
    print('you can drive now!')
else:
    print('you are not enough')

if is_old and is_licenced:
    print('you are old enough to drive!')
else:
    print('you are not enough')

# Truthy and Falsy
print('\n-------------------------Truthy and Falsy--------------------------\n')
is_old = 'hello'
is_licenced = 3
# 모든 값은 truthy 몇몇을 제외하면
# 0, {}, [] 등

if is_old and is_licenced:
    print('you are old enough to drive!')
else:
    print('you are not enough')

# 값이 있는지 없는지 체크하기 용이하다!

# Ternary Operator
print('\n-------------------------Ternary Operator--------------------------\n')

# condition_if_true if condition else condition_if_else
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)

# Short Circuiting
print('\n-------------------------Short Circuiting--------------------------\n')
is_friend = False
is_user = True

# 프로그램이 뒤의 is_friend는 무시, 의미가 없으므로
if is_user or is_friend:
    print('maybe friend')

# 프로그램이 무조건 넘어감, 실행될 수 없음
if is_user and is_friend:
    print('best friend forever')

# logical operator
print('\n-------------------------logical operator--------------------------\n')
# not() 혹은 not something, 나머지는 같음 ==, >, < 등

# is vs ==
print('\n-------------------------is vs ==--------------------------\n')

print(True == bool(1))
print('1' == 1)
print([] == [])
print(10 == 10.0)
print([1, 2, 3] == [1, 2, 3])

# is는 주소값 비교, immutable인 경우는 값 비교
print(True is bool(1))
print('1' is 1)
print([] is [])
print(10 is 10.0)
print([1, 2, 3] is [1, 2, 3])

# For loop
print('\n-------------------------For loop--------------------------\n')

# tuple, set도 가능
for item in [1, 2, 3, 4, 5]:
    print(item)

# iterable - list, dict, tuple, set, String

user = {
    'name': 'shayla',
    'age': 32,
    'lover': True
}

for item in user:
    print(item)

for item in user.items():
    print(item)

for k, v in user.items():
    print(k, v)
    print(k)
    print(v)

for item in user.keys():
    print(item)

for item in user.values():
    print(item)

# For loop exercise
print('\n-------------------------For loop exercise--------------------------\n')
li = list(range(1, 11))
result = 0
for i in li:
    result += i
print(result)

# range()
print('\n-------------------------range()--------------------------\n')
print(range(1, 100))  # range object return
for number in range(0, 100):
    print(number)

for _ in range(0, 10, 2):  # third parameter : 증감
    print(_)

for i in range(10, 0, -2):  # third parameter : 증감
    print(i)

# enumerate()
print('\n-------------------------enumerate()--------------------------\n')
for i, char in enumerate('helloooo'):
    print(i, char)
# list, tuple 다됨

# while
print('\n-------------------------while--------------------------\n')
i = 0
while i < 50:
    i += 1
    print(i)
    if i is 25:
        print('break time')
        break
else:
    print('done')  # while문 조건이 false일때

# continue, pass 있음, pass는 그냥 다음줄로 넘김

# exercise
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for i in picture:
    result = ''
    for pixel in i:
        if pixel == 0:
            result += ' '
        else:
            result += '*'
    print(result)

print('')
# 다른 방법
for image in picture:
    for pixel in image:
        if pixel == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print('')

# print default end = \n

# exercise
some_list = ['a', 'b', 'b', 'c', 'd', 'm', 'n', 'n']
result_list = []
for i in some_list:
    if some_list.count(i) >= 2 and result_list.count(i) == 0:
        result_list.append(i)

# 다른방법 if i not in result_list
print(result_list)

# function
print('\n-------------------------function--------------------------\n')


# default parameter
def say_hello(name='eunsoo', emoji=';)'):
    print(f'helllooooooo {name} {emoji}')


say_hello('shayla', ':)')  # 선언한 후에 존재해야함
print(say_hello)  # 주소
say_hello()
say_hello(emoji=':)')

# return
print('\n-------------------------return--------------------------\n')


def sum1(num1, num2):
    print('sum')
    return num1 + num2


result = sum1(10, 5)
print(sum1(10, result))

# docString
print('\n-------------------------docString--------------------------\n')


def test(a):
    """
    :param a: this is what you wanna print
    :return: print action
    """
    print(a)


help(test)

# *args **kwargs(keyword arguments)
print('\n-------------------------*args **kwargs--------------------------\n')


# *뒤에 아무렇게나 넣어도됨, args는 약속
def args(*args, **kwargs):
    print(args)
    print(kwargs)

    total = 0
    for i in kwargs.values():
        total += i
    return sum(args) + total


print(args(1, 2, 3, 4, 5, 6, 78, num1=5, num2=10))


# 정해져있는 파라미터 순서
# parameters, *args, default parameters, **kwargs

def highest_even(li):
    li.sort()
    li.reverse()
    for i in li:
        if i % 2 == 0:
            return i


print(highest_even([10, 2, 3, 4, 8, 11]))

# walrus operator
print('\n-------------------------walrus operator--------------------------\n')

a = 'heellllooooooooo'

# n에 len(a) 결과를 담음
if (n := len(a)) > 10:
    print(f'too long {n} elements')

while (n := len(a)) > 1:
    print(n)
    a = a[:-1]

print(a)

# scope
print('\n-------------------------scope--------------------------\n')

# scope - what variables do I have access to?
a = 1


def parent():
    # global a
    # 앞에 global 붙이면 global 변수 가져옴
    # parameter 넣는게 좋다
    a = 10

    def confusion():
        return a

    return confusion()


print(parent())
print(a)

# 0 - scope order
# 1 - start with local
# 2 - parent local?
# 3 - global
# 4 - built in python function

# nonlocal
print('\n-------------------------nonlocal--------------------------\n')
# scope order대로 상위 변수를 찾아서 return


def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner:', x)

    inner()
    print('outer:', x)


outer()
