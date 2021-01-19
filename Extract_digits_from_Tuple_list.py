#Program from gfg: Extract digits from Tuple list

test_list = [(15, 3), (3, 9)]
lst = []
lst1 = []
def creatinglst(test_list,lst1):
    for i in list(test_list):
        for j in i:
            lst1.append(j)



def listres(lst,lst1):
    for j in lst1:
        print(j)
        if j < 10 and j not in lst:
            lst.append(j)

        elif j>9:
            if (j>=0):
                x= j%10
                a = j // 10
                if a not in lst or x not in lst:
                    lst.append(x)
                    lst.append(a)
                    print(a,x,'k')

creatinglst(test_list,lst1)
listres(lst,lst1)
print(lst1)
print(lst)
