def solution(n, times):
    # 최소로 걸리는 시간 모름 -> 1로 설정
    min_time = 1
    
    # 최대로 걸리는 시간은 제일 오래 걸리는 심사대 * 사람 수
    max_time = max(times) * n
    
    # 최소 시간이 최대 시간보다 작을 때까지 반복
    while min_time < max_time:
        
        # 중간 시간 계산, 최신화 작업
        mid_time = (min_time + max_time) // 2
        
        # 구해 놓은 중간 시간에 처리 가능한 인원 확인
        total_people = sum(mid_time // time for time in times)
        
        # 처리 가능한 인원이 처리 할 인원보다 적을 경우
        # 최소 시간 증가 -> 중간 시간 증가시켜서 처리 가능한 인원 증가
        if total_people < n:
            min_time = mid_time + 1
        
        # 처리 가능한 인원이 처리 할 인원보다 많을 경우
        # 최대 시간 감소 -> 중간 시간 감소시켜서 처리 가능한 인원 감소
        else:
            max_time = mid_time
    
    
    return min_time