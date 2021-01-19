#Program from gfg: Python – Remove Tuples of Length K
test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
k = 2
#1:
lst =[]
for i in test_list:
    if len(i) != k:
        lst.append(i)
print(lst)
#2:
lst1 = [i for i in test_list if len(i) != k]
print(lst1)
#3:
for i in test_list:
    if len(i) == k:
        test_list.remove(i)

print(test_list)
