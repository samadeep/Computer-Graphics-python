import pygame
import math
import time

# Initialize Pygame
pygame.init()

# Clock parameters
clock_radius = 100
center_x, center_y = 200, 200
hour_hand_length = 60
minute_hand_length = 80
second_hand_length = 90

# Create a window
window_width, window_height = 400, 400
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Analog Clock")

# Run the clock
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current time
    current_time = time.localtime()
    hours = current_time.tm_hour
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the clock face
    pygame.draw.circle(screen, (0, 0, 0), (center_x, center_y), clock_radius, 2)
    pygame.draw.circle(screen, (0, 0, 0), (center_x, center_y), 5)

    # Calculate the angles for the clock hands
    hour_angle = math.radians(90 - (hours % 12) * 360 / 12)
    minute_angle = math.radians(90 - minutes * 360 / 60)
    second_angle = math.radians(90 - seconds * 360 / 60)

    # Draw the clock hands
    pygame.draw.line(screen, (0, 0, 0), (center_x, center_y), (center_x + hour_hand_length * math.cos(hour_angle),
                                                               center_y - hour_hand_length * math.sin(hour_angle)), 6)
    pygame.draw.line(screen, (255, 0, 0), (center_x, center_y), (center_x + minute_hand_length * math.cos(minute_angle),
                                                                center_y - minute_hand_length * math.sin(minute_angle)), 4)
    pygame.draw.line(screen, (0, 0, 255), (center_x, center_y), (center_x + second_hand_length * math.cos(second_angle),
                                                                center_y - second_hand_length * math.sin(second_angle)), 2)

    # Update the display
    pygame.display.flip()

    # Control the clock's refresh rate
    pygame.time.delay(1000)

# Quit Pygame
pygame.quit()
