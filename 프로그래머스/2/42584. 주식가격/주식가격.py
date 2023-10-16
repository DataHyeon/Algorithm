def solution(prices):
    answer = [0] * len(prices)  # 결과값을 저장할 리스트 초기화
    stack = []  # 시점의 인덱스를 저장할 스택

    for i, price in enumerate(prices):
        # 스택이 비어있지 않고, 스택의 최상단에 있는 가격이 현재 가격보다 클 때
        while stack and prices[stack[-1]] > price:
            j = stack.pop()  # 인덱스 pop
            answer[j] = i - j  # 결과값 저장
        stack.append(i)  # 현재 시점의 인덱스 push

    # 스택에 남아있는 인덱스 처리
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - j - 1

    return answer
