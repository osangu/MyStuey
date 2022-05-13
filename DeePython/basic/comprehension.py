foo = '예시 문자열'

list_bar = [i for i in foo]

dict_bar = {i: j for i, j in enumerate(foo)}

print(list_bar)  # ['예', '시', '문',' ', '자', '열']

print(dict_bar)  # {0: '예', 1: '시', 2: ' ', 3: '문', 4: '자', 5: '열'}