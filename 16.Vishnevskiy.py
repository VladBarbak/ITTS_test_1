def check(x):
    n=len(x)
    p=x[0]%2
    f=0
    for i in range(1,n):
         c=x[i]%2
         if (c==p):
            print('yes')
            f=1
            break
         p=c
    if (f==0):
       print('no')