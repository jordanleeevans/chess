from unittest import mock, TestCase
from piece import Piece, Pawn
from board import Board
from parameterized import parameterized

class TestPawn(TestCase):
    
    INITIAL_PAWN_MOVES = [[1, 1], [2, 1], [3, 1]]
    LATER_PAWN_MOVES = [[1, 1], [2, 1]]
    
    def setUp(self):
        with mock.patch("board.Board._place_pieces"):
            self.board = Board()
        self.pawn = self._populate_square(1, 1, Pawn("black"))
    
    @parameterized.expand([
        (False, 1, 1, INITIAL_PAWN_MOVES), # Pawn has not moved
        (True, 1, 1, LATER_PAWN_MOVES) # Pawn has moved
    ])
    def test_pawn__possible_moves__pawn(self, moved, initial_row, initial_col, possible_moves):
        
        self.pawn.moved = moved
        self.board.calculate_moves(self.pawn, initial_row, initial_col)
        
        for move in self.pawn.moves:
            self.assertIn([move.target_square.row, move.target_square.col], possible_moves)
    
    def test_pawn_possible_moves__rival_piece(self):
        
        self._populate_square(2, 1, Pawn("white"))
        self.board.calculate_moves(self.pawn, 1, 1)
        
        for move in self.pawn.moves:
            self.assertIn([move.target_square.row, move.target_square.col], [[2, 1]])
        
    def _populate_square(self, row: int, col: int, piece: Piece):
        self.board.squares[row][col].piece = piece
        return self.board.squares[row][col].piece