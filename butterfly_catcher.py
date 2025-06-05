import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Butterfly Catcher")

# Colors
BG_COLOR = (255, 240, 245)  # light pink
BASKET_COLOR = (255, 105, 180)  # hot pink
BUTTERFLY_COLOR = (255, 182, 193)  # light pink

# Basket settings
basket_width = 80
basket_height = 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - basket_height - 10
basket_speed = 6

# Butterfly settings
butterfly_size = 30
butterflies = []
butterfly_speed = 2
spawn_event = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_event, 1000)  # spawn butterfly every second

# Score
score = 0
font = pygame.font.SysFont(None, 36)

def draw_basket(x, y):
    pygame.draw.rect(screen, BASKET_COLOR, (x, y, basket_width, basket_height))
    # Add a small handle or pattern if you want

def draw_butterfly(x, y):
    # Simple circle to represent butterfly body
    pygame.draw.circle(screen, BUTTERFLY_COLOR, (x + butterfly_size//2, y + butterfly_size//2), butterfly_size//2)
    # Add wings or details if desired

def show_score(scr):
    score_surf = font.render(f"Score: {scr}", True, (150, 0, 50))
    screen.blit(score_surf, (10, 10))

def main():
    global basket_x, score
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == spawn_event:
                # Spawn new butterfly at random x position at top
                x_pos = random.randint(0, WIDTH - butterfly_size)
                butterflies.append([x_pos, 0])

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_x > 0:
            basket_x -= basket_speed
        if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
            basket_x += basket_speed

        # Move butterflies down
        for b in butterflies[:]:
            b[1] += butterfly_speed
            # Check if caught
            if (basket_y < b[1] + butterfly_size < basket_y + basket_height) and (basket_x < b[0] + butterfly_size//2 < basket_x + basket_width):
                butterflies.remove(b)
                score += 1
            # Remove if off screen
            elif b[1] > HEIGHT:
                butterflies.remove(b)

        draw_basket(basket_x, basket_y)

        for b in butterflies:
            draw_butterfly(b[0], b[1])

        show_score(score)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
