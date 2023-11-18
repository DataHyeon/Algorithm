import heapq

def solution(n, works):
    # 모든 작업량의 부호를 바꿔 최소 힙 생성
    works = [-work for work in works]
    heapq.heapify(works)

    # n 시간 동안 작업 진행
    for _ in range(n):
        if works:
            max_work = heapq.heappop(works)
            # 작업량이 이미 0인 경우 더 이상 진행하지 않음
            if max_work == 0:
                break
            # 작업량 감소
            heapq.heappush(works, max_work + 1)  # 부호가 바뀌었으므로 +1

    # 야근 피로도 계산 (부호가 바뀌었으므로 -를 붙여서 원래의 값으로 계산)
    return sum(work ** 2 for work in works)