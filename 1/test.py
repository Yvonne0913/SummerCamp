import pygame
import sys
import random
from Colors import *

pygame.init()

WIDTH, HEIGHT = 500, 500
window_surface = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("神準點擊手")

clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 40)
while True:
    window_surface.fill(Colors.WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    text = font.render("TEXT", True, Colors.RED)
    window_surface.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2  - text.get_height() // 2))

    pygame.dsiplay.update()
    clock.tick(60)