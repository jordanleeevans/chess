import unittest
from board import Board
from piece import Pawn, Knight, Bishop, Rook, Queen, King
class TestBoard(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        
    def test_board__correct_square_placement(self):
        
        squares = self.board.squares
        
        self.assertEqual(len(squares), 8)
        
    def test_board__squares__pieces_populated_correctly(self):
        
        squares = self.board.squares
        
        # Check Pawns
        for col in range(8):
            self.assertIsInstance(squares[1][col].piece, Pawn)
            self.assertEqual(squares[1][col].piece.colour, "black")
            self.assertIsInstance(squares[6][col].piece, Pawn)
            self.assertEqual(squares[6][col].piece.colour, "white")
    
        # Check Rooks
        self.assertIsInstance(squares[0][7].piece, Rook)
        self.assertEqual(squares[0][7].piece.colour, "black")
    
        self.assertIsInstance(squares[7][0].piece, Rook)
        self.assertEqual(squares[7][0].piece.colour, "white")
        
        # Check Knights
        self.assertIsInstance(squares[0][1].piece, Knight)
        self.assertEqual(squares[0][1].piece.colour, "black")
        
        self.assertIsInstance(squares[7][6].piece, Knight)
        self.assertEqual(squares[7][6].piece.colour, "white")
        
        # Check Bishops
        self.assertIsInstance(squares[0][2].piece, Bishop)
        self.assertEqual(squares[0][2].piece.colour, "black")
        
        self.assertIsInstance(squares[7][5].piece, Bishop)
        self.assertEqual(squares[7][5].piece.colour, "white")
        
        # Check Queen
        self.assertIsInstance(squares[0][3].piece, Queen)
        self.assertEqual(squares[0][3].piece.colour, "black")
        
        self.assertIsInstance(squares[7][3].piece, Queen)
        self.assertEqual(squares[7][3].piece.colour, "white")
        
        # Check King
        self.assertIsInstance(squares[0][4].piece, King)
        self.assertEqual(squares[0][4].piece.colour, "black")
        
        self.assertIsInstance(squares[7][4].piece, King)
        self.assertEqual(squares[7][4].piece.colour, "white")
        
    def test_board__calculate_moves__pawn(self):
        
        pawn_a2 = self.board.squares[1][0].piece
        valid_moves = pawn_a2.moves
        
        self.assertIn(
            valid_moves,
            [
                (2, 0),
                (3, 0)
            ]
        )
        