
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Ludo Board")


WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

screen.fill(WHITE)

pygame.draw.rect(screen, BLACK, (50, 50, 300, 300), 5)

pygame.draw.rect(screen, GREEN, (50, 50, 100, 100), 2)
pygame.draw.rect(screen, BLUE, (250, 50, 100, 100), 2)
pygame.draw.rect(screen, YELLOW, (50, 250, 100, 100), 2)
pygame.draw.rect(screen, RED, (250, 250, 100, 100), 2)

pygame.draw.line(screen, GREEN, (100, 50), (100, 150), 2)
pygame.draw.line(screen, BLUE, (300, 50), (300, 150), 2)
pygame.draw.line(screen, GREEN, (50, 100), (150, 100), 2)
pygame.draw.line(screen, YELLOW, (50, 300), (150, 300), 2)
pygame.draw.line(screen, BLUE, (250, 100), (350, 100), 2)
pygame.draw.line(screen, YELLOW, (250, 300), (350, 300), 2)
pygame.draw.line(screen, RED, (100, 250), (100, 350), 2)
pygame.draw.line(screen, RED, (300, 250), (300, 350), 2)

pygame.draw.circle(screen, GREEN, (100, 100), 10)
pygame.draw.circle(screen, BLUE, (300, 100), 10)
pygame.draw.circle(screen, YELLOW, (100, 300), 10)
pygame.draw.circle(screen, RED, (300, 300), 10)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
sys.exit()