from node import Node

# Depth-first search: LIFO stack, deepest node first
def dfs(nodes, graph, origin, destinations):
    stack = [Node(origin)] # LIFO: newest node expanded first
    nodes_created = 1 # root counts as created

    while stack:
        current = stack.pop()

        # Goal test when popped, not when generated
        if current.node_id in destinations:
            return {"goal": current.node_id,
                    "path": current.get_path(),
                    "nodes_created": nodes_created}

       
        path_so_far = current.get_path()

        # Push in reverse so the smallest neighbour ends up on top of the
        # stack and is expanded first
        for neighbour, cost in reversed(graph.get(current.node_id, [])):
            if neighbour in path_so_far:
                continue
            stack.append(Node(neighbour, current, current.path_cost + cost))
            nodes_created += 1
    # Stack empty: no destination reachable
    return {"goal": None, "path": None, "nodes_created": nodes_created}