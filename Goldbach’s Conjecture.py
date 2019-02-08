def isPrime(n):
    if (n<2):
        return False
    for i in range (2,int(n**0.5)+1):
        if (n%i==0):
            return False
    return True


def primepartition(m):
  if(m==2 or m==3 or m<=0):
    return False
  elif(m%2==0):
    return True
  elif(isPrime(m-2)):
    return True
  else:
    return False



    
    
