'''
This script make a dictionary ID : emitent
'''
data_list = []
with open('for_em.txt', encoding='utf-8') as emitent_information:
    for line in emitent_information:
        data_list.append(line)

_id, _name = data_list[0], data_list[1]
_id = _id[_id.index('[') + 1: _id.index(']')].split(',')
_name = _name[_name.index('[') + 1: _name.index(']')].split(',')
# for i in range():
print(_id)
# print(_name)
