#problem from gfg: Python – Append Dictionary Keys and Values ( In order ) in dictionar
#1:
test_dict = {'Gfg' : 1, 'is' : 2, 'Best' : 3}

keys = [key for key in test_dict.keys()]
valus = [val for val in test_dict.values()]
print(keys+valus)

#2:
test_dict = {'Gfg' : 1, 'is' : 2, 'Best' : 3}
dicts = list(test_dict.keys()) + list(test_dict.values())
print(dicts)

#3. using chain
from itertools import chain
test_dict= {'Gfg' : 1, 'is' : 2, 'Best' : 3}
result = list(chain(test_dict.keys(),test_dict.values()))
print(result)
