import pygame
from pygame import Color

class NaiveRayMarch():
    def __init__(self, display_size):
        self.x = display_size[0]//2
        self.y = display_size[1]//2
        self.angles = [i*30 for i in range(12)]
        self.distances = [0] * len(self.angles)


    def calculate(self, surface):
        self.distances = [(100, 100), (200, 100), (300, 100)]

    def draw(self, surface):
        for x, y in self.distances:
            pygame.draw.line(surface, Color(0,0,255), (self.x, self.y), (x, y))
            pygame.draw.circle(surface, Color(255, 0, 0), (x, y), 2)