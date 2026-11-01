import math
import heapq


def heuristic(node, destinations, coordinates):
    distances = []

    for goal in destinations:
        x1, y1 = coordinates[node]
        x2, y2 = coordinates[goal]

        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        distances.append(distance)

    return min(distances)
