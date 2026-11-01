
import heapq
import math
from itertools import count


def astar(nodes, graph, origin, destinations):
    # Find a safe scale for the Euclidean heuristic
    # This helps prevent the heuristic from overestimating costs
    scale = float("inf")

    for source, neighbors in graph.items():
        for target, edge_cost in neighbors:
            x1, y1 = nodes[source]
            x2, y2 = nodes[target]

            distance = math.hypot(x2 - x1, y2 - y1)

            if distance > 0:
                scale = min(scale, edge_cost / distance)

    if scale == float("inf"):
        scale = 0

    def heuristic(node):
        x1, y1 = nodes[node]

        return scale * min(
            math.hypot(nodes[goal][0] - x1, nodes[goal][1] - y1)
            for goal in destinations
        )

    # Priority queue stores:
    # (f_cost, node_id, insertion_order, g_cost, path)
    frontier = []
    insertion_order = count()

    start_h = heuristic(origin)

    heapq.heappush(
        frontier,
        (start_h, origin, next(insertion_order), 0, [origin])
    )

    nodes_created = 1

    # Store the cheapest known path cost to each node
    best_cost = {origin: 0}

    while frontier:
        current_f, current, order, current_g, path = heapq.heappop(
            frontier
        )

        # Skip an outdated entry
        if current_g > best_cost.get(current, float("inf")):
            continue

        # Check whether we reached a destination
        if current in destinations:
            return {
                "goal": current,
                "nodes_created": nodes_created,
                "path": path
            }

        # Explore neighbours in ascending node order
        for neighbor, edge_cost in sorted(graph.get(current, [])):
            new_g = current_g + edge_cost

            # Only add a better route to the frontier
            if new_g < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_g

                new_h = heuristic(neighbor)
                new_f = new_g + new_h
                new_path = path + [neighbor]

                heapq.heappush(
                    frontier,
                    (
                        new_f,
                        neighbor,
                        next(insertion_order),
                        new_g,
                        new_path
                    )
                )

                nodes_created += 1

    # No destination found
    return {
        "goal": None,
        "nodes_created": nodes_created,
        "path": []
    }
