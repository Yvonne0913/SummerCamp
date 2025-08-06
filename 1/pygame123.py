import pygame
import sys
import random
from Colors import *

pygame.init()

WIDTH, HEIGHT = 500, 500
window_surface = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("神準點擊手")

clock = pygame.time.Clock()


blocks = []
for i in range(5):
    while True:
        new_block = pygame.Rect(random.randint(0, 400), random.randint(0, 400), 100, 100)
        for block in blocks:
            if new_block.colliderect(block):  
                break
        else:
            blocks.append(new_block)
            break

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
                                break
                        else:
                            blocks.append(new_block)
                            break
    
    
    for block in blocks:
        pygame.draw.rect(window_surface, Colors.RED, block)
    
    
    pygame.display.update()
    clock.tick(60)