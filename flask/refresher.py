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

