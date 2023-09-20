from unittest import mock, TestCase
from piece import Piece, Pawn, Bishop
from board import Board
# from src.tests.test import BaseTest

class TestBishopMovement(TestCase):
    
    def setUp(self):
        with mock.patch("board.Board._place_pieces"):
            self.board = Board()
        self.bishop = self._populate_square(3, 3, Bishop("white"))
            
    def test_bishop__handle_bishop_moves(self):
        
        self.board.calculate_moves(self.bishop, 3, 3)
        self.assertEqual(len(self.bishop.moves), 13)
        
    def test_bishop__handle_bishop_moves__blocked_by_rival_piece(self):
        
        self.board.calculate_moves(self.bishop, 3, 3)
        self.assertEqual(len(self.bishop.moves), 13)
        
        self.bishop.moves = []
        self._populate_square(5, 5, Pawn("black"))
        
        self.board.calculate_moves(self.bishop, 3, 3)
        self.assertEqual(len(self.bishop.moves), 8)
        
    def test_bishop__handle_bishop_moves__blocked_by_team_piece(self):
        
        self.board.calculate_moves(self.bishop, 3, 3)
        self.assertEqual(len(self.bishop.moves), 13)
        self.bishop.moves = []
        
        self._populate_square(5, 5, Pawn("white"))
        
        self.board.calculate_moves(self.bishop, 3, 3)
        self.assertEqual(len(self.bishop.moves), 8)
    
    def _populate_square(self, row: int, col: int, piece: Piece):
        self.board.squares[row][col].piece = piece
        return self.board.squares[row][col].piece