my_dict = {'Natalie': 2000, 'Lera': 2008}
print(my_dict)
print(my_dict['Natalie'], my_dict.get('Oxana'))
my_dict.update({'Oxana': 1987,
               'Marina': 1960})
print(my_dict)
print(my_dict.pop('Marina'))
print(my_dict)