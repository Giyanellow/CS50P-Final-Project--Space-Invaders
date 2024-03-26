import pytest
from space_invaders import Player, Enemy, Attack

# test player.health
def test_player_health():
    player = Player(health=100, damage=10, score=0, x_pos=0, y_pos=0)
    assert player._health == 100
    assert player._health != 0
    
    # test for negative health
    player = Player(health=-100, damage=10, score=0, x_pos=0, y_pos=0)
    with pytest.raises(ValueError):
        player.health = -100

def test_enemy_health():
    enemy = Enemy(health=100, damage=10, x_pos=0, y_pos=0)
    assert enemy._health == 100
    assert enemy._health != 0
    
    # test for negative health 
    enemies = Enemy(health=-100, damage=10, x_pos=0, y_pos=0)
    with pytest.raises(ValueError):
        enemies.health = -100
    
def test_player_border_collision():
    player = Player(health=100, damage=10, score=0, x_pos=0, y_pos=0)
    player.x_pos = -100
    player.border_collision()
    assert player.x_pos == 0
    
    player.x_pos = 2000
    player.border_collision()
    assert player.x_pos == 1540
    
def test_enemy_border_collision():
    enemy = Enemy(health=100, damage=10, x_pos=0, y_pos=0)
    enemy.x_pos = -100
    enemy.border_collision()
    assert enemy.x_pos == 0
    
    enemy.x_pos = 2000
    enemy.border_collision()
    assert enemy.x_pos == 1540
    
def test_player_attack():
    player = Player(health=100, damage=25, score=0, x_pos=50, y_pos=50)
    player.attack()
    assert len(player.attacks) == 1
    assert isinstance(player.attacks[0], Attack)
    assert player.attacks[0].x_pos == 50
    assert player.attacks[0].y_pos == 800

def test_enemy_attack():
    enemy = Enemy(health=100, damage=10, x_pos=50, y_pos=50)
    enemy.attack()
    assert len(enemy.attacks) == 1
    assert isinstance(enemy.attacks[0], Attack)
    assert enemy.attacks[0].x_pos == 50
    assert enemy.attacks[0].y_pos == 50