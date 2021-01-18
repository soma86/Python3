#python program in gfg: Python Counter to find the size of largest subset of anagram words

strs = ['ant', 'magenta', 'magnate', 'tan','gnamate']

dis = {key: len(key) for key in strs}
print(dis)
z = dis['ant']
for val in dis.values():
    if val > z:
        z = val
print(z,'x')
lst2 = []
for key,val in dis.items():
    if val == z:
        lst2.append(key)
print(len(lst2))
