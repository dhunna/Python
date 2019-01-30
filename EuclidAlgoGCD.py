def EuclidAlgoGCD(m,n):
  if(m<n):
    (m,n)=(n,m)
    return(EuclidAlgoGCD(m,n))
  else:
    if(n==0):
     return(m)
    elif(m%n==0):
     return(n)
    else:
     return(EuclidAlgoGCD(n,m%n))
