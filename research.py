import sys
from itertools import permutations #permutations lists every possible order of some items
from search import read_file, build_graph
from cheapest import cheapest_path      # Nahan's part: cheapest (cost, path) between two nodes


def best_order(graph, origin, destinations):
    """Try every visiting order and return the cheapest: (total_cost, order, full_route)."""
    targets = [d for d in destinations if d != origin]   # origin is already "visited"
    best_cost, best_ord, best_route = None, None, None

    for order in permutations(sorted(targets)):   # e.g. (3, 4) then (4, 3)
        total = 0
        route = [origin]
        current = origin
        possible = True

        for d in order:                            # walk the order one destination at a time
            cost, path = cheapest_path(graph, current, d)
            if cost is None:                       # can't reach d from here
                possible = False
                break
            total = total + cost                   #add this leg's cost
            route = route + path[1:]               #join this leg's path onto the route
            current = d                            # we are now standing at d

        if possible and (best_cost is None or total < best_cost):  # is this order cheaper?
            best_cost, best_ord, best_route = total, order, route

    return best_cost, best_ord, best_route


if __name__ == "__main__":
    nodes, edges, origin, destinations = read_file(sys.argv[1])
    graph = build_graph(edges)
    cost, order, route = best_order(graph, origin, destinations)
    if order is None:                              # no order reaches every destination
        print("Not every destination can be reached from the origin")
    else:
        print("Best order:", order, "| total cost:", cost)
        print("Route:", " ".join(str(n) for n in route))