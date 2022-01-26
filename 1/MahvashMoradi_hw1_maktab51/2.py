def sum_d(x):
    sumd=0
    while(x!=0):
        sumd+=x%10
        x=int(x/10)

    return(sumd)
x=input('enter your string:').split('+')
for i in range (len(x)):
	x[i]=x[i].strip()
x.sort()
x="".join(x)
print(x)
x=int(x)
print(sum_d(x))
