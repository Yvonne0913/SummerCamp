import pygame
import sys
import random
from Colors import *

pygame.init()

WIDTH, HEIGHT = 700, 700
window_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("神準點擊手")
background = pygame.Rect(0, 0, 1000, 1000)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 40)
score = 0
blocks = []
time = 60
life = 10
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
    time -= (1 / 60)
    window_surface.fill(Colors.LIGHTBLUE)

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
                    score = score + 1
                    life = life + 1
                    break
            life -= 1
    for block in blocks:
        pygame.draw.rect(window_surface, Colors.YELLOW, block)
    text = font.render("score:" + str(score), True, Colors.WHITE)
    window_surface.blit(text, (0, 0))
    texttime = font.render("time:" + str(int(time)), True, Colors.WHITE)
    window_surface.blit(texttime, (0, 30))
    textlife = font.render("life:" + str(int(life)), True, Colors.WHITE)
    window_surface.blit(textlife, (0, 60))

  
    


    pygame.display.update()
    clock.tick(60)