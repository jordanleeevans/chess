import pygame
import sys
from settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    TITLE
)
from game import Game
from dragger import Dragger
from board import Board
from square import Square
from move import Move

class MainHandler():

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.board = Board()
        self.dragger = Dragger()
        self.game = Game(self.board, self.dragger)

    def loop(self):
        """Start the main loop for the game."""
        while True:
            self._show_background()
            self.game.show_moves(self.screen)
            self._show_pieces()
            
            if self.dragger.dragging:
                self.dragger.update_blit(self.screen)

            for event in pygame.event.get():
                self._check_quit(event)

                self._handle_mouse_down(event)
                self._handle_mouse_motion(event)
                self._handle_mouse_up(event)

            self._update_screen()
                
    def _check_quit(self, event: pygame.event.Event):
        """Check if the user wants to quit the game."""
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        pygame.display.update()

    def _show_background(self):
        """Show the background."""
        self.game.show_background(self.screen)

    def _show_pieces(self):
        """Show the pieces."""
        self.game.show_pieces(self.screen)

    def _handle_mouse_down(self, event: pygame.event.Event):
        """Handle mouse down events."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.dragger.update_position(event.pos)
            row_clicked, col_clicked = self.dragger.get_clicked_position()
            if self.board.squares[row_clicked][col_clicked].occupied:
                piece = self.board.squares[row_clicked][col_clicked].piece
                self.board.calculate_moves(piece, row_clicked, col_clicked)
                self.dragger.initial_position(event.pos) # set initial position of the piece, in case of invalid move
                self.dragger.drag_piece(piece)
                self._show_background()
                self.game.show_moves(self.screen)
                self._show_pieces()
                
    def _handle_mouse_up(self, event: pygame.event.Event):
        """Handle mouse up events."""
        if event.type == pygame.MOUSEBUTTONUP:
            
            if self.dragger.dragging:
                self.dragger.update_position(event.pos)
                released_row, released_col = self.dragger.get_clicked_position()
                
                initial_square = Square(self.dragger.initial_row, self.dragger.initial_col)
                target_square = Square(released_row, released_col)
                move = Move(initial_square, target_square)
                
                if self.board.valid_move(self.dragger.piece, move):
                    
                    self.board.move_piece(self.dragger.piece, move)
                    
                    self.game.show_background(self.screen)
                    self.game.show_pieces(self.screen)
            
            self.dragger.drop_piece()

    def _handle_mouse_motion(self, event: pygame.event.Event):
        """Handle mouse motion events."""
        if event.type == pygame.MOUSEMOTION:
            if self.dragger.dragging:
                self.dragger.update_position(event.pos)
                self._show_background()
                self.game.show_moves(self.screen)
                self.game.show_pieces(self.screen)
                self.dragger.update_blit(self.screen)
    
main = MainHandler()
main.loop()
