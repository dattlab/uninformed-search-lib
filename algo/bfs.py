from collections import deque
from .utils import print_queue


def bfs(root, target) -> None:
    search_queue = deque()
    search_queue.appendleft(root)

    nth_search_queue = 1
    while search_queue:
        print(f"Queue Status {nth_search_queue}: ", end="")
        print_queue(search_queue)

        _next = search_queue.popleft()

        if not _next:
            continue

        if _next.value == target:
            print("\nRESULT: Target was found")
            return

        search_queue.appendleft(_next.left)
        search_queue.appendleft(_next.right)

        nth_search_queue += 1

    print("\nRESULT: Target was NOT found")
    return
