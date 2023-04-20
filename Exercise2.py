import sys
import pygame as pg


class Rectangle:
    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = x  # Position X
        self.y = y  # Position Y
        self.w = w  # Width
        self.h = h  # Height

    def draw(self, screen):
        pg.draw.rect(screen, (204, 0, 0), (self.x, self.y, self.w, self.h))


class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)

    def isMouseOn(self):
        if btn.x <= pg.mouse.get_pos()[0] <= (btn.x + btn.w) and btn.y <= pg.mouse.get_pos()[1] <= (btn.y + btn.h):
            return True
        else:
            pass


pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(330, 170, 100, 100)  # สร้าง Object จากคลาส Button ขึ้นมา

while (run):
    screen.fill((255, 255, 255))

    btn.draw(screen)
    if btn.isMouseOn():
        if pg.mouse.get_pressed()[0]:
            pg.draw.rect(screen, (76, 0, 153), (btn.x,
                                                btn.y, btn.w, btn.h))
        else:
            pg.draw.rect(screen, (96, 96, 96), (btn.x,
                                                btn.y, btn.w, btn.h))
    else:
        pg.draw.rect(screen, (204, 0, 0), (btn.x,
                     btn.y, btn.w, btn.h))

    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

        if event.type == pg.KEYDOWN and event.key == pg.K_d:  # ปุ่มถูกกดลงและเป็นปุ่ม D
            btn.x += 10
        if event.type == pg.KEYDOWN and event.key == pg.K_a:  # ปุ่มถูกปล่อยและเป็นปุ่ม A
            btn.x -= 10
        if event.type == pg.KEYDOWN and event.key == pg.K_w:  # ปุ่มถูกกดลงและเป็นปุ่ม D
            btn.y -= 10
        if event.type == pg.KEYDOWN and event.key == pg.K_s:  # ปุ่มถูกปล่อยและเป็นปุ่ม A
            btn.y += 10
