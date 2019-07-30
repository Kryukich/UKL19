'''
This script make a dictionary ID : emitent
'''
data_list = []
with open('for_em.txt', encoding='utf-8') as emitent_information:
    for line in emitent_information:
        data_list.append(line)

_id, _name, _code = data_list[0], data_list[1], data_list[2]
_id = _id[_id.index('[') + 1: _id.index(']')].split(',')
_code = _code[_code.index('[') + 1: _code.index(']')].split(',')
# убираю кавычки у тикера
for ticker in range(len(_code)):
    _code[ticker] = _code[ticker][1: len(_code[ticker]) - 1]
dictionary_of_ticker_and_id = dict(zip(_code, _id))  # объединяю в словарь
print(len(_id), len(_code), 'SBER' in dictionary_of_ticker_and_id)
