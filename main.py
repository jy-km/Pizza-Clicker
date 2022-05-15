import pygame
import math
pygame.init()

width = 500
height = 500
screen = pygame.display.set_mode([width, height])
running = True

pizza = pygame.image.load('pizza.png')
pizza = pygame.transform.scale(pizza, (200,200))

while running == True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill((255,255,255))
  screen.blit(pizza,(150,150))
  pygame.display.flip()

pygame.quit()