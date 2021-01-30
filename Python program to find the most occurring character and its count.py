#Python program to find the most occurring character and its count; from gfg:
strs = 'hello'
lstdict ={i:strs.count(i) for i in strs}
print(lstdict)
x = strs[0]

y = lstdict[x]
for key,val in lstdict.items():
    if y < val:
        x = key
        y = val

print(x,y)
