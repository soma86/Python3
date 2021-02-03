#Pythagorean Triplet in an array: from gfg

n = 1
arr = [3, 2, 4, 6, 5]
l = len(arr)
for i in range(l):
    for j in range(i+1,l):
        if pow(i,2)+pow(j,2) == pow(j+1,2):
            print('yes',pow(i,2),pow(j,2),pow(j+1,2))
