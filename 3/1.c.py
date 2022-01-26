def getSumOfDivisors(n):
    divisors = [1]
    i = 2
    while n / i > i:
        if n % i == 0:
          divisors.append(i)
          divisors.append(n/i)
        i += 1
    return sum(divisors)

