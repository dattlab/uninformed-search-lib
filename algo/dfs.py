def dfs(root, target):
    return search(root, target)


def search(curr_node, target) -> None:
    """
    DFS's search implementation: recursive approach
    """

    if curr_node:
        print(f"Current node: {curr_node.value}")

    if not curr_node:
        
        print("\nRESULT: Target was NOT found")
        return False
    if curr_node.value == target:

        print("\nRESULT: Target was found")
        return True

    if curr_node.value < target:
        return search(curr_node.right, target)

    return search(curr_node.left, target)