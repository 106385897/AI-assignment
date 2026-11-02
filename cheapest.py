import heapq
from node import Node


def cheapest_path(graph, start, goal):
    counter = 0
    frontier = [(0, start, counter, Node(start))]
    best = {start: 0}   
    while frontier:
        cost, node_id, _, current = heapq.heappop(frontier)

        if cost > best[node_id]:
            continue

        if node_id == goal:
            return cost, current.get_path()

        for neighbour, step in graph.get(node_id, []):
            new_cost = cost + step
            if neighbour not in best or new_cost < best[neighbour]:
                best[neighbour] = new_cost
                counter += 1
                heapq.heappush(frontier,
                               (new_cost, neighbour, counter,
                                Node(neighbour, current, new_cost)))

    return None, None