import heapq

def solution(scoville, K):
    answer = 0
    
    # 리스트를 최소힙을 만족하게 변환
    # 최소힙 객체가 되는 거는 아님
    heapq.heapify(scoville)
    
    # 스코빌 지수를 계산하기 위해서 노드가 2개 이상 필요
    # 루트 노드가 기준 스코빌보다 작아야함 -> 최소 힙 성질 사용
    while len(scoville) > 1 and scoville[0] < K:
        # 최소 노드(루트 노드)를 반환
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        
        # 새로운 스코빌 지수 계산
        new_scoville = min1 + (min2 * 2)
        
        # 최소힙이 적용된 리스트에 추가
        # 최소힙이 적용된 리스트로 반환
        heapq.heappush(scoville, new_scoville)
        
        answer += 1
        
        # if scoville[0] < K and len(scoville) == 1:
        #     return -1
        
    # 힙의 루트 노드가 기준치보다 작을 경우
    if scoville[0] < K:
        return -1
    
    return answer