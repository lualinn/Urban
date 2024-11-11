my_dict = {'Natalie': 2000, 'Lera': 2008}
print(my_dict)
print(my_dict['Natalie'], my_dict.get('Oxana'))
my_dict.update({'Oxana': 1987,
               'Marina': 1960})
print(my_dict)
print(my_dict.pop('Marina'))
print(my_dict)
my_set = {1, 2, 3, 'apple', 'banana', 1, 2, 'apple', 3.5, True, False, None}
print("Первоначальное множество my_set:", my_set)
my_set.add('orange')
my_set.add(10)
my_set.discard(1)
print("Измененное множество my_set:", my_set)
