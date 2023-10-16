# def solution(clothes):
#     answer = 0
    
#     c_dict = {c[1] : 0 for c in clothes}
#     for cloth, category in clothes:
#         c_dict[category] += 1
    
#     value_sum = 1
#     for cloth, value in c_dict.items():
#         answer += value
#         value_sum *= value
    
#     if len(c_dict) == 1:
#         return answer
#     else:
#         answer = answer + value_sum
    
#     return answer

def solution(clothes):
    from collections import defaultdict
    
    cloth_dict = defaultdict(int)
    
    for _, cloth_type in clothes:
        cloth_dict[cloth_type] += 1

    answer = 1
    for count in cloth_dict.values():
        answer *= (count + 1)
    
    return answer - 1