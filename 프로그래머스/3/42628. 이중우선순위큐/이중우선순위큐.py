import heapq
def solution(operations):
    
    heap = []
    
    for operation in operations:
        
        # 추가하는 부분            
        if "I" in operation:
            insert_num = int(operation[2:])
            
            # 힙 푸시할 경우 자동으로 최소힙 특성 적용
            heapq.heappush(heap, insert_num)
        
        # 삭제하는 부분
        elif "D" in operation:
            
            # 최소힙으로 변환 후 아래 연산
            heapq.heapify(heap)
            
            # 힙이 비어 있으면 operations에서 원소 검사 후 재연산
            if not heap:
                continue
            
            # 최댓값 삭제
            elif "-" not in operation:
                
                # 모든 원소에 - 기호를 붙이고 최소힙으로 재변환
                heap = [-x for x in heap]
                heapq.heapify(heap)
                
                # 최댓값 삭제 이후 - 기호를 다시 붙이고 최소힙으로 재변환
                heapq.heappop(heap)
                heap = [-x for x in heap]
            
            # 최솟값 삭제
            else:
                heapq.heappop(heap)
    
    # 힙이 비어있는 경우
    if len(heap) == 0:
        return [0,0]
    
    # 아닌 경우
    else:
        return [max(heap), min(heap)]

