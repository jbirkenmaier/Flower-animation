import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Growing Rose Plant Animation")

# Colors
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

clock = pygame.time.Clock()

def draw_plant(x, y, growth_stage):
    # Draw stem
    pygame.draw.rect(screen, green, (x + 10, y, 10, growth_stage * 20))

    # Draw leaves
    for i in range(growth_stage):
        pygame.draw.circle(screen, green, (x + 10, y - (i + 1) * 20), 20)

    # Draw rose blossom
    pygame.draw.circle(screen, red, (x + 10, y - growth_stage * 20 - 20), 20)

def main():
    running = True
    x_pos = 400
    y_pos = height

    growth_stage = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(white)

        draw_plant(x_pos, y_pos, growth_stage)

        if growth_stage < 10:
            growth_stage += 1

        pygame.display.flip()
        clock.tick(2)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
