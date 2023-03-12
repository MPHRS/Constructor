from typing import Final, List, Tuple

Bondtype = List[Tuple[int, int]]

EMPTY: Final[Bondtype] = []
LINEAR: Final[Bondtype] = [(0, 1), (1, 2), (2, 3)]
GAP_ENUM: Final[Bondtype] = [(0, 1), (3, 0), (1, 3)]
NEGATIVE: Final[Bondtype] = [(-1, 0), (0, 1), (1, 2)]
DOUBLE_BOND: Final[Bondtype] = [(1, 2), (2, 1)]
CYCLIC_EDGE: Final[Bondtype] = [(0, 0), (1, 1), (2, 2)]