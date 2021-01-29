#from gfg: Python Program to Reverse the Content of a File
import os
lst = []
with open('test2.txt', 'r') as rf:
    rd1 = rf.readlines()
    for i in rd1:
        lst.append(i)


print(lst)
lst = lst[::-1]
with open('test3_copy.txt', 'w') as rf2:
    for j in lst:
        rf2.write(j)
with open('test3_copy.txt', 'r') as rf2:
    rd2 = rf2.readlines()
    for i in rd2:
        print(i)

os.remove('test3_copy.txt')
