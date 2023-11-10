import pygame
import math

# Initialize pygame
pygame.init()

# Define the dimensions of the flag
flag_width = 900
flag_height = 600

# Define colors
saffron = (255, 153, 51)
white = (255, 255, 255)
green = (19, 136, 8)
navy_blue = (0, 0, 139)

# Create a window
screen = pygame.display.set_mode((flag_width, flag_height))

# Draw the three horizontal bands
pygame.draw.rect(screen, saffron, (0, 0, flag_width, flag_height // 3))
pygame.draw.rect(screen, white, (0, flag_height // 3, flag_width, flag_height // 3))
pygame.draw.rect(screen, green, (0, 2 * flag_height // 3, flag_width, flag_height // 3))

# Draw the Ashoka Chakra
center_x = flag_width // 2
center_y = flag_height // 2
radius_outer = flag_height // 6
radius_inner = radius_outer // 12

# Draw the outer blue circle
pygame.draw.circle(screen, navy_blue, (center_x, center_y), radius_outer, width=8)

# Draw 24 spokes of the Ashoka Chakra
for i in range(24):
    angle = math.radians(i * 15)
    x2 = center_x + (radius_outer  ) * math.cos(angle)
    y2 = center_y + (radius_outer  ) * math.sin(angle)
    pygame.draw.line(screen, navy_blue, (center_x, center_y), (x2, y2), 6 )

# Update the display
pygame.display.flip()

# Run the program until the user closes the window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit pygame
pygame.quit()
