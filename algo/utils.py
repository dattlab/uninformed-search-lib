class Node:
    """Binary Tree Node"""
    def __init__(self, value: int, left = None, right = None) -> None:
        self.left = left
        self.right = right
        self.value = value


class BinaryTree:
    """
    Binary Tree implementation

    The default characteristics:
    - The left node's value is less than the current
      node's value
    - The right node's value is greater than or
      equal than the current node's value
    """
    def __init__(self) -> None:
        self.root: Node = None

    def insert(self, new_value: int) -> None:
        if self.root == None:
            self.root = Node(new_value)
            return

        curr_node = self.root
        while curr_node:
            if new_value >= curr_node.value:
                if curr_node.right == None:
                    curr_node.right = Node(new_value)
                    return
                else:
                    curr_node = curr_node.right
            else:
                if curr_node.left == None:
                    curr_node.left = Node(new_value)
                    return
                else:
                    curr_node = curr_node.left

    def add_node_list(self, new_values: list[int]) -> None:
        for value in new_values:
            self.insert(value)


def print_queue(q) -> None:
    print("[ ", end="")
    for node in list(q):
        if node:
            print(f"{node.value} ", end="")
        else:
            print(f"None ", end="")
    print("]")
