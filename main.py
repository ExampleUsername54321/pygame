import pygame

# 1. Initialize all imported pygame modules
pygame.init()

# 2. Set up the display window (Width, Height)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My First Pygame!")

# 3. Create a clock object to manage frame rate
clock = pygame.time.Clock()

# Game variables
player_x = 400
player_y = 300
player_speed = 5

# 4. The Core Game Loop
running = True
while running:
    # --- EVENT HANDLING ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- GAME LOGIC ---
    # Read keyboard inputs for continuous movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # --- DRAWING / RENDERING ---
    # Always clear the screen with a background color first (RGB format)
    screen.fill((40, 44, 52))  # Dark gray background

    # Draw a simple player character (a blue rectangle)
    # pygame.draw.rect(surface, color, (x, y, width, height))
    pygame.draw.rect(screen, (0, 122, 255), (player_x, player_y, 50, 50))

    # Update the full display Surface to the screen
    pygame.display.flip()

    # --- FRAME RATE CONTROL ---
    clock.tick(60)  # Limits the game to 60 frames per second

# Clean up and close the window
pygame.quit()
