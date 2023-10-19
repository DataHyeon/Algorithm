from collections import deque

def solution(n, wires):
    # 그래프 생성
    graph = {i: [] for i in range(1, n+1)}
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    # BFS 함수 정의
    def bfs(start, graph):
        queue = deque([start])
        visited = set([start])
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return count

    answer = n
    for a, b in wires:
        # 전선 제거
        graph[a].remove(b)
        graph[b].remove(a)

        # 두 서브그래프의 노드 수 차이 계산
        count1 = bfs(a, graph)
        count2 = n - count1
        answer = min(answer, abs(count1 - count2))

        # 전선 복원
        graph[a].append(b)
        graph[b].append(a)

    return answer
