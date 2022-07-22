"""Minesweeper"""
import re
from collections import defaultdict


def annotate(minefield):
    """Return `minefield` annotated with mine counts"""
    # Function body starts here
    nrows = len(minefield)
    if nrows == 0:
        return []

    ncols = len(minefield[0])
    if ncols == 0:
        return [""]

    if not all(len(row) == ncols for row in minefield[1:]) or not all(
        re.fullmatch(r"[\* ]*", row) for row in minefield
    ):
        # The rows are not equal length or one of them contains an invalid character
        raise ValueError("The board is invalid with current input.")

    mine_counts = defaultdict(int)
    mine_locations = []

    for idx_r, row in enumerate(minefield):
        for idx_c, char in enumerate(row):
            if char != "*":
                continue
            # The boundaries are ignored here. This works because of the
            # defaultdict and because the out-of-bound locations are ignored
            # when constructing the annotated list
            mine_locations.append((idx_r, idx_c))
            mine_counts[(idx_r, idx_c - 1)] += 1
            mine_counts[(idx_r, idx_c + 1)] += 1
            mine_counts[(idx_r - 1, idx_c)] += 1
            mine_counts[(idx_r + 1, idx_c)] += 1
            mine_counts[(idx_r - 1, idx_c - 1)] += 1
            mine_counts[(idx_r - 1, idx_c + 1)] += 1
            mine_counts[(idx_r + 1, idx_c - 1)] += 1
            mine_counts[(idx_r + 1, idx_c + 1)] += 1

    count_list = [""] * nrows
    for idx_r in range(nrows):
        for idx_c in range(ncols):
            idx = (idx_r, idx_c)
            if idx in mine_locations:
                char = "*"
            else:
                char = mine_counts[idx] if mine_counts[idx] else " "
            count_list[idx_r] = f"{count_list[idx_r]}{char}"

    return count_list
