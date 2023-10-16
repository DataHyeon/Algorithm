from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 다리 위의 상황을 나타내는 큐 초기화
    on_bridge = deque([0] * bridge_length)
    answer = 0
    truck_weights = deque(truck_weights)
    on_bridge_sum = 0
    
    while on_bridge:
        answer += 1 # 1초 증가
        on_bridge_sum -= on_bridge.popleft() # 다리의 맨 앞에 있는 트럭이 빠져나감
        
        # 아직 대기 중인 트럭이 있을 경우
        if truck_weights:
            # 대기 중인 첫 번째 트럭과 다리 위의 트럭 무게의 합이 weight보다 작거나 같을 경우
            if on_bridge_sum + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                on_bridge.append(truck)
                on_bridge_sum += truck
            else:
                on_bridge.append(0) # 무게 초과로 트럭이 못 올라옴, 그 시간에 비어있는 공간으로 생각
                
    return answer
