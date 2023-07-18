import pygame

class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
    ##actualizar las balas
    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == "enemy":
                self.enemy_bullets.remove(bullet)
                game.playing = False
                pygame.time.delay(1000)
                break

        for bullet in self.bullets:
            bullet.update(self.bullets)
            
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy) and bullet.owner == 'player':
                    game.enemy_manager.enemies.remove(enemy)
                
                
    ##dibujar las balas
    def draw(self, screen):

        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        
        for bullet in self.bullets:
            bullet.draw(screen)



    ##Agregar las balas
    def add_bullet(self, bullet):
        if bullet.owner == "enemy" and len(self.enemy_bullets) < 4:
            self.enemy_bullets.append(bullet)

        if bullet.owner == "player" :
            self.bullets.append(bullet)
