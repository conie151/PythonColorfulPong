import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BALL_RADIUS_RANGE = (50, 80)
BALL_SPEED_RANGE = (-5, 5)
NUM_BALLS = 25

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pingPong++")
clock = pygame.time.Clock()

# Ball class
class Ball:
    def __init__(self):
        self.radius = random.randint(*BALL_RADIUS_RANGE)
        self.x = random.randint(100, WIDTH - 100)
        self.y = random.randint(100, HEIGHT - 100)
        self.mass = 1 + self.radius / 10 - 3
        self.vx = random.uniform(*BALL_SPEED_RANGE)
        self.vy = random.uniform(*BALL_SPEED_RANGE)
        self.color = self.random_rgb()
        self.opacity = 0

    def random_rgb(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Initialize balls
balls = [Ball() for _ in range(NUM_BALLS)]

# Function to check collision
def is_colliding(ball1, ball2):
    distance = math.sqrt((ball1.x - ball2.x) ** 2 + (ball1.y - ball2.y) ** 2)
    return distance <= ball1.radius + ball2.radius

# Main loop
running = False
count = 0

def start():
    global running
    running = True

def resolve_collision(ball1, ball2):
    # Add collision resolution logic here
    pass

while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True

    screen.fill(WHITE)

    for ball in balls:
        ball.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
