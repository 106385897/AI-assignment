
from gbfs import gbfs
from astar import astar


def read_test_file(filename):
    nodes = {}
    edges = {}
    origin = None
    destinations = []
    section = ""

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line in ["Nodes:", "Edges:", "Origin:", "Destinations:"]:
                section = line[:-1]
                continue

            if section == "Nodes":
                node_id, coordinates = line.split(":")
                x, y = coordinates.strip().strip("()").split(",")
                nodes[int(node_id)] = (int(x), int(y))

            elif section == "Edges":
                connection, cost = line.split(":")
                source, target = connection.strip().strip("()").split(",")
                edges[(int(source), int(target))] = int(cost)

            elif section == "Origin":
                origin = int(line)

            elif section == "Destinations":
                destinations = [
                    int(goal.strip()) for goal in line.split(";")
                ]

    return nodes, edges, origin, destinations


def main():
    test_files = [
        "test1.txt",
        "test2.txt",
        "test3.txt",
        "test4.txt",
        "test_tiebreak.txt"
    ]

    for filename in test_files:
        print("\n" + "=" * 40)
        print("Testing:", filename)
        print("=" * 40)

        nodes, edges, origin, destinations = read_test_file(filename)

        gbfs_result = gbfs(nodes, edges, origin, destinations)
        astar_result = astar(nodes, edges, origin, destinations)

        print("GBFS Result:", gbfs_result)
        print("A* Result:", astar_result)

    print("\nAll tests finished!")


if __name__ == "__main__":
    main()
