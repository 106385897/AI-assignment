from collections import deque
from node import Node

#Breadth-first search: FIFO queue, fewest moves
def bfs(nodes, graph, origin, destinations):
    queue = deque([Node(origin)])  # FIFO: oldest node expanded first
    nodes_created = 1 # root counts as created

    while queue:
        current = queue.popleft() 

        # Goal test when popped, not when generated
        if current.node_id in destinations:
            return {"goal": current.node_id,
                    "path": current.get_path(),
                    "nodes_created": nodes_created}

        path_so_far = current.get_path()

        # neighbours are sorted ascending, so smaller nodes are queued first
        for neighbour, cost in graph.get(current.node_id, []):
            if neighbour in path_so_far:
                continue
            queue.append(Node(neighbour, current, current.path_cost + cost))
            nodes_created += 1

    # Queue empty: no destination reachable
    return {"goal": None, "path": None, "nodes_created": nodes_created}