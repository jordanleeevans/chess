from settings import ROWS, COLS
from typing import List, Tuple

def all_horizontal_moves(initial_row: int, initial_col: int) -> List[Tuple[int, int]]:
        """Return the horizontal moves for the rook and queen."""
        
        for col in range(COLS):
            if col == initial_col:
                continue
            if in_range(col):
                yield (initial_row, col)
                
def all_vertical_moves(initial_row: int, initial_col: int) -> List[Tuple[int, int]]:
    """Return the vertical moves for the rook and queen."""
    
    for row in range(ROWS):
        if row == initial_row:
            continue
        if in_range(row):
            yield (row, initial_col)

def all_diagonal_moves(initial_row: int, initial_col: int) -> List[Tuple[int, int]]:
    """Return the diagonal moves for the bishop and queen."""
    
    for row in range(ROWS):
        for col in range(COLS):
            if abs(row - initial_row) == abs(col - initial_col):
                yield (row, col)
                
def in_range(*args):
        """Check if the square is in range."""
        for arg in args:
            if not 0 <= arg <= 7:
                return False
        return True