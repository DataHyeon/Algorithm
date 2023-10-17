def solution(sizes):
    for idx, size in enumerate(sizes):
        a, b = size
        
        if a < b:
            sizes[idx] = [b, a]
    
    a_list, b_list = zip(*sizes)
    a_max, b_max = max(a_list), max(b_list)
    
    answer = a_max * b_max
    
    
    return answer