#Maximum Index: from gfg

arr = [34, 8, 10, 3, 2, 80, 30, 33, 1,15,16]
arr1=   [34, 8, 10, 3, 2, 80, 30, 33, 1]

def welcome(arr,l,m):
    i = 0
    j = l - 1
    while i < m and j > m:
        if arr[i] < arr[j]:
            print(arr[i],arr[j])
            md = j - i
            break
        i += 1
        j -= 1
    print(md)

welcome(arr,len(arr),len(arr)//2)
welcome(arr1,len(arr1),len(arr1)//2)

#>>https://practice.geeksforgeeks.org/problems/maximum-index-1587115620/1
