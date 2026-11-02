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
            total = total + cost                   # add this leg's cost to the running total
            route = route + path[1:]               # join this leg's path on, skipping its first node (already in route)
            current = d                            # we are now standing at d

        if possible and (best_cost is None or total < best_cost):  # keep this order if it's the first one or cheaper
            best_cost, best_ord, best_route = total, order, route

    return best_cost, best_ord, best_route


def greedy_order(graph, origin, destinations):
    """Always go to the cheapest-to-reach unvisited destination next: (total_cost, order, full_route)."""
    remaining = [d for d in destinations if d != origin]   # destinations still to visit
    total = 0
    route = [origin]
    current = origin
    order = []

    while remaining:                                   # until every destination is visited
        nearest = None                                 # (cost, destination, path) of the closest one
        for d in sorted(remaining):                    # sorted, so ties go to the smaller node
            cost, path = cheapest_path(graph, current, d)
            if cost is not None and (nearest is None or cost < nearest[0]):
                nearest = (cost, d, path)
        if nearest is None:                            # none of the remaining can be reached: stuck
            return None, None, None
        cost, d, path = nearest
        total = total + cost                           # same joining steps as best_order
        route = route + path[1:]
        current = d
        order.append(d)
        remaining.remove(d)                            # d is now visited

    return total, tuple(order), route


if __name__ == "__main__":
    nodes, edges, origin, destinations = read_file(sys.argv[1])
    graph = build_graph(edges)

    for name, method in [("Every order", best_order), ("Greedy", greedy_order)]:
        cost, order, route = method(graph, origin, destinations)
        if order is None:                              # no order reaches every destination
            print(name + ": not every destination can be reached from the origin")
        else:
            print(name + ": order", order, "| total cost:", cost, "| route:", " ".join(str(n) for n in route))