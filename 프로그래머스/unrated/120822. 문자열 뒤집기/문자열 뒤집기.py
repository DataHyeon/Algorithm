def solution(my_string):
    answer = ''
    for i in reversed(list(my_string)):
        answer += i
    return answer