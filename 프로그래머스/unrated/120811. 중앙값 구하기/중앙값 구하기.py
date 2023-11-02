def solution(array):
    array.sort()
    mid_idx = int(len(array) / 2)
    
    answer = array[mid_idx]
    return answer