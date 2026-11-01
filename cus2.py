import heapq
import math

def distance(p, q):
    """Straight-line distance between two points p=(x, y) and q=(x, y)"""
    return math.sqrt((p[0] - q[0]) **2 + (p[1] - q[1]) **2)    #using Pythagoras


def longest_edge(nodes, edges):
    """L_max: the longest straight-line length of any edge"""
    longest = 0
    for start in edges:                       # every node...
        for end, cost in edges[start]:        # ...and every edge leaving it
            d = distance(nodes[start], nodes[end])
            if d > longest:
                longest = d
    return longest


def heuristic(node, nodes, destinations, l_max):
    """Fewest moves we could possibly still need from this node"""
    if node in destinations:
        return 0
    nearest = min(distance(nodes[node], nodes[d]) for d in destinations)
    return math.ceil(nearest/l_max)    #divide and round up


def cus2(nodes, edges, origin, destinations):  # four variables as inputs from step 1
    l_max = longest_edge(nodes, edges)  # longest one-move distance, needed by the heuristic
    frontier = []
    heapq.heappush(frontier, (heuristic(origin, nodes, destinations, l_max), origin, 0, [origin]))  
    nodes_created = 1  # the origin was first node created so count starts at 1
    best_g = {origin: 0}  # fewest moves found so far to reach each node
    explored = set()  # holds nodes we've already checked, starts empty

    while frontier:  # repeat while the frontier still has something in it
        f, node, g, path = heapq.heappop(frontier)

        if node in explored:  # if node already checked, skip it
            continue

        if node in destinations:  # if destination then stop and hand back goal, count, route
            return{"goal": node, "path": path, "nodes_created": nodes_created}

        explored.add(node)  # mark node as checked

        for neighbour, cost in edges.get(node, []):  # loop through departures; cost unused because CUS2 counts moves
            new_g = g + 1  # moves to reach neighbour = parent's g + 1
            if neighbour in explored:  # if neighbour checked, skip it
                continue
            if neighbour in best_g and best_g[neighbour] <= new_g:  # already have an equal-or-shorter route, skip
                continue
            best_g[neighbour] = new_g  # new or better route: record it
            nodes_created += 1
            heapq.heappush(frontier, (new_g + heuristic(neighbour, nodes, destinations, l_max), neighbour, new_g, path + [neighbour]))

    return{"goal": None, "path": None, "nodes_created": nodes_created}  # only runs if frontier empties without finding a destination


