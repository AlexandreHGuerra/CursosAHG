import random
#import 

nl = int(input("informe o numero de elementos"))

if nl < 1 or nl > 101 :
    print("erro")

lstnum = [ random.randint(1,1000) for xx in range(nl) ]
print("---")
print(lstnum)
while True:
    swap = False
    for ct in range(nl - 1) :
        if lstnum[ct] > lstnum[ct+1] :

            num=lstnum[ct+1]
            lstnum[ct+1] = lstnum[ct]
            lstnum[ct] = num
            swap = True

    if not swap : break
print(lstnum)