import sys
import heapq

# problem : find the shortest path from source vertex to others
# idea : 
# build a adjacent list of all vertexs and a distance list to contain the distance from source vertex to the others
# using minheap(heapq) to take out the min element to the next vertex
# cross over all of neighbours of top element
# check if dist[v] > dist[u] + w ? push to heap : skip
# optional : skip outdated elements : check if dist[u] != du ?

INF = int(1e9)
input = sys.stdin.readline

def dijkstra(src, n, adj):
    dist = [INF] * (n + 1) # distance list
    dist[src] = 0 # 0 to 0
    pq = []
    heapq.heappush(pq, (0, src)) # (distance, node)
    
    while(pq):
        du, u = heapq.heappop(pq)
        
        # skip outdated elements
        if du != dist[u]: continue
        
        for v, w in adj[u]:
            if(dist[v] > du + w): 
                dist[v] = du + w
                heapq.heappush(pq, (dist[v], v))
    return dist

def main():
    n, m = map(int, input().split())
    adj = [[] for _ in range (n + 1)]
    
    for _ in range(m): 
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        
    for i in range(1, n + 1):
        dist = dijkstra(i, n, adj)
        for j in range(1, n + 1):
            print(-1 if dist[j] == INF else dist[j], end=" ")
        print()

if __name__ == "__main__":
    main()