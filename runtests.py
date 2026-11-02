import os

methods = ["DFS", "BFS", "GBFS", "AS", "CUS1", "CUS2"]

open("results.txt", "w").close()   # empty the old results file

for name in sorted(os.listdir("tests")):
    if name.endswith(".txt"):
        for method in methods:
            os.system(f"python search.py tests/{name} {method} >> results.txt")

print("Done. See results.txt")