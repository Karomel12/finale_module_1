my_dict = {'Denis': 2003, 'Anton': 2011, 'Alex': 1998}
print('Dict:',my_dict)
print('Existing value:',my_dict['Denis'])
print('Not existing value:',my_dict.get('Masha'))
my_dict.update({'Sasha': 2008,
'Nathasha': 1984})
print('Deleted value:',my_dict.pop('Alex'))
print('Modified dictionary:', my_dict)
print('  ')

my_set = {1,1,1,2,2,2,3,4,'Denis','Anthon',}
print('Set:',my_set)
my_set.add((332,323,332))
my_set.add(3213.123)
my_set.discard('Denis')
print('Modified set:',set(my_set))