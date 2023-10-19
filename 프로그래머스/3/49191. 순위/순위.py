def solution(n, results):
    # 이긴 사람과 진 사람의 목록을 저장할 두 개의 딕셔너리를 초기화
    win, lose = {}, {}
    for i in range(1, n+1):
        win[i], lose[i] = set(), set()
    
    for i, j in results:
        # win: i가 j를 이겼다면
        # lose: j가 i에게 졌다면
        win[i].add(j) # i선수가 이긴사람들의 목록
        lose[j].add(i) # j선수를 이긴사람들의 목록
    
    for i in range(1, n+1):
        
        # i선수가 이긴사람
        for loser in win[i]:
            # i선수에게 진 선수의 패배 목록을 i선수에게 이긴 사람들의 목록으로 업데이트
            lose[loser].update(lose[i])
        # i선수를 이긴사람
        for winner in lose[i]:
            # i선수를 이긴 선수의 승리 목록을 i선수를 이긴 선수의 승리 목록을 i선수의 승리 목록으로 업데이트
            win[winner].update(win[i])
            
    print(win)
    print(lose)
    
    # 이긴 사람의 수와 진 사람의 수의 합이 n-1인 선수의 수를 세서 반환합니다.
    return len([1 for i in range(1, n+1) if len(win[i]) + len(lose[i]) == n-1])
