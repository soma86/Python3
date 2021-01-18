#problem from gfg; Python | Remove all duplicates words from a given sentence
inps = 'Python is great and Java is also great'#'Geeks for Geeks'

lst = list(inps.split())
print(lst)

dis = {key : inps.index(key)  for key in lst}
lst1 = []
lst2=[]
for k in dis.keys():
    lst2.append(k)
    if k not in lst1:
        lst1.append(k)
print(dis,lst1,'\n',lst2)

