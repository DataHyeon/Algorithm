import heapq

def solution(jobs):
    # answer: 각 작업의 요청부터 종료까지 걸린 시간의 총합
    # now: 현재 시간
    # count: 현재까지 완료된 작업의 수
    # start: 직전에 처리한 작업이 시작된 시간, 아직 작업을 처리하지 않아 -1
    # head: 처리 대기 중인 작업 저장, 최소힙으로 사용
    answer, now, count = 0, 0, 0
    start = -1
    heap = []

    # 모든 작업을 처리할 때까지 반복
    while count < len(jobs):
        
        # 현재 시간 이전에 요청된 작업을 힙에 추가
        for job in jobs:
            if start < job[0] <= now:
                
                # 작업 시간을 기준으로 정렬
                # heappush에 들어가는 객체의 비교가능한 원소들의 첫번째 원소를 기준으로 정렬
                heapq.heappush(heap, [job[1], job[0]])
                
        # 처리할 작업이 있을 경우 진행
        if len(heap) > 0:
            
            # 작업 시간이 제일 적은 작업부터 처리
            current_job = heapq.heappop(heap)
            
            # 직전에 처리한 작업의 시작 시간을 현재 시간으로 설정
            start = now
            
            # 현재 시간을 해당 작업의 소요 시간만큼 증가
            now += current_job[0]
            
            # 해당 작업의 요청부터 종료까지 걸린 시간을 answer에 추가
            answer += (now - current_job[1])
            
            # 처리한 작업의 수 증가
            count += 1
            
        # 처리 대기 중인 작업이 없을 경우 현재 시간 증가
        else:
            now += 1

    return int(answer / len(jobs))
