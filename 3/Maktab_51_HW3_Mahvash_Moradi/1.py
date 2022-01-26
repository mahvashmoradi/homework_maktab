import time

start_time = time.time()
amicable = {}


###function for calculate SumOfDivisors
def getSumOfDivisors(n):
    divisors = [1]
    i = 2
    while n / i > i:
        if n % i == 0:
            divisors.append(i)
            divisors.append(n / i)
        i += 1
    return sum(divisors)


d = [0, 1]
for i in range(2, 10000):
    d.append(int(getSumOfDivisors(i)))
for a in range(2, 10000):
    b = d[a]
    try:
        if a == d[b] and a != d[a]:
            amicable[a] = True
            # print (a, d[a], d[b])
    except IndexError:
        pass

values = [key for key in amicable]
# print values
print(sum(values))
end_time = time.time()
print('The total time is: ', end_time - start_time)
