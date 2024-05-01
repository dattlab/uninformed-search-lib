from algo.bfs import bfs
from algo.dfs import dfs
from algo.utils import BinaryTree


def main() -> None:
    bt = BinaryTree()
    nodes = [
        50, 25, 75, 10, 33, 56, 
        89, 4, 11, 30, 40, 52,
        61, 82, 95
    ]

    bt.add_node_list(nodes)

    """
    When the list of nodes were inserted in BinaryTree(),
    it would look like this:
    """
    print("""
    Example Tree:

              +---------5---------+
              |                   |
              .                   .
          +---25---+         +---75---+
          |        |         |        |
          .        .         .        .
        +-10-+   +-33-+    +-56-+  +-89-+
        |    |   |    |    |    |  |    |
        .    .   .    .    .    .  .    .
        4   11   30  40    52  61  82  95
    """)

    print("""
    Choose an algorithm:
    [1] Breadth-first Search (BFS)
    [2] Depth-first Search (DFS)
    """)
    print("="*30)

    while True:
        algo_option = input("Enter here: ")
        if algo_option in {"1", "2"}:
            break

    input_target = int(input("What to search? "))
    print("="*30)

    match algo_option:
        case "1":
            bfs(bt.root, input_target)
        case "2":
            dfs(bt.root, input_target)


if __name__ == '__main__':
    main()