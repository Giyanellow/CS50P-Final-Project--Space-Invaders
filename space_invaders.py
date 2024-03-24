import pygame
import sys

# Var initialization
user_x = 800
grid_size = 20


class Player:
    def __init__(self, health:int,
                 damage:int,
                 score:int,
                 x_pos:int):

        self.health = health
        self.damage = damage
        self.score = score
        self.x_pos = x_pos
    
    # handle border collision
    def border_collision(self):
        if self.x_pos < 0:
            self.x_pos = 0
        elif self.x_pos > 1540:
            self.x_pos = 1540
    
        


def main():
    global screen
    score = 0
    pygame.init()
    screen = pygame.display.set_mode((1600,900))
    pygame.display.set_caption("Space Invaders")
    
    player = Player(health=100, damage=10, score=0, x_pos=user_x)


    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        keys = pygame.key.get_pressed()
        key_press(keys, player)

        draw(player)

        pygame.display.update()

        clock = pygame.time.Clock()
        clock.tick(15)
        
        
def key_press(keys, player):
    if keys[pygame.K_a]:
        player.x_pos -= 20
        player.border_collision()
        print(player.x_pos)
    if keys[pygame.K_d]:
        player.x_pos += 20
        player.border_collision()
        print(player.x_pos)

def draw(player):
    screen.fill((0,0,0))
    # Draw grid
    for x in range(80):
        for y in range(80):
            rect = pygame.Rect(x*grid_size, y*grid_size, grid_size, grid_size)
            pygame.draw.rect(screen, (5,5,5), rect, 1)
            
    # Draw player
    pygame.draw.rect(screen, (255,255,255), (player.x_pos, 800, 60, 60))
    

if __name__ == "__main__":
    main()
