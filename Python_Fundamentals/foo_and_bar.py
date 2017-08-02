##### Foo and Bar ######   Incomplete
# Write a program that prints all the prime numbers
# AND all the perfect squares for all numbers between 100 and 100000
# If it is prime print "Foo"
# If it is a perfect square print "Bar"
# If it is neither print "FooBar"

def isPrime(n,start,stop):
    if (n < 2):   # 0 and 1 are not prime, so we can take care of those cases
        return False
    if (n == 2):
        return True # 2 is the first prime number
    if not (n & 1): # Che
        return False
    for x in range(start,stop):
        if (n % x == 0):
            return False
    return True

def isPerfectSquare(n):
    x = n
    y = set([x])
    while x * x != n:
        x = (x+(n//x))//2
        if x in y:
            return False
        y.add(x)
    return True


def FooBar(start,stop):
    for n in range(start,stop):
        if isPrime(n,start,stop):
            print "Foo"
        elif isPerfectSquare(n):
            print "Bar"
        else:
            print "FooBar"

FooBar(100,10000)
