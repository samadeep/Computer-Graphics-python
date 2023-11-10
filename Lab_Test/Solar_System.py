import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
width, height = 800, 800
center_x, center_y = width // 2, height // 2

# Colors
white = (255, 255, 255)
yellow = (255, 255, 0)
gray = (192, 192, 192)

# Create a window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Solar System")

# Planet data (distance from the sun and radius)
planets = [
    {"name": "Sun", "color": yellow, "distance": 0, "radius": 30},
    {"name": "Mercury", "color": gray, "distance": 70, "radius": 5},
    {"name": "Venus", "color": (255, 215, 0), "distance": 110, "radius": 7},
    {"name": "Earth", "color": (0, 0, 255), "distance": 150, "radius": 7},
    {"name": "Mars", "color": (255, 0, 0), "distance": 220, "radius": 6},
]

# Run the solar system simulation
running = True
clock = pygame.time.Clock()
angle = 0  # Initial angle

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(white)

    for planet in planets:
        # Calculate the planet's position
        distance = planet["distance"]
        x = center_x + distance * math.cos(math.radians(angle))
        y = center_y + distance * math.sin(math.radians(angle))

        # Draw the planet
        pygame.draw.circle(screen, planet["color"], (int(x), int(y)), planet["radius"])

        # Update the angle for the next frame (simulating rotation)
        angle += 1


    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
