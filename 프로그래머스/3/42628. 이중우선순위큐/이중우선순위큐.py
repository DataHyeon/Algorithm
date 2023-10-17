import heapq
def solution(operations):
    answer = []
    
    heap = []
    now = None
    
    while operations:
        for operation in operations:
            
            if "I" in operation:
                insert_num = int(operation[2:])
                heapq.heappush(heap, insert_num)
            
            elif "D" in operation:
                heapq.heapify(heap)
                
                if not heap:
                    continue
    
                elif "-" not in operation:
                    heap = [-x for x in heap]
                    heapq.heapify(heap)
                    heapq.heappop(heap)
                    heap = [-x for x in heap]

                else:
                    heapq.heappop(heap)
        
        if len(heap) == 0:
            return [0,0]
        
        else:
            return [max(heap), min(heap)]
        
        