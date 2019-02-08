def isPrime(n):
    if (n<2):
        return False
    for i in range (2,int(n**0.5)+1):
        if (n%i==0):
            return False
    return True


def sumprimes(l):
 total = 0
 for x in l:
      if isPrime(x):
         total += x

 return total