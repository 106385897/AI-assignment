
import heapq
from itertools import count
from informed_search import heuristic, heuristic_scale


def astar(nodes, graph, origin, destinations):
    # A* uses f(n) = g(n) + h(n).
    # g(n) is the actual path cost so far.
    # h(n) estimates the remaining cost to a destination.

    # Scale the shared straight-line heuristic using edge costs.
    # This helps prevent overestimating the remaining path cost.
    scale = heuristic_scale(nodes, graph)

    # Priority queue stores:
    # (f_cost, node_id, insertion_order, g_cost, path)
    frontier = []
    insertion_order = count()

    # The starting node has a path cost of zero.
    start_h = scale * heuristic(origin, destinations, nodes)

    heapq.heappush(
        frontier,
        (start_h, origin, next(insertion_order), 0, [origin])
    )

    nodes_created = 1

    # Track the cheapest known cost to reach each node.
    best_cost = {origin: 0}

    while frontier:
        # Select the node with the lowest estimated total cost.
        current_f, current, order, current_g, path = heapq.heappop(
            frontier
        )

        # Ignore an older entry if a cheaper route was found.
        if current_g > best_cost.get(current, float("inf")):
            continue

        # Return the result when a destination is reached.
        if current in destinations:
            return {
                "goal": current,
                "nodes_created": nodes_created,
                "path": path
            }

        # Explore neighbours in ascending node ID order.
        for neighbor, edge_cost in sorted(graph.get(current, [])):
            new_g = current_g + edge_cost

            # Only continue if this route is cheaper than before.
            if new_g < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_g

                # Estimate the remaining cost using the shared heuristic.
                new_h = scale * heuristic(neighbor, destinations, nodes)
                new_f = new_g + new_h
                new_path = path + [neighbor]

                # Add the improved route to the priority queue.
                # Node ID and insertion order break priority ties.
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

    # Return None for the path if no destination is reachable.
    return {
        "goal": None,
        "nodes_created": nodes_created,
        "path": None
    }
