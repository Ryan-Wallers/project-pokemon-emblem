# All this stuff is what was used to test if pygame works
'''# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()'''

# Go go gadget copy and paste!
# But like, not actually I just had to follow a guide please don't fail me
# I'm like, 95% sure the majority of articles online are entirely AI generated

import pygame
import time

# Initialize Pygame
pygame.init()

# Constants for screen dimensions
TILE_SIZE = 32
MAP_WIDTH = 10
MAP_HEIGHT = 10

# Calculate screen size
SCREEN_WIDTH = TILE_SIZE * MAP_WIDTH
SCREEN_HEIGHT = TILE_SIZE * MAP_HEIGHT

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tile-based Game")

# Load tile images
grass_image = pygame.image.load("grass.png") #Tile images size must match the tile size in pixels
water_image = pygame.image.load("water.png")
wall_image = pygame.image.load("wall.png")
# You can organize these images in a dictionary for easy access
tile_images = {
    0: grass_image,
    1: water_image,
    2: wall_image,
}

'''Define the tile types
GRASS = 0
WATER = 1
WALL = 2'''

# Simple tile map (5x3)
'''tile_map = [
    [0, 0, 0, 1, 2],
    [0, 1, 1, 1, 2],
    [2, 1, 0, 0, 0],
]'''
# Simple tile map (10x10)
tile_map = [
    [0,0,0,1,2,1,1,0,1,0],
    [0,0,0,1,2,1,0,0,0,0],
    [0,0,1,0,0,0,0,0,1,1],
    [2,2,2,0,0,0,1,1,1,1],
    [0,1,1,0,0,2,1,1,1,0],
    [0,1,0,0,0,2,1,1,0,0],
    [0,1,0,0,0,2,2,1,1,0],
    [0,1,1,0,0,0,0,2,2,2],
    [0,1,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,1,1,1,1,0],
]


def get_tile_type(x, y, tile_map):
    """Return the type of tile at given coordinates."""
    if x < len(tile_map[0]) and y < len(tile_map) and x >= 0 and y >= 0:
        return tile_map[y][x]
    else:
        return 2

# Function to draw the tile map
def draw_tile_map(screen, tile_map, tile_images):
    for y, row in enumerate(tile_map):
        for x, tile_type in enumerate(row):
            # Calculate the position on the screen
            tile_x = x * TILE_SIZE
            tile_y = y * TILE_SIZE
            
            # Draw the corresponding tile image
            screen.blit(tile_images[tile_type], (tile_x, tile_y))

def can_move_to(x, y, tile_map):
    """Check if the player can move to the specified tile."""
    tile_type = get_tile_type(x, y, tile_map)
    return tile_type != 2  # Assuming 2 indicates an obstacle (wall)

class Pokemon:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
    def move(self, dx, dy, tile_map):
        new_x = self.x + dx
        new_y = self.y + dy
        if can_move_to(new_x, new_y, tile_map):
            self.x = new_x
            self.y = new_y

player = Pokemon(1, 1, 1)  # Start at tile (1, 1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.move(0, -1, tile_map)
    if keys[pygame.K_DOWN]:
        player.move(0, 1, tile_map)
    if keys[pygame.K_LEFT]:
        player.move(-1, 0, tile_map)
    if keys[pygame.K_RIGHT]:
        player.move(1, 0, tile_map)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Does what it says on the tin
    draw_tile_map(screen, tile_map, tile_images)

    # Draw the player (for simplicity, we can represent the player as a rectangle)
    player_rect = pygame.Rect(player.x * TILE_SIZE, player.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    pygame.draw.rect(screen, (255, 0, 0), player_rect)  # Red square for the player

    # Update the display
    pygame.display.flip()

    # Waits for a tenth of a second to prevent excessive inputs until a proper solution is found
    time.sleep(1/10)

# Quit Pygame
pygame.quit()