#from gfg:
#Python program to Count the Number of occurrences of a key-value pair in a text file

lst = []
with open('test3.txt','r') as df:
    samba = df.readlines()
    for j in samba:
        j = j.strip()
        lm = j[len(j)-1]
        lst.append(lm)

print(lst)
dict = {key:lst.count(key) for key in lst}
print(dict)
for key,values in dict.items():
    print('num of {0} in file is: {1}'.format(key,str(values)))
