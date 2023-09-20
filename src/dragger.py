import pygame
from settings import *
from piece import Piece

class Dragger:

    def __init__(self):
        self.initial_row = 0
        self.initial_col = 0
        self.x = 0
        self.y = 0
        self.piece = None
        self.dragging= False

    def update_position(self, position:tuple[int, int]):
        """Update the position of the dragger."""
        self.x, self.y = position

    def initial_position(self, position:tuple[int, int]):
        """Set the initial position of the dragger.
        Important for invalid moves."""
        self.initial_row = position[1] // SQUARE_SIZE
        self.initial_col = position[0] // SQUARE_SIZE

    def get_clicked_position(self):
        """Get the position of the dragger, in terms of rows and columns."""
        return (self.y // SQUARE_SIZE, self.x // SQUARE_SIZE)

    def drag_piece(self, piece:Piece):
        self.piece = piece
        self.dragging = True

    def drop_piece(self):
        self.piece = None
        self.dragging = False

    def update_blit(self, surface:pygame.Surface):
        """Update the image of the piece being dragged."""
        self.piece.set_image(size=128) 
        image = self.piece.image

        img = pygame.image.load(image)
        img_center = (self.x, self.y)
        self.piece.image_rect = img.get_rect(center=img_center)
        surface.blit(img, self.piece.image_rect)
