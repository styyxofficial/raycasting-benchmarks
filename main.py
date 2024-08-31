import pygame
from pygame import Color
import sys
from map import Map
from naive_ray_march import NaiveRayMarch


class App:
    def __init__(self):
        self._running = False
        self.size = self.width, self.height = 600, 400
        self.FPS = 60
        

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
            self.on_cleanup()

    def on_cleanup(self):
        pygame.quit()
        sys.exit()

    def on_execute(self):
        self._running = True

        pygame.init()
        clock = pygame.time.Clock()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

        # Create Assets
        background_map = Map(self.size)
        naive_ray_march = NaiveRayMarch(self.size)

        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)

            self._display_surf.fill(Color(0, 0, 0))
            background_map.draw(self._display_surf)

            # Calculate distances and draw
            naive_ray_march.calculate(self._display_surf)
            naive_ray_march.draw(self._display_surf)

            pygame.display.update()
            clock.tick(self.FPS)

        self.on_cleanup()


    
if __name__ == '__main__':
    print("hello world")
    app = App()
    app.on_execute()
