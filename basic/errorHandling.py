# Error Handling
while True:
    try:
        age = int(input('what is your age?'))
        print(age)
        # raise Exception('?')  #throwing error
        # raise ValueError('?')
    except ValueError:  # 어떤 error타입인지 명시하지 않아도 됨
        print('age man age...')
    except ZeroDivisionError:
        print('Are you just born?')
    else:
        print('good to know')
        break
    finally:
        print('!')  # log남길때 좋음


# else : exception이 없을 때 실행

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'no no {err}')


print(sum(1, '1'))
