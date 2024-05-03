from algo.bfs import bfs
from algo.dfs import dfs
from algo.ucs import ucs
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
    Choose an algorithm:
    [1] Breadth-first Search (BFS)
    [2] Depth-first Search (DFS)
    [3] Uniform Cost Search (UCS)
    """)
    print("="*30)

    while True:
        algo_option = input("Enter here: ")
        if algo_option in {"1", "2", "3"}:
            break


    match algo_option:
        case "1":
            print("""
            Example Tree:
        
                      +---------50--------+
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
            input_target = int(input("What to search? "))
            print("="*30)
            bfs(bt.root, input_target)
        case "2":
            print("""
            Example Tree:
        
                      +---------50--------+
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
            input_target = int(input("What to search? "))
            print("="*30)
            dfs(bt.root, input_target)
        case "3":
            print("""
            Example Graph:
            graph = {
                        'S': {'A': 3, 'B': 2, 'C': 6},
                        'A': {'S': 3, 'B': 1, 'D': 1},
                        'B': {'S': 2, 'A': 1, 'D': 4, 'E': 2},
                        'C': {'S': 6, 'E': 5},
                        'D': {'A': 1, 'B': 4, 'E': 1, 'F': 5},
                        'E': {'B': 2, 'C': 5, 'D': 1, 'F': 3},
                        'F': {'D': 5, 'E': 3}
                    }
            """)
            start_node = str(input("Starting position: "))
            goal_node = str(input("Goal: "))
            ucs(start_node, goal_node)


if __name__ == '__main__':
    main()
