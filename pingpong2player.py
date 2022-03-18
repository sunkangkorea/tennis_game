import pygame as pg
import time
import random

width = 800
height = 600

#control
running = True
game_continue = True
endding = True

#color
black_color = (0 ,0, 0)
white_color = (255, 255, 255)
gray_color = (40, 40, 40)

#player
pmovement = 20
pcount = 1
py = 250

#player2
pmovement2 = 20
pcount2 = 1
py2 = 250

#ball
b_size = 15
bmovement = 5
bx = width/2
by = height/2
mxball = 20
myball = -10

#board
board_size = 150

#score
p_sy = height / 6
pscore = 0
psx = 125
pscore2 = 0
psx2 = width - 275

#pygame
pg.init()
pg.display.set_caption("...")
screen = pg.display.set_mode(( width, height ))

#font
font = pg.font.SysFont("arial",44)
bigfont = pg.font.SysFont("arial",300)

#sound
ball_sound1 = pg.mixer.Sound("gamesound/ping_pong_8bit_plop.ogg")
ball_sound2 = pg.mixer.Sound("gamesound/ping_pong_8bit_plop.ogg")
ball_sound3 = pg.mixer.Sound("gamesound/ping_pong_8bit_plop.ogg")

def ball_sound():
    ball_sound1.play()
    ball_sound2.play()
    ball_sound3.play()

def backstage():
    screen.fill(black_color)
    pg.draw.line(screen, white_color, (width/2, 0), (width/2, height), 5)

def draw_ball():
    global bx, by
    bx -= mxball
    by -= myball
    pg.draw.circle(screen, white_color,(bx, by), b_size)

def control_ball():
    global bmovement, mxball, myball, bx, by, pscore, pscore2
    if by < b_size:
        myball *= -1
        bmovement *= -1
        by = 15
    elif by > height - b_size:
        myball *= -1
        bmovement *= -1
        by = height - 15
    if bx < 25:
        if by < py + board_size + b_size and by > py - b_size:
            ball_sound()
            mxball *= -1
            myball += bmovement
            if by > py + board_size/5 and by < py + board_size - board_size/5:
                myball -= bmovement*2
        else:
            bx = width/2
            by = height/2
            b_direction()
            pscore2 += 1
    elif bx > width - 25:
        if by < py2 + board_size + b_size and by > py2 - b_size:
            ball_sound()
            mxball *= -1
            myball += bmovement
            if by > py2 + board_size/5 and by < py2 + board_size - board_size/5:
                myball -= bmovement*2
        else:
            bx = width/2
            by = height/2
            b_direction()
            pscore += 1

def b_direction():
    global mxball, myball
    r_num = random.randint(1, 4)
    if r_num == 1:
        mxball = -20
        myball = -10
    if r_num == 2:
        mxball = 20
        myball = -10
    if r_num == 3:
        mxball = -20
        myball = 10
    if r_num == 4:
        mxball = 20
        myball = 10

def player():
    global py, pmovement
    py -= pmovement
    if py + board_size > height or py < 0:
        py += pmovement
    pg.draw.rect(screen, white_color, (0, py, 10, board_size))

def player2():
    global py2, pmovement2
    py2 -= pmovement2
    if py2 + board_size > height or py2 < 0:
        py2 += pmovement2
    pg.draw.rect(screen, white_color, (width - 10, py2, 10, board_size))

#score
def score_set():
    pscoreset = bigfont.render("{}".format(pscore), True, gray_color)
    screen.blit(pscoreset, (psx, p_sy))
    pscoreset2 = bigfont.render("{}".format(pscore2), True, gray_color)
    screen.blit(pscoreset2, (psx2, p_sy))

def replay():
    global endding, game_continue
    ask_g = font.render("Another game? Yes: Y, No: n", True, white_color)
    screen.blit(ask_g, (width/8, height/2 - 40))
    pg.display.update()
    while endding:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_y:
                    endding = False
                if event.key == pg.K_n:
                    endding = False
                    game_continue = False

while game_continue:
    sx = 125
    running = True
    endding = True
    pscore = 0
    pscore2 = 0
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                game_continue = False
            if event.type == pg.KEYDOWN:
                if event.key == 13 or event.key == pg.K_KP_ENTER:
                    pmovement2 *= -1
                    pcount2 *= -1
                if event.key == 32:
                    pmovement *= -1
                    pcount *= -1
        backstage()
        score_set()
        draw_ball()
        control_ball()
        player()
        player2()
        pg.display.update()
        time.sleep(0.03)
        if pscore == 10 or pscore2 ==10:
            break
    replay()
pg.quit()