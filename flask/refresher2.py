import sys
# from에 . 혹은 .. 같이 상대경로 입력 가능
from refresher import divide

print("import")

# 파이썬의 파일 탐색 경로를 확인할 수 있음
print(sys.path)
print(divide(10, 2))

# export PYTHONPATH=/Users
# unix환경에서 export하면 sys.path에 추가됨을 알 수 있음

# import된 모듈들 확인
# refresher에서 import한 typing도 같이 import됨을 알 수 있음
print(sys.modules)

# __init__ 파일 : 필요한 파일들을 모아서 돌림 (파이썬 2버전에서는 __init__파일 외에는 import가 안됨)


