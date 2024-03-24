import pygame
import sys

# Var initialization
user_x = 0
grid_size = 20

class Player:
    def __init__(self, health:int,
                 damage:int,
                 score:int,
                 x_pos:int,
                 x_dir:int):

        self.health = health
        self.damage = damage
        self.score = score
        self.x_pos = x_pos
        self.x_dir = x_dir


def main():
    global screen
    score = 0
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    pygame.display.set_caption("Space Invaders")


    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw()

        pygame.display.flip()

        clock = pygame.time.Clock()
        clock.tick(15)

def draw():
    # Draw grid
    for x in range(30):
        for y in range(30):
            rect = pygame.Rect(x*grid_size, y*grid_size, grid_size, grid_size)
            pygame.draw.rect(screen, (5,5,5), rect, 1)

if __name__ == "__main__":
    main()
