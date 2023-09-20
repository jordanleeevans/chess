from piece import Piece

class Square:

    def __init__(self, row:int, col:int, piece:Piece=None):
        self.row = row
        self.col = col
        self.piece = piece
        
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
    
    @property
    def occupied(self):
        return isinstance(self.piece, Piece)
    
    # @property
    def has_team_piece(self, colour:str):
        return self.occupied and self.piece.colour == colour
    
    def has_opposing_piece(self, colour:str):
        return self.occupied and self.piece.colour != colour
    
    # @property
    def empty_or_opposing(self, colour:str):
        return not self.has_team_piece(colour) or not self.occupied
