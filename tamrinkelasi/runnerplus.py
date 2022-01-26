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
    dic[factors[0]]=i
    dic[factors[1]]= int(input(i+', enter your distance in KM:'))
    dic[factors[2]]= float(input(i+', enter your duration in Minutes:'))
    dic[factors[3]]=dic[factors[1]]/(dic[factors[2]]/60)
    dic[factors[4]]= dic[factors[2]] / dic[factors[1]]
    if dic[factors[1]] < 10:
        continue
    elif dic[factors[1]]>=10 and dic[factors[1]]<21.0975:
        dic[factors[5]]='+10k'
    elif dic[factors[1]] >= 21.0975 and dic[factors[1]] < 42.195:
        dic[factors[5]] = 'half marathon'
    elif dic[factors[1]] >=42.195 and dic[factors[1]] < 60:
        dic[factors[5]]='marathon'
    else:
        dic[factors[5]]='ultra'

    lst.append(dic)
    dic=dict()
lst10k=[]
halfMarathon=[]
marathon=[]
ultra=[]
for j in lst:
    if j['class']=='+10k':
        lst10k.append(j)
    elif j['class']=='half marathon':
            halfMarathon.append(j)
    elif j['class']=='marathon':
            marathon.append(j)
    elif j['class']=='ultra':
            ultra.append(j)
#lst10k=[(i) for i in lst if lst['class']=='10K']
lst10k=sorted(lst10k,key=lambda x:x['speed'],reverse=True)
halfMarathon=sorted(halfMarathon,key=lambda x:x['speed'],reverse=True)
marathon=sorted(marathon,key=lambda x:x['speed'],reverse=True)
ultra=sorted(ultra,key=lambda x:x['speed'],reverse=True)
num=0
print('Class +10k ranking:')
for i in lst10k:
    if num<3:
        print(i['name'],i['speed'])
    num+=1
num=0
print('Class halfMarathon ranking:')
for i in halfMarathon:
    if num<3:
        print(i['name'],i['speed'])
    num+=1
num=0
print('Class Marathon ranking:')
for i in marathon:
    if num<3:
        print(i['name'],i['speed'])
    num+=1
num=0
print('Class ultra ranking:')
for i in ultra:
    if num<3:
        print(i['name'],i['speed'])
    num+=1
lst=sorted(lst,key=lambda x:x['speed'],reverse=True)
print('\nFastest runner: ',lst[0]['name'],lst[0]['speed'],'\n')
lst=sorted(lst,key=lambda x:x['distance'],reverse=True)
print('\nLongest distance: ',lst[0]['name'],lst[0]['distance'],'\n')
