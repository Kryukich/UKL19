'''
This script make a dictionary ID : emitent
'''
data_list = []
with open('for_em.txt', encoding='utf-8') as emitent_information:
    for line in emitent_information:
        data_list.append(line)

_id, _name, _code = data_list[0], data_list[1], data_list[2] 
_id = _id[_id.index('[') + 1: _id.index(']')].split(',')
_name = _name[_name.index('[') + 1: _name.index(']')].split(',')
_code = _code[_code.index('[') + 1: _code.index(']')].split(',')
# for i in range():
print(_id, _code, _name)
print(len(_id), len(_code))
# print(_name)
