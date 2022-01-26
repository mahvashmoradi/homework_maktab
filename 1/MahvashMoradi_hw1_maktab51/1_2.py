x=input('enter your string:')
vovel=['A','a','e','E','o','O','u','U','i','I']
y=x
k=0
for i in range(0,len(x)):
      for j in vovel:
          if x[i]!=j:
              continue
          else:
               y = y.replace(j,'')
               break
      else:
            #print('biseda',x[i])
            k=y.find(x[i],k)
            #print(k)
            y=y[:k]+'.'+y[k:]
            #print(y)
y=y.lower()
print(y)
        
