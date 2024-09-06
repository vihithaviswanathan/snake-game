import pygame
import sys
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize snake
snake = [(100, 100), (90, 100), (80, 100)]
snake_direction = (GRID_SIZE, 0)

# Initialize food
food = (random.randrange(1, (WIDTH//GRID_SIZE)) * GRID_SIZE,
        random.randrange(1, (HEIGHT//GRID_SIZE)) * GRID_SIZE)

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, GRID_SIZE):
                snake_direction = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -GRID_SIZE):
                snake_direction = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and snake_direction != (GRID_SIZE, 0):
                snake_direction = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-GRID_SIZE, 0):
                snake_direction = (GRID_SIZE, 0)
# Move the snake
new_head = ((snake[0][0] + snake_direction[0]) // GRID_SIZE * GRID_SIZE,
            (snake[0][1] + snake_direction[1]) // GRID_SIZE * GRID_SIZE)
snake.insert(0, new_head)

# Check for collisions with itself
if new_head in snake[1:]:
    pygame.quit()
    sys.exit()

# Draw everything
screen.fill(BLACK)

# Draw snake
for segment in snake:
    pygame.draw.rect(screen, WHITE, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))    # Draw food
    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))

    pygame.display.flip()
    clock.tick(FPS)
