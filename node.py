class Node:
    def __init__(self, node_id, parent=None, path_cost=0):
        self.node_id = node_id
        self.parent = parent
        self.path_cost = path_cost

    def get_path(self):
        path = []
        node = self
        while node is not None:
            path.append(node.node_id)
            node = node.parent
        path.reverse()
        return path