from collections import Counter

def solution(array):
    counter = Counter(array)
    
    common_list = [k for k, v in counter.items() if v == max(counter.values())]
    
    answer = common_list[0] if len(common_list) == 1 else -1
    return answer