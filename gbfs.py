
import heapq
from itertools import count
from informed_search import heuristic


def gbfs(nodes, graph, origin, destinations):
    # GBFS selects the node with the smallest estimated
    # straight-line distance to a destination.
    frontier = []
    insertion_order = count()

    # Add the starting node to the priority queue.
    start_h = heuristic(origin, destinations, nodes)

    heapq.heappush(
        frontier,
        (start_h, origin, next(insertion_order), [origin])
    )

    # The origin counts as the first created node.
    nodes_created = 1

    while frontier:
        # Remove the node with the lowest heuristic value.
        # Node ID and insertion order are used for tie-breaking.
        current_h, current, order, path = heapq.heappop(frontier)

        # Return the result when a destination is reached.
        if current in destinations:
            return {
                "goal": current,
                "nodes_created": nodes_created,
                "path": path
            }

        # Explore neighbours in ascending node ID order.
        for neighbor, cost in sorted(graph.get(current, [])):

            # Avoid cycles within the current path.
            if neighbor in path:
                continue

            new_path = path + [neighbor]
            new_h = heuristic(neighbor, destinations, nodes)

            # Add the new path to the priority queue.
            heapq.heappush(
                frontier,
                (
                    new_h,
                    neighbor,
                    next(insertion_order),
                    new_path
                )
            )

            # Count every new node added to the frontier.
            nodes_created += 1

    # Return None for the path if no destination is reachable.
    return {
        "goal": None,
        "nodes_created": nodes_created,
        "path": None
    }
