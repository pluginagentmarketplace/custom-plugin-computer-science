# Algorithms Guide

## Sorting Algorithms

### QuickSort
```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
```
**Time**: O(n log n) average, O(n²) worst
**Space**: O(log n)

### MergeSort
```python
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)
```
**Time**: O(n log n) guaranteed
**Space**: O(n)

## Graph Algorithms

### BFS (Breadth-First Search)
```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited
```

### Dijkstra's Shortest Path
```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current = heapq.heappop(pq)
        if current_dist > distances[current]:
            continue
        for neighbor, weight in graph[current]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances
```

## Complexity Cheat Sheet

| Algorithm | Time | Space |
|-----------|------|-------|
| Binary Search | O(log n) | O(1) |
| QuickSort | O(n log n) | O(log n) |
| MergeSort | O(n log n) | O(n) |
| HeapSort | O(n log n) | O(1) |
| BFS/DFS | O(V + E) | O(V) |
| Dijkstra | O((V+E) log V) | O(V) |

---

*Computer Science Plugin - Algorithms Skill*
