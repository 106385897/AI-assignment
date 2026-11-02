from collections import deque
from node import Node


def bfs(nodes, graph, origin, destinations):
    queue = deque([Node(origin)])
    nodes_created = 1

    while queue:
        current = queue.popleft()          # oldest node first (FIFO)

        if current.node_id in destinations:
            return {"goal": current.node_id,
                    "path": current.get_path(),
                    "nodes_created": nodes_created}

        path_so_far = current.get_path()

        # neighbours are already sorted ascending, so just go in order
        for neighbour, cost in graph.get(current.node_id, []):
            if neighbour in path_so_far:
                continue
            queue.append(Node(neighbour, current, current.path_cost + cost))
            nodes_created += 1

    return {"goal": None, "path": None, "nodes_created": nodes_created}