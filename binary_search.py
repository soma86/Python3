#binary search: from gfg
arr = [ 2, 3, 4, 10, 40 ]
x = 3

def binser(arr,x):
    y = arr[len(arr)//2]

    if x == y:
        print(x, 'is at location: ' ,arr.index(y))

    elif x > y:
        ars = [arr[r] for r in range(len(arr)//2,len(arr))]
        if len(ars) >= 1:
            binser(ars,x)

    else:
        ars = [arr[r] for r in range(0,len(arr)//2)]
        if len(ars)>=1:
            binser(ars,x)

binser(arr,x)
