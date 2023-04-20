from datetime import datetime
import sys
import pygame as pg


class Rectangle:
    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = x  # Position X
        self.y = y  # Position Y
        self.w = w  # Width
        self.h = h  # Height

    def draw(self, screen):
        pg.draw.rect(screen, COLOR_INACTIVE,
                     (self.x, self.y, self.w, self.h), 2)


class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)

    def isMouseOn(self):
        if self.x <= pg.mouse.get_pos()[0] <= (self.x + self.w) and self.y <= pg.mouse.get_pos()[1] <= (self.y + self.h):
            return True
        else:
            pass


class TextBox:
    def __init__(self, col, text=''):
        self.color = col
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y))


class InputBox:

    def __init__(self, x, y, w, h, text='', type=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.type = type

    def handle_event(self, event):

        if event.type == pg.MOUSEBUTTONDOWN:  # ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            # ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE  # เปลี่ยนสีของ InputBox
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if self.type == 'str':
                        self.text += event.unicode
                    elif self.type == 'int':
                        if event.unicode.isnumeric():
                            self.text += event.unicode
                        else:
                            self.text = self.text
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(self.rect.w, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)


class PasswordBox:

    def __init__(self, x, y, w, h, hiddentext='', text='', type=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.hiddentext = hiddentext
        self.text = text
        self.txt_surface = FONT.render(hiddentext, True, self.color)
        self.active = False
        self.type = type

    def handle_event(self, event):

        if event.type == pg.MOUSEBUTTONDOWN:  # ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            # ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE  # เปลี่ยนสีของ InputBox
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                    self.hiddentext = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                    self.hiddentext = self.hiddentext[:-1]
                else:
                    self.hiddentext += "*"
                    self.text += event.unicode

                # Re-render the text.
                self.txt_surface = FONT.render(
                    self.hiddentext, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(self.rect.w, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)


def calc_age(time, year, month, day):
    curr_year = str(time)[:4]
    curr_month = str(time)[5:7]
    curr_date = str(time)[8:10]

    y = int(curr_year)-int(year)
    m = int(curr_month)-int(month)
    d = int(curr_date)-int(day)

    if d < 0:
        m -= 1
        d += 30
    if m < 0:
        y -= 1
        m += 12
    if y == 0:
        if m == 0:
            if d == 1:
                final = "{dd} day".format(dd=d)
            elif d == 0:
                final = "you have just borned"
            else:
                final = "{dd} days".format(dd=d)
        elif m == 1:
            if d == 1:
                final = "{mm} month and {dd} day".format(mm=m, dd=d)
            elif d == 0:
                final = "{mm} month".format(mm=m)
            else:
                final = "{mm} month and {dd} days".format(mm=m, dd=d)
        else:
            if d == 1:
                final = "{mm} months and {dd} day".format(mm=m, dd=d)
            elif d == 0:
                final = "{mm} months".format(mm=m)
            else:
                final = "{mm} months and {dd} days".format(mm=m, dd=d)
    elif y == 1:
        if m == 0:
            if d == 1:
                final = "{yy} year and {dd} day".format(yy=y, dd=d)
            elif d == 0:
                final = "{yy} year".format(yy=y)
            else:
                final = "{yy} year and {dd} days".format(yy=y, dd=d)
        elif m == 1:
            if d == 1:
                final = "{yy} year, {mm} month and {dd} day".format(
                    yy=y, mm=m, dd=d)
            elif d == 0:
                final = "{yy} year and {mm} month".format(yy=y, mm=m)
            else:
                final = "{yy} year, {mm} month and {dd} days".format(
                    yy=y, mm=m, dd=d)
        else:
            if d == 1:
                final = "{yy} year, {mm} months and {dd} day".format(
                    yy=y, mm=m, dd=d)
            elif d == 0:
                final = "{yy} year and {mm} months".format(yy=y, mm=m)
            else:
                final = "{yy} year, {mm} months and {dd} days".format(
                    yy=y, mm=m, dd=d)
    else:
        if m == 0:
            if d == 1:
                final = "{yy} years and {dd} day".format(yy=y, dd=d)
            elif d == 0:
                final = "{yy} years".format(yy=y)
            else:
                final = "{yy} years and {dd} days".format(yy=y, dd=d)
        elif m == 1:
            if d == 1:
                final = "{yy} years, {mm} month and {dd} day".format(
                    yy=y, mm=m, dd=d)
            elif d == 0:
                final = "{yy} years and {mm} month".format(yy=y, mm=m)
            else:
                final = "{yy} years, {mm} month and {dd} days".format(
                    yy=y, mm=m, dd=d)
        else:
            if d == 1:
                final = "{yy} years, {mm} months and {dd} day".format(
                    yy=y, mm=m, dd=d)
            elif d == 0:
                final = "{yy} years and {mm} months".format(yy=y, mm=m)
            else:
                final = "{yy} years, {mm} months and {dd} days".format(
                    yy=y, mm=m, dd=d)
    return final


pg.init()
win_x, win_y = 1200, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(200, 400, 200, 32)
Black = (0, 0, 0)
Red = (255, 51, 51)
information_switch = 0

# ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font('C:\WINDOWS\FONTS\BRUSHSCI.TTF', 28)

input_box1 = InputBox(75, 125, 200, 32, '', 'str')
input_box2 = InputBox(325, 125, 200, 32, '', 'str')
input_box3 = InputBox(75, 200, 50, 32, '', 'int')
input_box4 = InputBox(150, 200, 50, 32, '', 'int')
input_box5 = InputBox(225, 200, 50, 32, '', 'int')
input_box6 = InputBox(325, 200, 200, 32, '', 'str')
input_box7 = PasswordBox(75, 275, 200, 32, '', '', 'str')
input_box8 = PasswordBox(325, 275, 200, 32, '', '', 'str')
input_box_FN = InputBox(75, 125, 200, 32, 'Firstname : ')
input_box_NN = InputBox(325, 125, 200, 32, 'Familyname : ')
input_box_DB = InputBox(75, 200, 100, 32, 'Birth date (AD.)')
input_box_ED = InputBox(325, 200, 300, 32, 'Email Address : ')
input_box_PW = InputBox(75, 275, 200, 32, 'Password : ')
input_box_CPW = InputBox(325, 275, 200, 32, 'Confirm Password : ')
# เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
input_boxes = [input_box1, input_box2, input_box3,
               input_box4, input_box5, input_box6,
               input_box7, input_box8]
texts = [input_box_FN, input_box_NN, input_box_DB,
         input_box_ED, input_box_PW, input_box_CPW]
run = True

while run:
    screen.fill((255, 229, 204))
    btn.draw(screen)
    if information_switch == 1:
        name = "Hello!, {fn} {sn}".format(
            fn=input_box1.text, sn=input_box2.text)
        age = "You are {calced_age} old.".format(calced_age=calc_age(
            datetime.now(), input_box5.text, input_box4.text, input_box3.text))
        mail = "Email address: {mail_a}".format(mail_a=input_box6.text)
        password = "Password : {pass_confirmed}".format(
            pass_confirmed=input_box7.text)
        screen.blit(TextBox(100, 300, 200, 32, Black,
                    name).txt_surface, (750, 125))
        screen.blit(TextBox(100, 300, 200, 32, Black,
                    age).txt_surface, (750, 200))
        screen.blit(TextBox(100, 300, 200, 32, Black,
                    mail).txt_surface, (750, 275))
        screen.blit(TextBox(100, 300, 200, 32, Black,
                    password).txt_surface, (750, 350))
        pg.draw.rect(screen, COLOR_INACTIVE, (599, 0, 2, 480))
    if btn.isMouseOn():
        if pg.mouse.get_pressed()[0]:
            pg.draw.rect(screen, COLOR_ACTIVE, (btn.x,
                                                btn.y, btn.w, btn.h), 5)
            if input_box7.text != input_box8.text:
                screen.blit(TextBox(
                    100, 300, 200, 32, Red, "Password doesn't match ").txt_surface, (190, 350))
            else:
                information_switch = 1
                print('Hello,', input_box1.text, input_box2.text,
                      '! You are', calc_age(datetime.now(), input_box5.text, input_box4.text, input_box3.text), 'old.', "Email adress :", input_box6.text, "Password :", input_box7.text)
        else:
            pg.draw.rect(screen, COLOR_INACTIVE, (btn.x,
                                                  btn.y, btn.w, btn.h), 5)
    else:
        pg.draw.rect(screen, (COLOR_INACTIVE), (btn.x,
                     btn.y, btn.w, btn.h), 2)

    # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
    for box in input_boxes:
        box.update()  # เรียกใช้ฟังก์ชัน update() ของ InputBox
        # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        box.draw(screen)
    for txt in texts:
        screen.blit(txt.txt_surface, (txt.rect.x, txt.rect.y-30))
    screen.blit(TextBox(Black,
                'SUBMIT').txt_surface, (245, 400))
    screen.blit(TextBox(Black,
                'REGISTER').txt_surface, (240, 50))
    screen.blit(TextBox(Black,
                'Your Information').txt_surface, (820, 50))

    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()


'''if self.type == 'str':
                        self.hiddentext += "*"
                        self.text += event.unicode
                    elif self.type == 'int':
                        if event.unicode.isnumeric():
                            self.hiddentext += "*"
                            self.text += event.unicode
                        else:
                            self.hiddentext = self.hiddentext
                            self.text = self.text'''
