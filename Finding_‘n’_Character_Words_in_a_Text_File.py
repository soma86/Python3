#Python | Finding ‘n’ Character Words in a Text File | from gfg:
charlen = int(input('enter length: '))
with open('test2.txt','r') as df:
    nchars = df.readlines()
    for i in nchars:
        for j in i.split():
            if len(j)==charlen:
                print(j)
