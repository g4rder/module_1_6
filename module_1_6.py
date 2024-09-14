my_dict = {'Ilya':2000, 'Arthur':1992}
print(my_dict)
print(my_dict.get('Arthur'))
my_dict.update({'Inna':1969, 'Eduard':1966})
s = my_dict.get('Ilya')
del my_dict['Ilya']
print(s)
print(my_dict)

my_set = {0, 4, 0, 4, 2, 0, 0, 0}
print(my_set)
my_set.add(10); my_set.add(40)
my_set.remove(2)
print(my_set)