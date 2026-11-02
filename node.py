class Node:
    # One node in the search tree (not the same as a graph node)
    def __init__(self, node_id, parent=None, path_cost=0):
        self.node_id = node_id
        self.parent = parent
        self.path_cost = path_cost

    def get_path(self):
        #Return the list of node ids from the origin to this node.
        path = []
        node = self
        # Build the path backwards, then reverse it
        while node is not None:
            path.append(node.node_id)
            node = node.parent
        path.reverse()
        return path