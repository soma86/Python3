#problem from gfg :  Convert a list of Tuples into Dictionary

inp = [("akash", 10), ("gaurav", 12), ("anand", 14),
         ("suraj", 20), ("akhil", 25), ("ashish", 30)]

s1 = [i[0] for i in inp]# for x[0] in range(len(i))]
s2 = [[i[1]] for i in inp]
print(s1,s2)
#1:
dd = dict(zip(s1,[i for i in s2]))
print(dd)
#2:
d1 = dict (zip(s1,s2))
print(d1)
#3:
d2 = dict(zip((i[0] for i in inp), ([i[1]] for i in inp)))
print(d2)
