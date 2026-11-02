from node import Node


def dfs(nodes, graph, origin, destinations):
    stack = [Node(origin)]
    nodes_created = 1

    while stack:
        current = stack.pop()

       
        if current.node_id in destinations:
            return {"goal": current.node_id,
                    "path": current.get_path(),
                    "nodes_created": nodes_created}

       
        path_so_far = current.get_path()

        
        for neighbour, cost in reversed(graph.get(current.node_id, [])):
            if neighbour in path_so_far:
                continue
            stack.append(Node(neighbour, current, current.path_cost + cost))
            nodes_created += 1

    return {"goal": None, "path": None, "nodes_created": nodes_created}