from typing import List, Tuple


class SmartQueue:
    def __init__(self) -> None:
        """
        ::
            Constructor for SmartQueue.
            Holds tuples representing points (x, y).
            Every 2 points compose a line.
        """
        self.queue: List[Tuple[int, int]] = []

    def append(self, value: Tuple[int, int]) -> None:
        """
        ::
            Appends to the beginning of the queue (head).

        Parameters:
            (Tuple[int, int]) value:        Value to append.
        """
        self.queue.insert(0, value)

    def push(self, value: Tuple[int, int]) -> None:
        """
        ::
            Pushes to the left side of the queue, FIFO style.

        Parameters:
            (Tuple[int, int]) value:        Value to push.
        """
        self.append(value)
        if self.queue:
            self.queue.pop()

    def get_head_point(self) -> Tuple[int, int]:
        """
        ::
            Getter for first value in queue.

        Return:
            (Tuple[int, int]):                          First element in queue.
        """
        return self.queue[0]

    def get_head_node(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        """
        ::
            Getter for first 2 elements in queue as a tuple.

        Return:
            (Tuple[Tuple[int, int], Tuple[int, int]]):  First 2 elements as tuple.
        """
        return self.queue[0], self.queue[1]
