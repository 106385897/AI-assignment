
import math


def heuristic(node, destinations, coordinates):
    # Find the straight-line distance to the closest destination.
    # This heuristic is shared by GBFS and A*.
    x1, y1 = coordinates[node]

    distances = []

    for goal in destinations:
        x2, y2 = coordinates[goal]

        # Euclidean distance between the current node and destination.
        distance = math.hypot(x2 - x1, y2 - y1)
        distances.append(distance)

    return min(distances)


def heuristic_scale(nodes, graph):
    # Find a safe multiplier for A* based on the graph's edge costs.
    # This helps keep the heuristic from overestimating route costs.
    scale = float("inf")

    for source, neighbors in graph.items():
        for target, edge_cost in neighbors:
            x1, y1 = nodes[source]
            x2, y2 = nodes[target]

            distance = math.hypot(x2 - x1, y2 - y1)

            if distance > 0:
                scale = min(scale, edge_cost / distance)

    # If no suitable edge exists, use a zero heuristic.
    if scale == float("inf"):
        return 0

    return scale
