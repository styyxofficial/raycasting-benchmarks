import pygame
from pygame import Color, Rect

class Map():
    def __init__(self, screen_size):
        # Border is how much space to leave from the outside edge of the display
        self.border = 10
        self.screen_size = screen_size
        print(screen_size)

    def draw(self, surface):
        pygame.draw.rect(surface, Color(255, 255, 255), Rect(self.border, self.border, self.screen_size[0]-self.border*2, self.screen_size[1]-self.border*2))
        pygame.draw.rect(surface, Color(0, 0, 0), Rect(80, 80, 40, 40))
        pygame.draw.rect(surface, Color(0, 0, 0), Rect(480, 80, 40, 40))
        pygame.draw.rect(surface, Color(0, 0, 0), Rect(280, 80, 40, 40))
        pygame.draw.rect(surface, Color(0, 0, 0), Rect(280, 280, 40, 40))
        pygame.draw.rect(surface, Color(0, 0, 0), Rect(80, 280, 40, 40))
        pygame.draw.rect(surface, Color(0, 0, 0), Rect(480, 280, 40, 40))