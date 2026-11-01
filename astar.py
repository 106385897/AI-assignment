
import heapq
from itertools import count
from informed_search import heuristic


def astar(nodes, edges, origin, destinations):
    # Create a directed weighted graph
    graph = {node_id: [] for node_id in nodes}

    for (source, target), cost in edges.items():
        graph[source].append((target, cost))

    # Sort neighbors in ascending order
    for node_id in graph:
        graph[node_id].sort(key=lambda edge: edge[0])

    # Priority queue stores:
    # (f_cost, insertion_order, node, g_cost, path)
    frontier = []
    insertion_order = count()

    # Starting node has a path cost of zero
    start_g = 0
    start_h = heuristic(origin, destinations, nodes)

    heapq.heappush(
        frontier,
        (start_g + start_h, next(insertion_order),
         origin, start_g, [origin])
    )

    nodes_created = 1

    # Remember the cheapest known cost to each state
    best_cost = {origin: 0}

    while frontier:
        current_f, order, current, current_g, path = heapq.heappop(
            frontier
        )

        # Ignore outdated queue entries
        if current_g > best_cost.get(current, float("inf")):
            continue

        # Check whether we reached a destination
        if current in destinations:
            return {
                "goal": current,
                "nodes_created": nodes_created,
                "path": path
            }

        # Explore outgoing edges
        for neighbor, edge_cost in graph.get(current, []):
            new_g = current_g + edge_cost

            # Only consider a cheaper route to this node
            if new_g < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_g

                new_h = heuristic(neighbor, destinations, nodes)
                new_f = new_g + new_h
                new_path = path + [neighbor]

                heapq.heappush(
                    frontier,
                    (
                        new_f,
                        next(insertion_order),
                        neighbor,
                        new_g,
                        new_path
                    )
                )

                nodes_created += 1

    return None
