def solution(numbers):
    answer = ''
    
    numbers = sorted(list(map(str, numbers)), key = lambda x:x*3, reverse=True)
    
    answer = str(int(''.join(numbers)))
    
    return answer