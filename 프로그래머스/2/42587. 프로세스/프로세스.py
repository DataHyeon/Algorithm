def solution(priorities, location):
    # (중요도, 원래 인덱스) 쌍을 원소로 가진 리스트 생성
    p_idx_list = [(p, idx) for idx, p in enumerate(priorities)]
    
    answer = 0
    while p_idx_list:
        cur = p_idx_list.pop(0)
        # 현재 항목의 중요도가 나머지 항목들 중 최대 중요도보다 작다면
        if any(cur[0] < item[0] for item in p_idx_list):
            p_idx_list.append(cur)
        else:
            answer += 1
            if cur[1] == location:
                break
    return answer
