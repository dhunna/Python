def matched(s):
    depth = 0
    for char in s:
        if char == ')':
            depth -= 1
            if depth < 0:
                return False
        elif char == '(':
            depth += 1
    if(depth == 0):
      return True
    else:
      return False


def nestingdepth(s):
    depth = 0
    maxDepth=1
    count=0
    for char in s:
        if char == ')' or char == '(':
            count+=1
            break
    if(count==0):
      return 0
    elif(matched(s)):
      for char in s:
        if char == ')':
            depth -= 1
        elif char == '(':
            depth += 1
        if(maxDepth<depth):
            maxDepth=depth
      return maxDepth
    else:
      return -1
