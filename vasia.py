z=int(input())

def searth(n):
    ls=[]
    for i in range(2,n):
        if n%i==0:
            ls.append(i)
    return ls
print(searth(z))

