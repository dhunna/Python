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
