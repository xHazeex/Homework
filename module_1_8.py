# Работа со словарем
my_dict = {'Ivan' : 1975 , 'Oleg' : 1999 , 'Petya' : 2001}
print(my_dict['Ivan'])
print(my_dict.get('lexa'))
my_dict['Artem'] = 2005
my_dict['Ola'] = 2002
print(my_dict)
del my_dict['Oleg']
print(my_dict)

# Работа с множеством
my_set = {1, 2, '10', 2, '10'}
print(my_set)
my_set.add(22)
my_set.add('Нуууу')
print(my_set)
my_set.remove('10')
print(my_set)