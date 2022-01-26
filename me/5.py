categorize=lambda x:'not finisher' if x<10 \
                else '10k' if (x>=10 and x<21.0975) \
                else 'half_marathon' if (x>=21.0975 and x<42.195) \
                else 'marathon' if (x>=42.195 and x<60) \
                else 'ultra'


def ranking(member_list, metric , count=None):
    member_list=sorted(member_list,key=lambda k:k[metric],reverse=True)
    return member_list[:count]


### inplace
def set_record(runner_inform):
    runner_inform['speed']=runner_inform['distance']/runner_inform['duration']/60
    runner_inform['pace']=runner_inform['duration']/runner_inform['distance']
    runner_inform['class']=categorize(runner_inform['distance'])
### return
def set_record_2(distance, duration):
    speed= distance/duration/60
    pace= duration/distance

    category=categorize(distance)
    return {'speed':speed,'pace':pace,'category':category}

{'10k': [{'name': 'nora', 'distance': 12.0, 'speed': 0.0016260162601626016}], 'half_marathon': [], 'marathon':
 [{'name': 'yas', 'distance': 43.0, 'speed': 0.0016589506172839505}], 'ultra': []}
runners=list(map(lambda x:x.strip(),input("enter names:").split(',')))
runners=sorted(set(runners))
print(runners)
runners_list=[]

for i in range(len(runners)):
    information=dict()
    information['id']=i+1
    information['name']=runners[i]
    information['distance']=float(input(f"{runners[i]} enter distance"))
    information['duration']=float(input(f"{runners[i]} enter duration"))
    set_record(information)
    print(set_record_2(information['distance'],information['duration']))
    runners_list.append(information)
    
print(ranking(runners_list, 'speed',1))
print(ranking(runners_list, 'distance',1))
print(ranking(runners_list, 'speed'))

category=['10k','half_marathon','marathon','ultra']
categorized_runners=dict()
for group in groups:
    categorized_runners[group]=[info for info in runners_list if info['class']==group]

