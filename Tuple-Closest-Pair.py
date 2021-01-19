# problem from gfg; tupple: Python – Closest Pair to Kth index element in Tuple
test_list = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]
tup = (17, 23)
k=2
#print(tup[k-1])
def closestpair(test_list,tup,k):
    for i in test_list:
        for j in range(len(i)):
            if i[j] == tup[k-1]:
                    print(i)
            
closestpair(test_list,tup,k)
