def solution(s):
        
    if s[0] != '(':
        return False
    
    i = 0
    for _ in list(s):
        if _ == '(':
            i += 1
        else:
            i -= 1
        
        if i < 0:
            return False
        
    if i == 0:
        return True
    else:
        return False
    
    