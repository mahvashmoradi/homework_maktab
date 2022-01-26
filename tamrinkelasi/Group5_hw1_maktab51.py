runners=input("enter names:").split(',')
for i in range(len(runners)):
    runners[i]=runners[i].strip()
runners=set(runners)
runners=list(runners)
runners.sort()
for i in range(len(runners)):
    print(i,runners[i])
dic={}
for i in runners:
    dic[i]=int(input(i+', enter your distance:'))
sorted_runners=sorted(dic.items(),key=lambda x:x[1],reverse=True)
print(sorted_runners)
for i in range(len(sorted_runners[:3])):
    print(i+1,sorted_runners[i][0],sorted_runners[i][1])

    
    
