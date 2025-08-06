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

blocks = []
for i in range(5):
    new_block = pygame.Rect((random.randint(0, 400), random.randint(0, 400), 100, 100))
    blocks.append(new_block)
while True:
    window_surface.fill(Colors.WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  
            for block in blocks:
                if block.collidepoint(mouse_pos):
                    blocks.remove(block)

                    while True:
                        new_block = pygame.Rect(random.randint(0, 400), random.randint(0, 400), 100, 100)
                        for block in blocks:
                            if new_block.colliderect(block):
                   # block = pygame.Rect((random.randint(0, 400),random.randint(0, 400), 100, 100))        
      
            
            
    #pygame.draw.rect(window_surface, Colors.RED, block)

    pygame.display.update()
    clock.tick(60)