
class Graph:
    def __init__(self, vertices):
        if vertices <= 0:
            raise ValueError("Number of vertices must be greater than 0.")
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, src, dest, weight):
        if src < 0 or dest < 0 or src >= self.V or dest >= self.V or weight < 0:
            raise ValueError("Invalid edge parameters.")
        self.graph[src][dest] = weight
        self.graph[dest][src] = weight

    def tsp_greedy(self, start):
        if start < 0 or start >= self.V:
            raise ValueError("Invalid start node.")
        
        visited = [False] * self.V
        path = []
        total_time = 0

        current = start
        path.append(current)
        visited[current] = True

        for _ in range(self.V - 1):
            nearest_neighbor = None
            nearest_time = float('inf')
            for j in range(self.V):
                if not visited[j] and self.graph[current][j] < nearest_time and self.graph[current][j] > 0:
                    nearest_time = self.graph[current][j]
                    nearest_neighbor = j
            if nearest_neighbor is not None:
                path.append(nearest_neighbor)
                total_time += nearest_time
                visited[nearest_neighbor] = True
                current = nearest_neighbor

        total_time += self.graph[current][start]
        path.append(start)

        return total_time, path