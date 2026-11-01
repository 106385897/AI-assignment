import sys
from dfs import dfs
# Teammates add their imports here, for example:
from bfs import bfs
# from gbfs import gbfs
# from astar import astar
from cus1 import cus1
# from cus2 import cus2

# Teammates add one line each here
METHODS = {
    "DFS": dfs,
    "BFS": bfs,
    # "GBFS": gbfs,
    # "AS": astar,
    "CUS1": cus1,
    # "CUS2": cus2,
}


def read_file(filename):
    nodes = {}
    edges = {}
    origin = None
    destinations = []
    section = ""

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue

            if line.lower() == "nodes:":
                section = "nodes"
            elif line.lower() == "edges:":
                section = "edges"
            elif line.lower() == "origin:":
                section = "origin"
            elif line.lower() == "destinations:":
                section = "destinations"

            elif section == "nodes":
                # Example line: 1: (4,1)
                parts = line.split(":")
                node_id = int(parts[0])
                coords = parts[1].replace("(", "").replace(")", "")
                x, y = coords.split(",")
                nodes[node_id] = (int(x), int(y))

            elif section == "edges":
                # Example line: (2,1): 4
                parts = line.split(":")
                pair = parts[0].replace("(", "").replace(")", "")
                a, b = pair.split(",")
                edges[(int(a), int(b))] = int(parts[1])

            elif section == "origin":
                origin = int(line)

            elif section == "destinations":
                # Example line: 5; 4
                for part in line.split(";"):
                    if part.strip() != "":
                        destinations.append(int(part))

    return nodes, edges, origin, destinations


def build_graph(edges):
    # graph[node] = list of (neighbour, cost), sorted by neighbour number
    graph = {}
    for (a, b), cost in edges.items():
        if a not in graph:
            graph[a] = []
        graph[a].append((b, cost))
    for a in graph:
        graph[a].sort()
    return graph


def main():
    if len(sys.argv) != 3:
        print("Usage: python search.py <filename> <method>")
        return

    filename = sys.argv[1]
    method = sys.argv[2].upper()

    try:
        nodes, edges, origin, destinations = read_file(filename)
    except FileNotFoundError:
        print("Error: file not found")
        return
    except (ValueError, IndexError):
        print("Error: invalid file format")
        return

    if method not in METHODS:
        print("Error: unknown or unfinished method", method)
        return

    graph = build_graph(edges)
    result = METHODS[method](nodes, graph, origin, destinations)

    print(filename, method)
    if result["goal"] is None:
        print("No goal found", result["nodes_created"])
    else:
        print(result["goal"], result["nodes_created"])
        print(" ".join(str(n) for n in result["path"]))


if __name__ == "__main__":
    main()