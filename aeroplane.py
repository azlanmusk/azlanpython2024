import random
import pygame

# Initialize Pygame and create a window
pygame.init()
pygame.key.set_repeat(1, 10)  # Add this line
screen = pygame.display.set_mode((800, 600))

# Load images
airplane_image = pygame.image.load("D:/AzlanCoding/Python/azlanpython2024/airplane.png")
airplane_image = pygame.transform.scale(airplane_image, (100, 50))
cloud_image = pygame.image.load("D:/AzlanCoding/Python/azlanpython2024/cloud.png")
maps = [pygame.image.load("D:/AzlanCoding/Python/azlanpython2024/map1.png"), 
        pygame.image.load("D:/AzlanCoding/Python/azlanpython2024/map2.png"),
        pygame.image.load("D:/AzlanCoding/Python/azlanpython2024/map3.png")]

# Define the Airplane class
class Airplane:
    def __init__(self):
        self.position = [400, 300]  # Start position
        self.speed = 5
        self.is_flying = True
        self.in_emergency = False
        self.direction = [0, 0]  # Initial direction

    def draw(self, screen):
        # Draw the airplane image at its current position
        screen.blit(airplane_image, self.position)

    def update(self):
      self.position[0] += self.direction[0] * self.speed
      self.position[1] += self.direction[1] * self.speed
      print(f"Updating position to {self.position}")

    def initiate_emergency_landing(self, runway):
        self.in_emergency = True
        self.direction = [0, -1]  # Direct the airplane towards the runway for landing
        self.speed = 2  # Slow down for landing

    def check_runway(self, runway):
        if runway.rect.collidepoint(self.position[0], self.position[1]):
            self.is_flying = False
            print("Airplane has landed on the runway.")

# Define the Runway class
class Runway:
    def __init__(self):
        self.rect = pygame.Rect(300, 500, 200, 100)  # Modify as needed

    def draw(self, screen):
        pygame.draw.rect(screen, (128, 128, 128), self.rect)
        # Draw white lines
        pygame.draw.line(screen, (255, 255, 255), (300, 500), (300, 600), 5)  # Left line
        pygame.draw.line(screen, (255, 255, 255), (500, 500), (500, 600), 5)  # Right line

# Define the Weather class
class Weather:
    def __init__(self):
        self.type = "clear"
        self.emergency = False

    def randomize(self):
        # Randomize weather and emergency conditions
        self.type = "storm" if random.random() < 0.5 else "clear"
        self.emergency = True if random.random() < 0.2 else False

    def draw(self, screen):
        if self.type == "storm":
            screen.blit(cloud_image, (100, 50))

# Define the Map class
class Map:
    def __init__(self, image):
        self.image = image

    def draw(self, screen):
        screen.blit(self.image, (0, 0))

# Initialize game elements
airplane = Airplane()
weather = Weather()
current_map = Map(random.choice(maps))
runway = Runway()

# Before the main game loop
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print("Key pressed")
            if event.key == pygame.K_UP:
                airplane.direction = [0, -1]
                print("Moving Up")
            elif event.key == pygame.K_DOWN:
                airplane.direction = [0, 1]
            elif event.key == pygame.K_LEFT:
                airplane.direction = [-1, 0]
            elif event.key == pygame.K_RIGHT:
                airplane.direction = [1, 0]
        elif event.type == pygame.KEYUP:
            airplane.direction = [0, 0]  # Stop moving when the key is released

    
    # Update game elements
    weather.randomize()
    airplane.update()
    if weather.emergency and airplane.is_flying:
        airplane.initiate_emergency_landing(runway)
    airplane.check_runway(runway)

    # Drawing
    screen.fill((0, 0, 0))  # Clear screen
    current_map.draw(screen)
    runway.draw(screen)
    airplane.draw(screen)

    pygame.display.flip()  # Update the screen
    clock.tick(60)

pygame.quit()