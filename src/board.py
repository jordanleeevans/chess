from settings import *
from square import Square
from piece import *
from move import Move

class Board:

    def __init__(self):
        self.squares = []
        self.last_move = None
        self._create_board()
        self._place_pieces("white")
        self._place_pieces("black")

    def _create_board(self):
        """Create the board with squares."""
        self.squares = [
            [Square(row, col) for col in range(COLS)]
            for row in range(ROWS)
        ]
        
    def _place_pieces(self, colour:str):
        """Place pieces on the board."""

        # Want pawns to be placed on file 2 for white and file 7 for black
        (row_pawn, row_other) = (6, 7) if colour == "white" else (1, 0)

        # Pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(colour))
        # Rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(colour))
        self.squares[row_other][COLS - 1] = Square(row_other, COLS - 1, Rook(colour))

        # Knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(colour))
        self.squares[row_other][COLS - 2] = Square(row_other, COLS - 2, Knight(colour))

        # Bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(colour))
        self.squares[row_other][COLS - 3] = Square(row_other, COLS - 3, Bishop(colour))

        # King and Queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(colour))
        self.squares[row_other][COLS - 4] = Square(row_other, COLS - 4, King(colour))
        
    def calculate_moves(self, piece: Piece, initial_row: int, initial_col: int):
        
        if isinstance(piece, Pawn):
            self._handle_pawn_moves(piece, initial_row, initial_col)
        elif isinstance(piece, Knight):
            self._handle_knight_moves(piece, initial_row, initial_col)
        elif isinstance(piece, King):
            self._handle_king_moves(piece, initial_row, initial_col)
        elif isinstance(piece, Rook):
            self._handle_rook_moves(piece, initial_row, initial_col)
        elif isinstance(piece, Bishop):
            self._handle_bishop_moves(piece, initial_row, initial_col)
        elif isinstance(piece, Queen):
            self._handle_queen_moves(piece, initial_row, initial_col)
        else:
            raise ValueError(f"Invalid piece: {piece}")
        
    
    def move_piece(self, piece:Piece, move:Move):
        
        self.last_move = move
        
        self.squares[move.initial_square.row][move.initial_square.col].piece = None
        self.squares[move.target_square.row][move.target_square.col].piece = piece
        
        piece.moved = True
        
        piece.clear_moves()
        
        
    def valid_move(self, piece:Piece, move:Move):
        return move in piece.moves
    
    def _handle_pawn_moves(self, piece:Pawn, initial_row:int, initial_col:int):
        """Handle complex pawn moves, such as en passant and promotion."""
        
        for move in piece.possible_moves(initial_row, initial_col):
            
            target_row, target_col = move
            
            target_square = self.squares[target_row][target_col]
            
            # If the pawn is moving diagonally, then it must be capturing a piece
            if target_col != initial_col:
                
                # If the target square is not occupied, then it is not a valid move
                if not target_square.occupied:
                    continue 
                
                self._add_move(piece, initial_row, initial_col, target_row, target_col)
                
            # If the pawn is moving vertically, then it must be moving to an empty square
            if target_square.occupied:
                break
            
            self._add_move(piece, initial_row, initial_col, target_row, target_col)
                
    def _handle_knight_moves(self, piece:Piece, initial_row:int, initial_col:int):
        """Check if current piece is a knight, handle jumping over pieces."""
        for move in piece.possible_moves(initial_row, initial_col):
            
            target_row, target_col = move
            target_square = self.squares[target_row][target_col]
            
            if target_square.empty_or_opposing(piece.colour):
                
                if not self.squares[target_row][initial_col].occupied:
                    pass
                if not self.squares[initial_row][target_col].occupied:
                    pass
                
                self._add_move(piece, initial_row, initial_col, target_row, target_col)
                
    def _handle_king_moves(self, piece:Piece, initial_row:int, initial_col:int):
        """Check if current piece is a king, handle castling."""
        
        for move in piece.possible_moves(initial_row, initial_col):
            
            target_row, target_col = move
            target_square = self.squares[target_row][target_col]
            
            if target_square.empty_or_opposing(piece.colour):
                
                self._add_move(piece, initial_row, initial_col, target_row, target_col)
                
        
    def _handle_rook_moves(self, piece:Piece, initial_row:int, initial_col:int):
        
        for move_increment in piece.possible_moves(initial_row, initial_col):
            
            row_increment, col_increment = move_increment
            
            target_increment = [initial_row + row_increment, initial_col + col_increment]
            
            while True:
                
                if not in_range(*target_increment):
                    break
                
                target_row, target_col = target_increment
                target_square = self.squares[target_row][target_col]
                
                if not target_square.occupied:
                    self._add_move(piece, initial_row, initial_col, target_row, target_col)
                
                if target_square.has_opposing_piece(piece.colour):
                    self._add_move(piece, initial_row, initial_col, target_row, target_col)
                    break
                
                if target_square.has_team_piece(piece.colour):
                    break
                
                target_increment = [target_increment[0] + row_increment, target_increment[1] + col_increment]
                    
    def _handle_bishop_moves(self, piece:Piece, initial_row:int, initial_col:int):
        
        # TODO: if piece moves onto square in possible moves, then we need to make sure that the bishop can not move past it
        for move_increment in piece.possible_moves(initial_row, initial_col):
            
            row_increment, col_increment = move_increment
            
            target_increment = [initial_row + row_increment, initial_col + col_increment]
            
            while True:
                
                if not in_range(*target_increment):
                    break
                
                target_row, target_col = target_increment
                target_square = self.squares[target_row][target_col]
                
                if not target_square.occupied:
                    self._add_move(piece, initial_row, initial_col, target_row, target_col)
                
                if target_square.has_opposing_piece(piece.colour):
                    self._add_move(piece, initial_row, initial_col, target_row, target_col)
                    break
                
                if target_square.has_team_piece(piece.colour):
                    break
                
                target_increment = [target_increment[0] + row_increment, target_increment[1] + col_increment]
                
    def _handle_queen_moves(self, piece:Piece, initial_row:int, initial_col:int):
        
        for move in piece.possible_moves(initial_row, initial_col):
            
            target_row, target_col = move
            target_square = self.squares[target_row][target_col]
            
            if target_square.empty_or_opposing(piece.colour):
                
                self._add_move(piece, initial_row, initial_col, target_row, target_col)
                
    def _add_move(self, piece:Piece, initial_row:int, initial_col:int, target_row:int, target_col:int):
        initial_square = Square(initial_row, initial_col)
        target_square = Square(target_row, target_col)
        move = Move(initial_square, target_square)
        piece.add_move(move)