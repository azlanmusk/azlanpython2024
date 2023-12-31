import pygame
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('2D Ship Simulation with Coordinate Finder')

# Define the distance function
def distance(p1, p2):
    """ Calculate the distance between two points """
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

# Game Variables
running = True
ship_position = [76, 432]  # Starting position
fuel_level = 100  # Starting fuel level
SPEED = 4  # Ship movement speed

# Load map image (replace 'map_of_australia.png' with your actual map file)
map_image = pygame.image.load("D:/AzlanCoding/Python/azlanpython2024/map_of_australia.png")
map_image = pygame.transform.scale(map_image, (screen_width, screen_height))

# Load ship image (replace 'ship.png' with your actual ship file)
ship_image = pygame.image.load("D:/AzlanCoding/Python/azlanpython2024/spirit_of_tasmania.png")
ship_image = pygame.transform.scale(ship_image, (50, 50))

# City positions and labels (replace with your city positions and labels)
cities = {
    "Sydney": {"pos": (1126, 506)},
    "Melbourne": {"pos": (912, 565)},
    "Brisbane": {"pos": (1227, 355)},
    "Perth": {"pos": (88, 433)},
    "Adelaide": {"pos": (737, 484)},
    "Hobart": {"pos": (972, 676)},
    "Darwin": {"pos": (538, 82)},
}

# Define a font for city labels
font = pygame.font.Font(None, 36)

# Main Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position and print it
            x, y = pygame.mouse.get_pos()
            print(f"Mouse Clicked at: x={x}, y={y}")

    # Game Logic
    keys = pygame.key.get_pressed()
    moving = False

    if keys[pygame.K_LEFT]:
        ship_position[0] -= SPEED
        moving = True
    if keys[pygame.K_RIGHT]:
        ship_position[0] += SPEED
        moving = True
    if keys[pygame.K_UP]:
        ship_position[1] -= SPEED
        moving = True
    if keys[pygame.K_DOWN]:
        ship_position[1] += SPEED
        moving = True

    # Fuel consumption
    if moving:
        fuel_level -= 0.05
    if fuel_level <= 0:
        print("Didn't make it successfully.")
        running = False

    # Check for collision with cities and refuel
    for city, city_data in cities.items():
        dist = distance(ship_position, city_data["pos"])
        if dist < 20:  # Adjust the collision distance as needed
            fuel_level = 100  # Refuel
            print(f"Refueled at {city}!")

     # Check for reaching Hobart
    hobart_dist = distance(ship_position, cities["Hobart"]["pos"])
    if hobart_dist < 20:  # Adjust the collision distance as needed
        print("Spirit of Tasmania V has reached Hobart safely.")
        running = False

    # Drawing on the screen
    screen.fill((255, 255, 255))  # Clear screen
    screen.blit(map_image, (0, 0))  # Draw the map
    screen.blit(ship_image, ship_position)  # Draw the ship

    # Draw fuel gauge
    pygame.draw.rect(screen, (0, 255, 0), (10, 10, fuel_level, 20))

    # Draw city labels as rectangles
    for city, city_data in cities.items():
        city_rect = pygame.Rect(city_data["pos"][0] - 10, city_data["pos"][1] - 10, 20, 20)
        pygame.draw.rect(screen, (255, 0, 0), city_rect)  # Red rectangle for city marker
        city_label = font.render(city, True, (0, 0, 0))
        screen.blit(city_label, (city_data["pos"][0] - 20, city_data["pos"][1] - 40))

    pygame.display.flip()  # Update the display
    clock = pygame.time.Clock()
    clock.tick(60)  # Maintain 60 frames per second

pygame.quit()