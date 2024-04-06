import pygame as pg

bird_image = [pg.image.load(f'birds/bird{i}.png') for i in range(1, 4)]
print(bird_image)
pg.mixer.init()
sound = pg.mixer.Sound('birds/sfx_wing (1).mp3')

class Bird(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.jump_time = None
        self.image = pg.image.load('birds/bird1.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.vector = 2

    def jump(self):
        self.image = pg.image.load('birds/bird4.png.')
        self.vector = -5
        self.jump_time = pg.time.get_ticks()
        sound.play()

    def update(self):

        self.rect.y += self.vector
        if self.rect.y >= 570:
            self.rect.y = 570

        if self.rect.bottom > 600:
            self.rect.bottom = 600

        if self.rect.top < 0:
            self.rect.top = 0

        if self.jump_time is not None:
            elapsed_time = pg.time.get_ticks() - self.jump_time
            if elapsed_time >= 300:
                self.vector = 2
                current_time = pg.time.get_ticks()
                frame_duraction = 200
                frame_index = (current_time // frame_duraction) % len(bird_image)
                self.image = bird_image[frame_index]
