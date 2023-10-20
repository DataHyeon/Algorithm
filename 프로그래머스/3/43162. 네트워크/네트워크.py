from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0] * n
    graph = [[] for _ in range(n)]
    
    # 그래프 형성
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
                
    def bfs(start):
        queue = deque([start])
        visited[start] = 1
        
        while queue:
            node = queue.popleft()
            for next_node in graph[node]:
                if not visited[next_node]:
                    visited[next_node] = 1
                    queue.append(next_node)

    # 모든 컴퓨터에 대해서 방문하지 않았다면 BFS를 통해 네트워크 탐색
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1

    return answer
