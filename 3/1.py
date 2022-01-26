import time
start_time = time.time()
num=10000
def proper(num):
    _sum=0
    i=1
    j=num
    ragham=[]
    while(i<j-1):
        i+=1
        if num%i==0:
            #print('finddddddddddddddd',i)
            ragham.append(i)
            j=num/i
            ragham.append(j)
            #print(ragham)
            #print(_sum)
        else:
            continue
    ragham=list(set(ragham))
    _sum=sum(ragham)
    _sum+=1
    return _sum
prop=[]
for i in range (1,num):
    prop.append(proper(i))

result=0
prop=[0]+prop
for i in range(1,len(prop)):
    d1=proper(i)
    d2=proper(d1)
    if i==d2:
        if i!=d1:
            print(f"{i} and {d1} is ame")
            result+=i
            result+=d1
            #prop.pop(i)
            #prop.pop(
    else:
        continue


end_time = time.time()
#result=Amicable(2)
print(result/2)
print('The total time is: ',end_time-start_time)
