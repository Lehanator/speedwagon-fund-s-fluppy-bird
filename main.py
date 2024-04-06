import random
import pygame as pg
from bird import Bird
from pipe import Pipe
import random

pg.init()
score = 0
pg.font.init()
font = pg.font.SysFont('None', 100)
W = 600
H = 600

color = "black"
screen = pg.display.set_mode((W, H))
bird = Bird(50, H // 2)
all_sprite = pg.sprite.Group(bird)
clock = pg.time.Clock()
pipes = pg.sprite.Group()
pg.time.set_timer(pg.USEREVENT, 2000)
run = True

back_graund_img = pg.image.load('flappy_bird.png')
back_graund = pg.surface.Surface((back_graund_img.get_width(),600))
back_graund_x = 0
back_graund_x2 = back_graund_img.get_width()

while run:
    clock.tick(65)
    screen.fill(color)

    back_graund.blit(back_graund_img, (0,0))
    screen.blit(back_graund, (back_graund_x, 0 ))
    screen.blit(back_graund, (back_graund_x2, 0))

    back_graund_x -= 1
    back_graund_x2 -=1

    if back_graund_x < -back_graund_img.get_width():
        back_graund_x = back_graund_img.get_width()

    if back_graund_x2 < -back_graund_img.get_width():
        back_graund_x2 = back_graund_img.get_width()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYUP and event.key == pg.K_SPACE:
            bird.jump()
        if event.type == pg.USEREVENT:
            rand_hight = 150 + random.randint(0, 50)
            pipe_up = Pipe(W, 0, 50, rand_hight, (129, 208, 58))
            pipe_down = Pipe(W, rand_hight + random.randint(100, 200), 50, 1000, (129, 208, 58))
            all_sprite.add(pipe_up, pipe_down)
            pipes.add(pipe_up, pipe_down)
            score += 1

    if pg.sprite.spritecollide(bird, pipes, False):
        run = False

    all_sprite.draw(screen)
    all_sprite.update()
    text = font.render(f'{score}', False, 'white')
    screen.blit(text, (W//2 - 25, 500))
    pg.display.update()

pg.quit()
