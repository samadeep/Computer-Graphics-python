import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = WIDTH // 15  # Size of each square
BORDER_WIDTH = 5  # Border width for the board
BORDER_COLOR = (0, 0, 0)  # Border color

# Ludo board colors
GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PLAYER_COLORS = [GREEN, YELLOW, RED, BLUE]

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ludo Board")

# Draw the Ludo board
def draw_board():
    for row in range(15):
        for col in range(15):
            x = col * SQUARE_SIZE
            y = row * SQUARE_SIZE
            color = (255, 255, 255) if (row + col) % 2 == 0 else (255, 204, 153)
            pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.rect(screen, BORDER_COLOR, (x, y, SQUARE_SIZE, SQUARE_SIZE), BORDER_WIDTH)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Clear the screen
    draw_board()  # Draw the Ludo board

    # Draw player pieces (you can add more logic to position player pieces)

    pygame.display.flip()  # Update the display

# Quit Pygame
pygame.quit()
sys.exit()
