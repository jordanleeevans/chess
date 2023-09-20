import pygame

from board import Board
from dragger import Dragger
from piece import *

from settings import (
    ROWS,
    COLS,
    SQUARE_SIZE,
    DARK_GREEN,
    LIGHT_GREEN,
)

class Game:

    def __init__(self, board: Board, dragger: Dragger):
        self.board = board
        self.dragger = dragger

    def show_background(self, screen: pygame.Surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = LIGHT_GREEN
                else:
                    color = DARK_GREEN

                rectangle = (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(screen, color, rectangle)

    def show_pieces(self, screen: pygame.Surface):
        for row in range(ROWS):
            for col in range(COLS):
                if not self.board.squares[row][col].occupied:
                    continue
                piece = self.board.squares[row][col].piece
                self._render_piece_image(piece, screen, col, row)
                
    def show_moves(self, screen: pygame.Surface):
        if self.dragger.dragging:
            piece = self.dragger.piece
            for move in piece.moves:
                self._render_move(screen, move)

    def _render_piece_image(self, piece: Piece, screen: pygame.Surface, col: int, row: int):
        
        """Render the image of the piece."""
        
        if piece is not self.dragger.piece:
            piece.set_image(size=80)
            image = pygame.image.load(piece.image)
            image_center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
            piece.image_rect = image.get_rect(center=image_center)
            screen.blit(image, piece.image_rect)
        
    def _render_move(self, screen: pygame.Surface, move: Move):
        highlight_colour = '#C86464' if (move.target_square.row + move.target_square.col) % 2 == 0 else '#F2AFAF'
        rectangle = (move.target_square.col * SQUARE_SIZE, move.target_square.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
        pygame.draw.rect(screen, highlight_colour, rectangle)