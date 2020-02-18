while True:
    v=int(input('Length of list(0-100):'))
    if v<0 or v>100:
        print('Incorrect number!')
        continue
    a=[v]
    for i in range(v):
        a.append(int(input(f'[{i}]:')))
    print(max(a)-min(a))
    print(max(a), min(a))
    print('Print 1 to close program or other button to rerun')
    k=input()
    if k == '1':
        break
    else:
        continue
    
            
