# #Fundamental data type
# int
# float
# bool
# str
# list
# tuple
# set
# dict
#
# #classes -> custom types
#
# #Specialized data types
#
# None


print(type(6))
print(type(0))
print(type(2 / 4))  # 실수는 소숫점을 기준으로 따로 저장한다(?)
print(type(20 + 1.1))
print(type(9.9 + 1.1))
print(9.9 + 1.1)  # 11.0

# 결과가 정수로만 나옴
print(2 ** 3)  # 거듭제곱
print(2 * 3)
print(2 / 3)
print(2 // 3)  # 내림
print(4 // 3)
print(4 % 3)

# math function
print('\n----------------math function--------------------\n')
print(round(3.1))
print(abs(-20))  # 절대값

# complex, 또 다른 연산용 자료형
# bin() > 2진수 전환
print(bin(5))  # 0b101, 0b는 파이썬에서 ob이하의 수가 2진수라는 표기
print(int('0b101', 2))  # 2진수 > 10진수로

print('\n----------------variable--------------------\n')
PI = 3.14  # constant, 전부 대문자면 constant라는 의미, 재사용은 가능
a, b, c = 1, 2, 3
print(a + b + c)

print('\n----------------string--------------------\n')
print(type('string'))
long_string = '''
holy shit is
this
really
works?
?
?
'''

print(long_string)

# string concatenation
print('\n----------------string concatenation--------------------\n')
print('hello' + 'eunsoo')
# print('hello' + 5) 안됨
print('hello' + str(5))

# escape sequence
print('\n----------------escape sequence--------------------\n')
weather = 'it\'s \"kind of\" sunny'
print(weather)

# formatted strings
print('\n----------------formatted strings--------------------\n')
name = 'johnny'
age = 55

print('hi ' + name + '. You are ' + str(age) + ' years old')
print(f'hi {name}. You are {age} years old')  # 앞에 f붙임
print('hi {0}. You are {1} years old'.format(name, age))
print('hi {1}. You are {0} years old'.format(name, age))
print('hi {new_name}. You are {new_age} years old'.format(new_name='shayla', new_age='11'))

# string index
print('\n----------------string index--------------------\n')
selfish = '0123456789'
print(selfish[7])
print(selfish[-7])
print(selfish[1:])
print(selfish[:5])
print(selfish[0:8])
print(selfish[0:8:2])
print(selfish[::-1])

# built-in function
print('\n----------------built-in function--------------------\n')
length = 'lengthlengthl'
print(len(length))

quote = 'to be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.lower())
print(quote.find('be'))
print(quote.find('didyou'))
print(quote.replace('be', 'me'))

# booleans
print('\n----------------booleans--------------------\n')
name = 'andrei'
is_cool = True
is_cool = False

print(f'is {name} cool? {is_cool}')

# lists
print('\n----------------list------------------\n')

li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 'a', True]

print(li[0])
li[0] = 'list is mutable. you can not assign string like this'
print(li[0])
print(li[1:3])
li[0] = 1

li2[0] = 'd'
li4 = li2  # 주소복사인듯
li4[0] = 'a'
print(li2)
print(li4)

li2[0] = 'd'
li4 = li2[:]  # 값복사
li4[0] = 'a'
print(li2)
print(li4)

new_list = li.append(100)  # return value가 없음
print(li)
print(new_list)
new_list = li[:]
# list method의 index는 1부터 시작...
new_list.insert(5, 100)
print(new_list)
new_list.extend([101, 102, 103])
print(new_list)
new_list.pop()  # remove와 같지만 return value가 있다! ()안에 index를 넣으면 index value를 return
print(new_list)
new_list.remove(4)
print(new_list)
new_list.clear()
print(new_list)
print(li.index(2))
print(li)
li_check = ['z', 'a', 'b', 'c', 'd', 'e']
# print('\n----------------list 안됨------------------\n')
# print(li.index('6', 0, 5))  # ???
# print(li.index('6', 0, 5))  # ???
# print(li.index(3, 0, 5))  # ???
#
# li_check = ['a', 'b', 'c', 'd', 'e']
# print(li_check.index('x', 0, 4))
# print(li_check.index('a', 0, 4))
# print(li_check.index('a'))
print('\n----------------list------------------\n')
print('a' in li_check)
print(li_check.count('d'))
# li_check.sort() # list 정렬, list자체를 변경
print(li_check)
print(sorted(li_check))  # sorted는 return 값 있음
print(li_check)  # 근데 list는 건드리지 않음

li_check_new = li_check.copy()
print(li_check_new)

li_check.reverse()  # 역순 정렬이 아님, 따라서 sort를 먼저하고 사용하면 역순정렬됨
print(li_check)

print('\n----------------common list pattern------------------\n')

li = ['a', 'x', 'b', 'e', 'q', 'g', 'd', 'b', 'z']
li.sort()
li.reverse()
print(li)
print(li[::-1])

print(list(range(1, 100)))  # list 생성
print(list(range(100)))

sentence = ''
sentence = sentence.join(['hi', 'my', 'name', 'is', 'hoho'])
print(sentence)

sentence = ' '
sentence = sentence.join(['hi', 'my', 'name', 'is', 'hoho'])
print(sentence)

sentence = '!'.join(['hi', 'my', 'name', 'is', 'hoho'])
print(sentence)

# lists unpacking
print('\n----------------list------------------\n')

a, b, c, *other, d = list(range(1, 100))
print(a)
print(b)
print(c)
print(other)
print(d)

# None
print('\n----------------None------------------\n')
print('\n----------------None is null------------------\n')

# Dictionary
print('\n----------------Dictionary------------------\n')
dict1 = {
    'a': [1, 2, 3],
    'b': 'hello',
    'x': True
}
# key data type은 int str boolean은 되는데 list는 안됨 (immutable만 됨)
# key값 중복은 동작은 하지만 당연히 권장하지 않음
print(dict1['a'][1])
print(dict1.get('age', 55))  # key값이 age인지 찾고 없을시 55로 대체

user = dict(name='john', greet='hello')
print(user)
print('name' in user)
print('age' in user)
print('hello' in user)
print('hello' in user.keys())
print('hello' in user.values())
print(user.items())
print(user.pop('name'))
print(user.popitem())  # dictionary는 unordered, 따라서 random하게 제거
user.update({'age': 55})
print(user)

# Tuple
print('\n----------------Tuple------------------\n')
tuple1 = (1, 2, 3, 4, 5)  # immutable list, less flexible but faster
tuplebug = tuple1[1:2]
print(tuplebug)  # 뒤에 , 찍혀나옴...
print(tuple1.count(1))
print(tuple1.index(2))

# Set
print('\n----------------Set------------------\n')
set1 = {1, 2, 3, 4, 5, 5, 1, 2, 3}  # set은 duplicate가 없다
print(set1)

set1.add(2)
set1.add(3)
set1.add(100)
print(set1)

li = [1, 2, 3, 4, 5, 5, 1, 2, 3]
print(set(li))
print(1 in set1)
print(len(set1))
print(list(set1))

print('\n----------------Set method------------------\n')
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8, 9, 10}
set3 = {4}

print(set1.difference(set2))
set1.discard(5)
print(set1)
# set1.difference_update(set2) # 겹치는 부분을 실제로 삭제
# print(set1)
print(set1.intersection(set2))  # 교집합
print(set1 & set2)  # 교집합 (같은 결과)
print(set1.isdisjoint(set2))  # 겹치는 부분이 없는지 확인
print(set1.union(set2))  # 합집합
print(set1 | set2)  # 합집합(같은 결과)
print(set1.issubset(set3))  # 부분집합
print(set1.issuperset(set3))  # 부분집합 반대 개념
