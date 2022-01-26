x=input('enter your string:')
vovel=['A','a','e','E','o','O','u','U','i','I']
for i in vovel:
    x=x.replace(i,'.')
x=x.lower()
print(x)
