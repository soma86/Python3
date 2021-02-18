#from gfg- Longest Palindrome in a String:
sts = 'aaaabbaa'

stslst = [sts[i:j] for i in range(len(sts)) for j in range(i+1,len(sts)+1)]
length = len(stslst)
#print(stslst)


dict2 = {key:len(key) for key in stslst}
#print(dict2)
def dictvals(dict2,sts):
    lsts = []
    din ={}
    for key, val in dict2.items():
        if key[0:len(key):1] == key[len(key)::-1]:
            #print('val',key)
            lsts.append(key)

    #print(lsts)
    dicts = {i:len(i) for i in lsts}
    #print(dicts)
  
    longstr = max(dicts,key = dicts.get)
    print (longstr,len(longstr))

dictvals(dict2,sts)
