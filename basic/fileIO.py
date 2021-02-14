my_file = open('test.txt')
print(my_file.read())
print(my_file.read())  # 한번만 읽을 수 있음
my_file.seek(0)  # seek 추가시 읽기 가능
print(my_file.read())

my_file.seek(0)
print(my_file.readline())  # 한줄씩 읽음
print(my_file.readline())  # 한줄씩 읽음
print(my_file.readline())  # 한줄씩 읽음

my_file.seek(0)
print(my_file.readlines())  # regular expression 포함해서 읽음

my_file.close()  # 자원 반납

print('\n--------------------with--------------------\n')
with open('test.txt') as my_file:
    print(my_file.readlines())

# close를 신경쓰지 않아도 됨

# mode r, reading r+ reading and writing a appending w 덮어쓰기
# r+의 경우 appending이 된다, python버전에 따라 다른듯
with open('test.txt', mode='r+') as my_file:
    text = my_file.write('hey it\'s me')
    print(my_file.readlines())

with open('test2.txt', mode='w') as my_file2:
    text = my_file2.write('hey it\'s me')

try:
    with open('test2.txt', mode='r') as my_file2:
        print(my_file2.readlines())
except FileNotFoundError as err:
    print('no file')
    raise err
except IOError as err:
    print('IO error')
    raise err
