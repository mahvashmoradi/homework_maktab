x=input('enter your string:')
vovel=['A','a','e','E','o','O','u','U','i','I']
for i in range(0,len(x)):
      for j in vovel:
          if x[i]!=j:
              continue
          else:
                print(x[i])
                x=x[:i]+'.'+x[i+1:]
                break
           #print(x)   
print(x)
        
