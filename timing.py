import random
import time
from research import best_order, greedy_order


def make_random_graph(seed):
    """Make a random one-way graph with 30 nodes."""
    random.seed(seed)        # same seed = same graph every time, so results can be repeated
    graph = {}
    for node in range(1, 31):
        graph[node] = []

    # a circle 1 -> 2 -> ... -> 30 -> 1, so every node can be reached
    for node in range(1, 30):
        graph[node].append((node + 1, random.randint(1, 20)))
    graph[30].append((1, random.randint(1, 20)))

    # 60 extra random shortcuts
    for i in range(60):
        a = random.randint(1, 30)
        b = random.randint(1, 30)
        if a != b:
            graph[a].append((b, random.randint(1, 20)))

    for node in graph:
        graph[node].sort()   # sorted neighbours, same as build_graph in search.py
    return graph


for num_dests in range(2, 9):          # try 2, 3, 4 ... 8 destinations
    every_order_time = 0
    greedy_time = 0
    greedy_was_best = 0

    for trial in range(10):            # 10 different random graphs for each size
        graph = make_random_graph(trial)
        destinations = random.sample(range(2, 31), num_dests)   # pick random destinations

        start = time.perf_counter()                 # start the stopwatch
        best_cost, _, _ = best_order(graph, 1, destinations)
        every_order_time += time.perf_counter() - start

        start = time.perf_counter()
        greedy_cost, _, _ = greedy_order(graph, 1, destinations)
        greedy_time += time.perf_counter() - start

        if greedy_cost == best_cost:
            greedy_was_best += 1

    # average time per graph, in milliseconds
    print("Destinations:", num_dests)
    print("  Every order:", round(every_order_time / 10 * 1000, 2), "ms")
    print("  Greedy:     ", round(greedy_time / 10 * 1000, 2), "ms")
    print("  Greedy found the best route", greedy_was_best, "out of 10 times")