res=1
m=int(input('m='))
if 0<m<=20:
    if m%2==0:
        for m in range(2,m+1,2) :
            res*=m
        print(res)
    else :
        for m in range(1,m+1,2) :
            res*=m
        print(res)
else :
    print('Невірний діапазон')