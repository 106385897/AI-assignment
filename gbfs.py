
import heapq
from itertools import count
from informed_search import heuristic


def gbfs(nodes, edges, origin, destinations):
    # Convert directed edges into an adjacency list
    graph = {node_id: [] for node_id in nodes}

    for (source, target), cost in edges.items():
        graph[source].append((target, cost))

    for node_id in graph:
        graph[node_id].sort(key=lambda edge: edge[0])

    # Priority queue: (heuristic, insertion order, node, path)
    frontier = []
    insertion_order = count()

    start_h = heuristic(origin, destinations, nodes)
    heapq.heappush(
        frontier,
        (start_h, next(insertion_order), origin, [origin])
    )

    nodes_created = 1

    while frontier:
        current_h, order, current, path = heapq.heappop(frontier)

        # Stop when a destination is reached
        if current in destinations:
            return {
                "goal": current,
                "nodes_created": nodes_created,
                "path": path
            }

        # Expand neighbors in ascending node order
        for neighbor, cost in graph.get(current, []):
            # Prevent cycles along the current search path
            if neighbor in path:
                continue

            new_path = path + [neighbor]
            neighbor_h = heuristic(neighbor, destinations, nodes)

            heapq.heappush(
                frontier,
                (
                    neighbor_h,
                    next(insertion_order),
                    neighbor,
                    new_path
                )
            )

            nodes_created += 1

    return None
