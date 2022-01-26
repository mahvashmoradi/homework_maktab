import math
def isPrime(n):
    if n<2:
        return False
    if n%2==0:
        return False
    if n%3==0:
        return False
    h = math.floor(1 + math.sqrt(n))
    i = 5
    #print('5')
    while i<=h:
        if n%i==0:
            return False
        if n%(i+2)==0:
            return False
        i+= 1
    return True


def solution(L):
    c = 2
    n = 6

    while n<L:
        
        if (isPrime(n + 1)):
            c+=1
        
        if (isPrime(n - 1)):
            c+=1
        n+= 6

#  // Add one for the final prime being of the form 6k + 1
    return c

print(solution(10001))
