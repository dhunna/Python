def rotatelist(l,k):
 return l[k % len(l):] + l[:k % len(l)]
