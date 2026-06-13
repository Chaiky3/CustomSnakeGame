from typing import List, Tuple


class SmartQeue:
    def __init__(self) -> None:
        """
        ::
            Constructor for SmartQeue.
            The holds tuples representing points (x, y).
            Every 2 points compose a line.
        """
        self.qeue: List[Tuple[int, int]] = []

    def append(self, value: Tuple[int, int]) -> None:
        """
        ::
            Appends to the beinning of the qeue (head).


        Parameters:
            (Tuple[int, int]) value:        Value to append.
        """
        self.qeue.insert(0, value)

    def push(self, value: Tuple[int, int]) -> None:
        """
        ::
            Pushes to the left side of the qeue, FIFO style.

        Parameters:
            (Tuple[int, int]) value:        Value to push.
        """
        self.append(value)
        self.qeue.pop()

    def get_head_point(self) -> Tuple[int, int]:
        """
        ::
            Getter for first value int qeue.

        Return:
            (Tuple[int, int]):                          First element in qeue.

        """
        return self.qeue[0]

    def get_head_node(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        """
        ::
            Getter for first 2 elements in qeue as a tuple.

        Return:
            (Tuple[Tuple[int, int], Tuple[int, int]]):  First 2 elements as tuple.

        """
        return self.qeue[0], self.qeue[1]
