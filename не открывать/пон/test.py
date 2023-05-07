import pygame, controls
from gun import Gun
from pygame.sprite import Group
from ino import Ino
FPS = 120


def run():
    pygame.init
    screen = pygame.display.set_mode((800, 700))
    pygame.display.set_caption("jgvrjg")
    bg_color = (255, 0, 60)
    gun = Gun(screen)
    bullets = Group()
    ino = Ino(screen)

    while True:

        controls.event(screen, gun, bullets)
        gun.update_gun()
        controls.update(bg_color, screen, gun, ino, bullets)
        controls.update_bullets(bullets)









run()