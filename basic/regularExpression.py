import re

pattern = re.compile('search')  # 추가시 없을시 noneType error 안남
string = 'search inside of this text please!'

print('search' in string)

# print(re.search('search', string))
# a = re.search('search', string)

a = pattern.search(string)  # pattern 있을시
b = pattern.findall(string)
c = pattern.fullmatch(string)  # string이 pattern과 정확히 일치해야함
d = pattern.match(string)

print(a.span())
print(a.start())
print(a.group())

print(b)
print(c)
print(d)

# regex101.com  테스트용
# https://regexone.com/ 연습
