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
# Guide is https://www.codersjungle.com/2025/01/27/creating-tile-based-games-with-pygame/

import pygame

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

# Define the tile types
TILE_GRASS = 0
TILE_WATER = 1
TILE_WALL = 2

# Simple tile map (5x3)
tile_map = [
    [TILE_GRASS, TILE_GRASS, TILE_GRASS, TILE_WATER, TILE_WALL],
    [TILE_GRASS, TILE_WATER, TILE_WATER, TILE_WATER, TILE_WALL],
    [TILE_WALL, TILE_GRASS, TILE_GRASS, TILE_GRASS, TILE_GRASS],
]

# Function to draw the tile map
def draw_tile_map(screen, tile_map, tile_images):
    for y, row in enumerate(tile_map):
        for x, tile_type in enumerate(row):
            # Calculate the position on the screen
            tile_x = x * TILE_SIZE
            tile_y = y * TILE_SIZE
            
            # Draw the corresponding tile image
            screen.blit(tile_images[tile_type], (tile_x, tile_y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Does what it says on the tin
    draw_tile_map(screen, tile_map, tile_images)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()