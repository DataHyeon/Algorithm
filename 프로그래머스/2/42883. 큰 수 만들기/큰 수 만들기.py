def solution(number, k):
    stack = []
    for num in number:
        # 처음 들어가는 숫자는 제외, 제외할 횟수가 남아있는 경우에만 실행
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)

    # k가 남아있는 경우 끝에서부터 제거
    if k != 0:
        stack = stack[:-k]

    return ''.join(stack)