def solution(brown, yellow):
    total = brown + yellow
    
    return_list = []
    for i in range(total, 0, -1):
        if total % i == 0 and i >= total // i and i < brown and total // i > 2 and i * 2 < brown and brown == i * 2 + ((total // i) - 2) * 2:
            return_list = [i, total // i]
    
    return return_list
    
    # if len(return_list) == 1:
    #     answer = return_list[0]
    # else:
    #     pass
        
        
    # return answer