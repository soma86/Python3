#from gfg: Python Program for Find sum of odd factors of a number
def oddsum(n):
    lst = []

    for i in range(1,n):
        if n %i == 0 and i % 2 !=0:
            lst.append(i)
    print(lst)
    oddsumtotal = 0
    for i in lst:
        oddsumtotal += i
    print(n,'total sum of odd values is: ',oddsumtotal)

oddsum(54)
lst = [105,889674,35647,30012,121,888]
for no in lst:
    oddsum(no)
