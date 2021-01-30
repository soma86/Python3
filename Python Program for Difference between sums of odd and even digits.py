#from gfg:Python Program for Difference between sums of odd and even digits

no = 1212112

def inpsum(no):
    sum = 0
    lstodd =[]
    lsteven = []
    n = []
    while no >= 1:
        x = no % 10
        n.append(x)
        no = no // 10
    print(n)
    n = n[len(n)::-1]
    print(n)

    for i in range(len(n)):
        if i == 0 or i %2==0:
            lsteven.append(n[i])
        else:
            lstodd.append(n[i])

    print(lstodd,lsteven)
    oddsum = 0
    evensum =0
    for k in lstodd:
        oddsum +=k
    for l in lsteven:
        evensum +=l
    print(abs(evensum-oddsum), 'is the diff.')

inpsum(no)
