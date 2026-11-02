import sys
from search import read_file, build_graph
from cheapest import cheapest_path

filename = sys.argv[1]
nodes, edges, origin, destinations = read_file(filename)
graph = build_graph(edges)

print("From the origin:")
for d in destinations:
    cost, path = cheapest_path(graph, origin, d)
    print(origin, "->", d, ":", cost, path)


points = [origin]
for d in destinations:
    if d not in points:
        points.append(d)

print("Between every pair:")
for a in points:
    for b in points:
        if a != b:
            cost, path = cheapest_path(graph, a, b)
            print(a, "->", b, ":", cost, path)