#z=int(input())

def searth(n):
    ls=[]
    for i in range(2,n):
        if n%i==0:
            ls.append(i)
 #   print(ls)
    return ls
#searth(z)

