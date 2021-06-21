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
