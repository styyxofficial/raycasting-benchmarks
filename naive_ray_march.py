import pygame
from pygame import Color
import math
class NaiveRayMarch():
    def __init__(self, display_size):
        self.display_size = display_size # size of display
        self.x = display_size[0]//2 # Starting x location of ray
        self.y = display_size[1]//2 # Starting y location of ray
        self.step = 30 # Interval between the angles
        self.angles = list(range(0, 360, self.step))
        self.end_points = [0] * len(self.angles)


    def calculate(self, surface):
        for i in range(len(self.angles)):
            theta = math.radians(self.angles[i]) # angle in radians
            curr_x, curr_y = self.x, self.y # starting position of ray
            step_x = math.cos(theta)
            step_y = math.sin(theta)

            while curr_x>=0 and curr_x<self.display_size[0] and curr_y >=0 and curr_y<self.display_size[1]:
                # get the pixel color at the curr position
                pixel_color = tuple(surface.get_at((int(round(curr_x)), int(round(curr_y))))) 
                
                if pixel_color == (0, 0, 0, 255):
                    break
                else:
                    curr_x += step_x
                    curr_y -= step_y

            self.end_points[i] = [int(round(curr_x)), int(round(curr_y))]

    def draw(self, surface):
        for x, y in self.end_points:
            pygame.draw.line(surface, Color(0,0,255), (self.x, self.y), (x, y))
            pygame.draw.circle(surface, Color(255, 0, 0), (x, y), 2)