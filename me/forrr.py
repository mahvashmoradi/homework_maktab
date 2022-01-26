for num in range (10,20):
    if num%2==0:
        continue
    for i in range (3,num):
        if num%i==0:
            break
    else:
        print(num, 'is a prime number')
