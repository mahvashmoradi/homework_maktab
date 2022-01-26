Balance=0
while(True):
    value=input('enter deposit with D and withdrawal with W: ')
    if value=='-1':
        break
    else:
        WorD=value[0]
        if WorD=='W':
            Balance-=int(value[1:])
        elif WorD=='D':
            Balance+=int(value[1:])
        else:
            print('wrong input')
            break
print(Balance)
