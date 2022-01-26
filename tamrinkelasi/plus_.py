runners=input("enter names:").split(',')
for i in range(len(runners)):
    runners[i]=runners[i].strip()
runners=set(runners)
runners=list(runners)
runners.sort()
for i in range(len(runners)):
    print(i,runners[i])
factors=['name','distance','duration','speed','pace','class']

dic={}
lst=[]

for i in runners:
