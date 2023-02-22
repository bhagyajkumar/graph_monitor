import pygame
import sys

ACTIVE_COLOR = pygame.Color('lightskyblue3')
PASSIVE_COLOR = pygame.Color('chartreuse4')

class GraphMonitor():
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.input_active = False
        
    def place_input(self):
        self.input_box = pygame.Rect(20, 20, 140, 32)
        self.input_color = ACTIVE_COLOR if self.input_active else PASSIVE_COLOR
        pygame.draw.rect(self.screen, self.input_color, self.input_box)
        
    def render(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.input_box.collidepoint(event.pos):
                    self.input_active = not self.input_active
                else:
                    self.input_active = False

        self.screen.fill((255,255,255))
        self.place_input()
        self.clock.tick()


pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([600, 500])

graph_monitor = GraphMonitor(screen, clock)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    graph_monitor.render(events)
    pygame.display.flip()

        
  
