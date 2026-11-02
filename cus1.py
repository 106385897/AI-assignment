import heapq
from node import Node


def cus1(nodes, graph, origin, destinations):
    counter = 0                                  # insertion order, for ties
    frontier = [(0, origin, counter, Node(origin))]
    nodes_created = 1

    while frontier:
        g, _, _, current = heapq.heappop(frontier)   # lowest g first

        if current.node_id in destinations:
            return {"goal": current.node_id,
                    "path": current.get_path(),
                    "nodes_created": nodes_created}

        path_so_far = current.get_path()

        for neighbour, cost in graph.get(current.node_id, []):
            if neighbour in path_so_far:
                continue
            counter += 1
            child = Node(neighbour, current, current.path_cost + cost)
            heapq.heappush(frontier, (child.path_cost, neighbour, counter, child))
            nodes_created += 1

    return {"goal": None, "path": None, "nodes_created": nodes_created}