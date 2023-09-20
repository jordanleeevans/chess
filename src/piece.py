import os
from move import Move
from utils import all_horizontal_moves, all_vertical_moves, all_diagonal_moves, in_range

class Piece:

    def __init__(self, name:str, colour:str, value:int, image_rect:str=None):
        self.name = name
        self.colour = colour
        self.value = value
        self.image_rect = image_rect
        self.set_image()
        self.moves = []
        self.moved = False
        self.captured = False

    def set_image(self, size:int=80):
        """Set the image of the piece."""
        piece_name = self.name.lower()
        self.image = os.path.join(f"assets/images/imgs-{size}px/{self.colour}_{piece_name}.png")
        
    def add_move(self, move: Move):
        self.moves.append(move)
    
    def clear_moves(self):
        self.moves = []

class Pawn(Piece):

    def __init__(self, colour: str):
        self.direction = -1 if colour == "white" else 1
        super().__init__(name="Pawn", colour=colour, value=1)

    
    def possible_moves(self, row:int, col:int):
        
        steps = 2 if not self.moved else 1
        
        start = row + self.direction
        end = row + (self.direction * (steps + 1))
        
        horizontal_moves =  [
            [i, col] for i in range(start, end, self.direction)
        ]
        
        diagonal_moves = [
            [row + self.direction, col + 1],
            [row + self.direction, col - 1]
        ]
        
        for move in diagonal_moves:
            if not in_range(*move):
                diagonal_moves.remove(move)
        
        return [
            *horizontal_moves,
            *diagonal_moves
        ]
            
        
class Knight(Piece):

    def __init__(self, colour:str):
        super().__init__(name="Knight", colour=colour, value=3)
    
    
    def possible_moves(self, row:int, col:int):
        
        for move in [
            [row + 2, col + 1],
            [row + 2, col - 1],
            [row - 2, col + 1],
            [row - 2, col - 1],
            [row + 1, col + 2],
            [row + 1, col - 2],
            [row - 1, col + 2],
            [row - 1, col - 2]
        ]:
            if in_range(*move):
                yield move
        
class Bishop(Piece):

    def __init__(self, colour:str):
        super().__init__(name="Bishop", colour=colour, value=3)
    
    
    def possible_moves(self, row:int, col:int):
         
         for move in [
            (-1, 1), # up right
            (-1, -1), # up left
            (1, 1), # down right
            (1, -1) # down left
        ]:
            yield move
        
class Rook(Piece):

    def __init__(self, colour:str):
        super().__init__(name="Rook", colour=colour, value=5)
    
    
    def possible_moves(self, row:int, col:int):
        
        for move in [
            (-1, 0), # up
            (1, 0), # down
            (0, 1), # right
            (0, -1) # left
        ]:
            yield move
    
class Queen(Piece):

    def __init__(self, colour:str):
        super().__init__(name="Queen", colour=colour, value=9)
    
    
    def possible_moves(self, row:int, col:int):
        
        for move in  [
            (-1, 0), # up
            (1, 0), # down
            (0, 1), # right
            (0, -1), # left
            (-1, 1), # up right
            (-1, -1), # up left
            (1, 1), # down right
            (1, -1) # down left
        ]:
            yield move
            

class King(Piece):

    def __init__(self, colour:str):
        super().__init__(name="King", colour=colour, value=None)
        
    
    def possible_moves(self, row:int, col:int):
        return [
            (row + 1, col),
            (row + 1, col + 1),
            (row + 1, col - 1),
            (row, col + 1),
            (row, col - 1),
            (row - 1, col),
            (row - 1, col + 1),
            (row - 1, col - 1)
        ]
