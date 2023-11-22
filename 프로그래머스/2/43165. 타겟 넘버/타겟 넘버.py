from collections import deque

def solution(numbers, target):
    queue = deque([(0, 0)])  # (현재 인덱스, 현재까지의 합)
    count = 0

    while queue:
        idx, total = queue.popleft()
        
        # 모든 숫자를 다 사용한 경우
        if idx == len(numbers):
            if total == target:
                count += 1
        else:
            # 현재 숫자를 더하는 경우
            queue.append((idx+1, total+numbers[idx]))
            # 현재 숫자를 빼는 경우
            queue.append((idx+1, total-numbers[idx]))

    return count
