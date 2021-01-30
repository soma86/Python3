# from gfg :Python Program for Product of unique prime factors of a number
def uniqueprimefactor(n):
    lst = []
    divisor = 2

    while divisor <= n:
        if n%divisor == 0:
            lst.append(divisor)
            n = n/divisor
        else:
            divisor+=1
    print(lst)
    listcnt = { key:lst.count(key) for key in lst}
    #print(listcnt)
    unqvals = []
    dupval = []
    for keys,val in listcnt.items():

        if val == 1:
            unqvals.append(keys)

        elif val == 2:
            dupval.append(keys)
    if len(unqvals) >1:
        return unqvals
    
    else:
        return dupval


lst = [105, 889674, 356478912, 30012, 121, 888088880]
for no in lst:
    print('unique values are',uniqueprimefactor(no))
