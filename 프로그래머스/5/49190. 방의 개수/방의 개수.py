def solution(arrows):
    # 8 방향 정의
    move = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    
    cur_pos = (0,0)
    visited_nodes = {cur_pos}
    visited_edges = set()
    rooms = 0

    for arrow in arrows:
        for _ in range(2):  # 2번씩 체크하여 대각선 움직임에 대한 예외처리 해결
            next_pos = (cur_pos[0] + move[arrow][0], cur_pos[1] + move[arrow][1])

            # 방이 형성되는 경우 확인
            if next_pos in visited_nodes and (cur_pos, next_pos) not in visited_edges:
                rooms += 1
                
            visited_nodes.add(next_pos)
            visited_edges.add((cur_pos, next_pos))
            visited_edges.add((next_pos, cur_pos))  # 양방향 모두 체크
            cur_pos = next_pos

    return rooms
