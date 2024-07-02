my_dict = {'Anton': 1998, 'Max': 2004 }
print('Dict:',my_dict)
print('Existing value:', my_dict['Anton'])
my_dict['Eva']= 1995
print('Not existing value:',my_dict.get('Masha'))
my_dict['Artem']= 2000
my_dict['Vas']= 2001
del my_dict['Max']
print('Deleted value:', 2004)
print('Modified dictionary:',my_dict)
my_set = {1,11,'Bom',1,39,42.3,39,'Bom'}
print('Set:',my_set)
print(my_set.add(5))
print(my_set.add(25))
print(my_set)
print(my_set.discard(1))
print('Modified set', my_set)