#Find Missing And Repeating: from gfg

arr = [1,3, 3,4,6,6,7,8,9,10,11,13,13,14,15,16]
l = len(arr)

for i in range(l-1):
    if arr[i] == arr[i+1]:
        print(arr[i]-1,i+1)
