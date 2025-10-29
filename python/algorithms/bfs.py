import sys
from collections import deque

def bfs(u, adj, visited):
    q = deque()
    if u in adj:
        visited.add(u)
        q.append(u)
    while q:
        cur = q.popleft()
        print(cur, end=" ")
        
        neighbors = sorted(adj.get(cur, []))
        
        for v in neighbors:
            if v not in visited:
                visited.add(v)
                q.append(v)
def main():
    n, m = map(int, sys.stdin.readline().strip().split())
    adj = {i:[] for i in range(1, 1 + n)}
    
    for _ in range(m):
        x, y = map(int, sys.stdin.readline().strip().split())
        adj[x].append(y)
        adj[y].append(x)
    
    visited = set()
    for i in range(1, n + 1):
        if(i not in visited):
            bfs(i, adj, visited)
    
if __name__ == "__main__":
    main()