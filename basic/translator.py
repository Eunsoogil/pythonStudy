from translate import Translator

# en, ja, ko, es(spanish)
translator = Translator(to_lang='ko')
try:
    with open('./translator.txt', 'rt', encoding='UTF8') as trans:  # UTF-8로 여는법
        text = trans.read().split('\n')
        with open('./translator_result_kor.txt', mode='w') as translator_result_kor:
            translator_result_kor.write('')
        for i in text:
            text2 = i.split('. ')
            for j in text2:
                transResult = translator.translate(j)
                print(transResult)
                with open('./translator_result_kor.txt', mode='a') as translator_result_kor:
                    translator_result_kor.write(transResult)
except FileNotFoundError as err:
    print('no file')
    raise err
except IOError as err:
    print('IO error')
    raise err
