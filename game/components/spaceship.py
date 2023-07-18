import pygame, random
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH
from game.components.bullets.bullet import Bullet

class Spaceship(Sprite):
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500

    def __init__(self, name):
        super().__init__()
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.move_rect = 10
        self.name = name  # Nuevo atributo para almacenar el nombre del jugador
        self.type = 'player'
        self.shooting_time = 0
        self.score = 0

    def update(self, user_input, game, enemies):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        if user_input[pygame.K_RIGHT]:
            self.move_right()
        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_DOWN]:
            self.move_down()
        if user_input[pygame.K_SPACE]:
            self.shooting_sp(game)

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= self.move_rect

    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.move_rect

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= self.move_rect

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y += self.move_rect
    
    def shooting_sp(self, game):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            game.bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(15, 30)


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

        font = pygame.font.Font(None, 24)
        name_text = font.render(self.name, True, (255, 255, 255))
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))

        name_rect = name_text.get_rect()
        score_rect = score_text.get_rect()

        name_rect.topright = (self.rect.right + 50, self.rect.top)
        score_rect.topright = (self.rect.right + 65, self.rect.top + 25)  # Ajusta la posición del score debajo del nombre
    
        screen.blit(name_text, name_rect)
        screen.blit(score_text, score_rect)