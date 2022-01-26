contestants=input("enter names:").split('*')
contestants=list(map(lambda x:x.split(","),contestants))
teams=[]
for contestant in contestants:
    teams.append(list(map(lambda x:x.strip(),contestant)))
runners=list()
for i in range(len(teams)):
     for j in range(len(teams[i])):
         runners.append(teams[i][j].strip())
runners=set(runners)
runners=list(runners)
runners.sort()
for i in range(len(runners)):
     print(i+1,runners[i])

################################################# get information about every runner ###########################
     
dic={}
lst=[]
for i in runners:
     dic['name']=i
     dic['distance']= int(input(i+', enter your distance in KM:'))
     dic['duration']= float(input(i+', enter your duration in Minutes:'))
     dic['speed']=dic['distance']/(dic['duration']/60)
     dic['pace']= dic['duration'] / dic['distance']
     if dic['distance'] < 10:
         continue
     elif dic['distance']>=10 and dic['distance']<21.0975:
         dic['class']='+10k'
     elif dic['distance'] >= 21.0975 and dic['distance'] < 42.195:
         dic['class'] = 'half marathon'
     elif dic['distance'] >=42.195 and dic['distance'] < 60:
         dic['class']='marathon'
     else:
         dic['class']='ultra'

     lst.append(dic)
     dic=dict()

'''teams=[['a', 'b'], ['c', 'd'], ['e', 'f']]
lst=[{'name': 'a', 'distance': 120, 'duration': 5.0, 'speed': 144.0, 'pace': 0.4166666666666667, 'class': '+10k'},
     {'name': 'b', 'distance': 23, 'duration': 12.0, 'speed': 115.0, 'pace': 0.5217391304347826, 'class': 'half marathon'},
     {'name': 'c', 'distance': 34, 'duration': 11.0, 'speed': 185.45454545454547, 'pace': 0.3235294117647059, 'class': 'half marathon'},
     {'name': 'd', 'distance': 260, 'duration': 14.0, 'speed': 111.42857142857143, 'pace': 0.5384615384615384, 'class': 'half marathon'},
     {'name': 'e', 'distance': 37, 'duration': 56.0, 'speed': 39.64285714285714, 'pace': 1.5135135135135136, 'class': 'half marathon'},
     {'name': 'f', 'distance': 69, 'duration': 56.0, 'speed': 73.92857142857143, 'pace': 0.8115942028985508, 'class': 'ultra'}]
'''
################################################# calculate average speed  ###########################

sum_t=0
average_speed=dict()
t=0
for team in teams:
    counter = 0
    for i in lst:
        if i['name'] in team:
        #lambda x:
            sum_t+=i['speed']
            counter+=1
    average_speed[t]=sum_t/counter
    t+=1
    #average_speed.append(sum_t/counter)
    sum_t=0
print('\n*************team_result(average_speed)***********\n')

for i in range( len(teams)):
        print(teams[i],'average speed: ', average_speed[i])
        
################################################# calculate total distance  ###########################

total_distance=dict()
sum_d=0
t=0
for team in teams:
    for i in lst:
        if i['name'] in team:
            sum_d+=i['distance']
    total_distance[t]=sum_d
    t+=1
    #total_distance.append(sum_d)
    sum_d=0
#print(total_distance)
print('\n*************team_result(total_distance)***********\n')
for i in range(len(teams)):
        print(teams[i],'total distance: ', total_distance[i])
        
################################################# determine leader  #################################

sorted_teams=[]
for team in teams:
    list_team=[]
    for i in lst:
        if i['name'] in team:
            list_team.append(i)
    sorted_teams.append(list_team)      
#print(sorted_teams)

sorted_list=[]
for i in sorted_teams:
    sorted_list.append(sorted(i, key=lambda i:i['speed'],reverse=True))
#print(sorted_list)
print('\n*************team_result(leader)***********\n')
for team in teams:
    for i in sorted_list:
        if i[0]['name'] in team:
            print(team,'leader: ', i[0]['name'])
            
################################################# determine top 3 teams  ###########################

s=sorted(total_distance,key=lambda x:total_distance[x],reverse=True)
counter=0
print('\n*************top 3 teams base on total distance ***********\n')
for i in s:
     if counter <3:
         print('team',teams[i],':',total_distance[i])
         counter+=1
         
