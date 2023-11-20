def solution(n, s):
    
    if s < n:
        return [-1]
    
    value = s // n
    remainder = s % n
    
    best_set = [value] * n
    for i in range(remainder):
        best_set[i] += 1
        
    best_set.sort()
    
    return best_set
    
    
    return answer