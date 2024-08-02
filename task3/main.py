import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v, weight):
        if u not in self.edges:
            self.edges[u] = []
        if v not in self.edges:
            self.edges[v] = []
        self.edges[u].append((v, weight))
        self.edges[v].append((u, weight)) 

    def dijkstra(self, start):
        min_heap = [(0, start)]  
        distances = {vertex: float('infinity') for vertex in self.edges}
        distances[start] = 0
        visited = set()

        while min_heap:
            current_distance, current_vertex = heapq.heappop(min_heap)

            if current_vertex in visited:
                continue

            visited.add(current_vertex)

            for neighbor, weight in self.edges[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        return distances

graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

distances = graph.dijkstra('A')

print(f"Найкоротші відстані від вершини A:")
for vertex, distance in distances.items():
    print(f"Відстань до {vertex}: {distance}")