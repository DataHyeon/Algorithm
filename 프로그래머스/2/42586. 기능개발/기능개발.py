def solution(progresses, speeds):
    answer = []
    comp_list = []
    for p, s in zip(progresses, speeds):
        
        d = 1
        while True:
            p += s
            d += 1
            
            if p >= 100:
                break
    
        comp_list.append(d)
    
    idx = 0
    for comp in comp_list:
        if not answer:
            answer.append([1,comp])
            continue
        
        if comp <= answer[idx][1]:
            answer[idx][0] += 1
        
        else:
            idx += 1
            answer.append([1,comp])
    
    answer = list(map(lambda x : x[0], answer))
        
        
        
    
    
    
    return answer