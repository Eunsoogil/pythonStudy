# import 방식
# import dataType
# 또는
# from dataType import class or function
# 아래 방식이 더 나음, * 가능

# __name__ : print(__name__)하면 파일명 나옴
# 참고로 파이썬에서 파일은 module
# 폴더 package
# 폴더 내 import : import 폴더.모듈

# if __name__ == '__main__':
# main은 하나임 다른 파일(모듈)에 해도 안나오며 main이름 바꿔도 main이라고 나옴

from random import shuffle  # external libriaries에 오픈소스 있음..

my_list = [1,2,3,4,5]
shuffle(my_list)
print(my_list)

import sys
print(f'hiiii {sys.argv[1]} {sys.argv[2]}')
# 터미널에 파일명.py param1 param2 식으로 값 전달 가능

# pypi.org > python package index > 여러 모듈 올라옴
# standard에 있는지 확인하고 여기서 확인
# python built in 구글 검색하면 standard, 안되면 pypi로 검색

# venv 하위에 파일을 만드는 이유 : 여러 모듈 버전 유지에 좋음