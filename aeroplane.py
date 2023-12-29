import random
import pygame

# Initialize Pygame and create a window
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Load images (replace with actual file paths)
airplane_image = pygame.image.load("D:/AzlanCoding/Python/azlanpython2024/airplane.png")
# Scale the image to new size, e.g., 100x50 pixels
airplane_image = pygame.transform.scale(airplane_image, (100, 50))


# Define constants for movement
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Define the Airplane class
class Airplane:
    def __init__(self):
        self.position = [400, 300]
        self.speed = 5
        self.lights_on = False
        self.control_difficulty = 1  # Normal difficulty

    def draw(self, screen):
        screen.blit(airplane_image, self.position)

    def update(self, weather, direction):
        # Update based on weather
        if weather.type == "storm":
            self.control_difficulty = 4
        elif weather.type == "windy":
            self.control_difficulty = 2
        else:
            self.control_difficulty = 1

        # Move the airplane based on control difficulty and direction
        self.position[0] += direction[0] * self.speed / self.control_difficulty
        self.position[1] += direction[1] * self.speed / self.control_difficulty

# Define the Weather class
class Weather:
    def __init__(self):
        self.type = "clear"

    def randomize(self):
        if random.random() < 0.5:
            self.type = "storm"
        else:
            self.emergency = True

# Define the Map class
class Map:
    def __init__(self, map_image):
        self.image = map_image
        self.position = [0, 0]

    def draw(self, screen):
        screen.blit(self.image, self.position)

# Load map images (replace with actual file paths)
map_images = [pygame.image.load("D:/AzlanCoding/Python/azlanpython2024/map1.png"), pygame.image.load("D:/AzlanCoding/Python/azlanpython2024/map2.png"), pygame.image.load("D:/AzlanCoding/Python/azlanpython2024/map3.png")]

# Main game loop
airplane = Airplane()
weather = Weather()
current_map = Map(random.choice(map_images))  # Choose a random map

running = True
while running:
    direction = [0, 0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = UP
            elif event.key == pygame.K_DOWN:
                direction = DOWN
            elif event.key == pygame.K_LEFT:
                direction = LEFT
            elif event.key == pygame.K_RIGHT:
                direction = RIGHT

    # Update game elements
    weather.randomize()
    airplane.update(weather, direction)

    # Drawing
    screen.fill((0, 0, 0))  # Clear screen
    current_map.draw(screen)
    airplane.draw(screen)

    pygame.display.flip()  # Update the screen

pygame.quit()
