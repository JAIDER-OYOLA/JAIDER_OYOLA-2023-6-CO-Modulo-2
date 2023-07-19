from game.utils.constants import ENEMY_1,ENEMY_2
from game.components.enemies.enemy import Enemy

class EnemyManager:
    def __init__(self):
        self.enemies = []
    
    def update(self, game):
        self.add_enemy()
        
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def add_enemy(self):
        if len(self.enemies) < 2:
            enemy1 = Enemy("dv1",ENEMY_1)
            enemy2 = Enemy("dv2",ENEMY_2, speed_x=15)
            self.enemies.append(enemy1)
            self.enemies.append(enemy2)