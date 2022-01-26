num=int(input('enter the number of votes: '))
vote=[]
for i in range(num):
    vote.append(input('enter the vote {}: '.format(i+1)))
num_m=set(vote)
num_m=list(num_m)
num_m.sort()
dic={}
for j in num_m:
    dic[j]=vote.count(j)
print(dic)
