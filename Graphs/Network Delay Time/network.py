class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        # Min-heap to always process the node with the smallest time so far
        min_heap = [(0, k)]  # (current_time, node)

        visited = {}  # Dictionary to store the shortest time at which each node is reached
        t = 0  # Variable to keep track of the latest time any node is reached

        while min_heap:
            time, node = heapq.heappop(min_heap)

            # If we’ve already visited this node, skip it
            if node in visited:
                continue

            # Mark the node as visited and store the time it was reached
            visited[node] = time
            t = time  # Update the latest time we've reached a node

            # Push all unvisited neighbors to the heap with their accumulated times
            for nei, wt in graph[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (time + wt, nei))

        # If all nodes were reached, return the total delay time (max of shortest paths)
        # Otherwise, return -1 (not all nodes received the signal)
        return t if len(visited) == n else -1