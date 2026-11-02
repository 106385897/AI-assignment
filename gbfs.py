
import heapq
from itertools import count
from informed_search import heuristic


def gbfs(nodes, graph, origin, destinations):
    # Priority queue for GBFS
    frontier = []
    insertion_order = count()

    # Add the starting node
    start_h = heuristic(origin, destinations, nodes)

    heapq.heappush(
        frontier,
        (start_h, origin, next(insertion_order), [origin])
    )

    # Count the origin as the first created node
    nodes_created = 1

    while frontier:
        # Get the node with the smallest heuristic
        current_h, current, order, path = heapq.heappop(frontier)

        # Check if the current node is a destination
        if current in destinations:
            return {
                "goal": current,
                "nodes_created": nodes_created,
                "path": path
            }

        # Explore neighbours in ascending node order
        for neighbor, cost in sorted(graph.get(current, [])):
            # Avoid going back to a node already in this path
            if neighbor in path:
                continue

            new_path = path + [neighbor]
            new_h = heuristic(neighbor, destinations, nodes)

            heapq.heappush(
                frontier,
                (
                    new_h,
                    neighbor,
                    next(insertion_order),
                    new_path
                )
            )

            # Count every node added to the frontier
            nodes_created += 1

    # No destination found
    return {
        "goal": None,
        "nodes_created": nodes_created,
        "path": []
    }
