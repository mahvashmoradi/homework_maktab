result=[]

dic={}
dic_reverse={}
runner= input('enter name:').split(',')
for i in range (len(runner)):
	runner[i]=runner[i].strip()
print(runner)
runner=list(set(runner))
#print(runner)
runner.sort()
for i in range(len(runner)):
    print(i , runner[i])
for i in runner:
    dic[i]=int(input('enter the distance for '+i+' '))
print('names and records:' ,dic)
for i,j in dic.items():
	dic_reverse[j]=i
maghadir=dic.values()
val=list(maghadir)
val.sort()
for i in range(-1,-4,-1):
        a=dic_reverse[val[i]]+':'+str(val[i])
        result.append(a)


print(result)
