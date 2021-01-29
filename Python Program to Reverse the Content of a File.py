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


INPUT:
    ['i am somasree biswas\n', 'i live in pune.\n', 'Pune is in india\n', 'my # is 9881045030\n', 'eg. email is soma.biswas#123@gmail.com\n', 'welcome to my world.\n', 'i love goa.\n']
OUTPUT:
i love goa.

welcome to my world.

eg. email is soma.biswas#123@gmail.com

my # is 9881045030

Pune is in india

i live in pune.

i am somasree biswas
