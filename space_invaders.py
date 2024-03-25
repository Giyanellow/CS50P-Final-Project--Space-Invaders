import pygame
import sys
import random

# Var initialization
user_x = 800
user_y = 800
attack_speed = 20
grid_size = 20

enemy_amount = 15
enemy_speed = 10
# Enemy spacing
spacing = 1600 // enemy_amount

class Attack:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

class Player:
    def __init__(self, health:int, damage:int, score:int, x_pos:int, y_pos:int=user_y):
        self._health = health
        self.damage = damage
        self.score = score
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.attacks = []  # List to store active attacks
        
    @property
    def health(self):
        return self._health    
        
    @health.setter
    def health(self, health:int):
        self._health = health
        self.max_health = health
        self.min_health = 0
    
    # handle border collision
    def border_collision(self):
        if self.x_pos < 0:
            self.x_pos = 0
        elif self.x_pos > 1540:
            self.x_pos = 1540
    
    # player attack
    def attack(self):
        # Create a new attack instance at player's position
        new_attack = Attack(self.x_pos + 20, user_y)
        self.attacks.append(new_attack)

class Enemy:
    def __init__(self, health:int, damage:int, x_pos:int, y_pos:int):
        self._health = health
        self.damage = damage
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.attacks = []  # List to store active attacks
        self.direction = 1
    
    @property
    def health(self:int):
        return self._health

    @health.setter
    def health(self, health:int):
        self._health = health
        self.max_health = health
        self.min_health = 0
    
    def border_collision(self):
        if self.x_pos < 0:
            self.x_pos = 0
        elif self.x_pos > 1540:
            self.x_pos = 1540
            
    def move(self):
        self.x_pos += self.direction * enemy_speed  # Update x_pos based on direction
        if self.x_pos > 1540 or self.x_pos < 0:  # If the enemy has reached the edge of the screen...
            self.direction *= -1  # Reverse direction
            self.y_pos += 60  # Move down

        if self.y_pos > 900:
            self.y_pos = 0
            self.x_pos = random.randint(0, 1540)
            self.health = 100
    
    def attack(self):
        # Create a new attack instance at enemy's position
        new_attack = Attack(self.x_pos + 20, self.y_pos)
        self.attacks.append(new_attack)

def main():
    global screen
    score = 0
    last_attack_time = 0
    attack_interval = 2000 # 2 seconds
    pygame.init()
    screen = pygame.display.set_mode((1600,900))
    pygame.display.set_caption("Space Invaders")
    
    player = Player(health=100, damage=100, score=0, x_pos=user_x, y_pos=user_y)
    enemies = [Enemy(health=100, damage=10, x_pos=i*spacing, y_pos=0) for i in range(enemy_amount)]

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.attack()
        
        current_time = pygame.time.get_ticks()
        if current_time - last_attack_time > attack_interval:
            for enemy in enemies:
                enemy.attack()
            last_attack_time = current_time
            
        # Lose Conditionals
        # If player loses all health
        if player.health <= 0:
            print("Game Over")
            pygame.quit()
            sys.exit()
        # If enemy crosses border
        for enemy in enemies:
            if enemy.y_pos > 625:
                print("Game Over")
                pygame.quit()
                sys.exit()
        
        # Win Conditionals
        if len(enemies) == 0:
            print("You Win!")
            pygame.quit()
            sys.exit()
        
                
        keys = pygame.key.get_pressed()
        key_press(keys, player)

        update_attacks(player, enemies=enemies)
        check_collisions(player, enemies=enemies)

        draw_background()
        draw_score(player.score)
        draw_player(player)
        draw_enemy(enemies)
        print(player.score)
        pygame.display.update()

        # Game Tick / FPS
        clock = pygame.time.Clock()
        clock.tick(120)
        
        
def key_press(keys, player):
    if keys[pygame.K_a]:
        player.x_pos -= 20
        player.border_collision()
        
    if keys[pygame.K_d]:
        player.x_pos += 20
        player.border_collision()

def update_attacks(player, enemies):
    # Update the position of each attack
    for attack in player.attacks:
        attack.y_pos -= attack_speed
        if attack.y_pos < 0:
            player.attacks.remove(attack)
    
    for enemy in enemies:
        for attack in enemy.attacks:
            attack.y_pos += attack_speed
            if attack.y_pos > 900:
                enemy.attacks.remove(attack)
                
def check_collisions(player, enemies):
    for enemy in enemies:
        for attack in enemy.attacks:
            if player.x_pos < attack.x_pos < player.x_pos + 60 and player.y_pos < attack.y_pos < player.y_pos + 60:
                player.health -= enemy.damage  # Decrease player's health
                enemy.attacks.remove(attack)  # Remove the attack

        for attack in player.attacks:
            if enemy.x_pos < attack.x_pos < enemy.x_pos + 60 and enemy.y_pos < attack.y_pos < enemy.y_pos + 60:
                enemy.health -= player.damage  # Decrease enemy's health
                player.attacks.remove(attack)  # Remove the attack
                if enemy.health <= 0:
                    enemies.remove(enemy)  # Remove the enemy if its health is 0
                    player.score += 1

def draw_background():
    screen.fill((0,0,0))
    # Draw grid
    for x in range(80):
        for y in range(80):
            rect = pygame.Rect(x*grid_size, y*grid_size, grid_size, grid_size)
            pygame.draw.rect(screen, (5,5,5), rect, 1)

    pygame.draw.line(screen, (255, 255, 255), (0, 625), (1600, 625), 2)

def draw_score(score):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (255,255,255))
    screen.blit(text, (10, 10))


def draw_player(player):
    # Draw health bar
    pygame.draw.rect(screen, (255,0,0), (player.x_pos, player.y_pos-10, 60, 5))
    pygame.draw.rect(screen, (0,255,0), (player.x_pos, player.y_pos-10, 60 * (player.health / 100), 5))  # Green health bar
    
    # Draw player
    pygame.draw.rect(screen, (255,255,255), (player.x_pos, user_y, 60, 60))
    
    # Draw attacks
    for attack in player.attacks:
        pygame.draw.rect(screen, (0,255,0), (attack.x_pos, attack.y_pos, 20, 20))
        
def draw_enemy(enemies):
    # Draw enemies
    for enemy in enemies:
        # Draw health bar
        pygame.draw.rect(screen, (255,0,0), (enemy.x_pos, enemy.y_pos-10, 60, 5))
        pygame.draw.rect(screen, (0,255,0), (enemy.x_pos, enemy.y_pos-10, 60 * (enemy.health / 100), 5))  # Green health bar
        
        pygame.draw.rect(screen, (255,0,0), (enemy.x_pos, enemy.y_pos, 60, 60))
        enemy.move()
        enemy.border_collision()

    # Draw enemy attacks
    for enemy in enemies:
        for attack in enemy.attacks:
            pygame.draw.rect(screen, (0,0,255), (attack.x_pos, attack.y_pos, 20, 20))
    

if __name__ == "__main__":
    main()
