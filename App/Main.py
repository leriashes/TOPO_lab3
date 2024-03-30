from pickle import FALSE
import pygame as pg
from datetime import datetime as dt
from App.Const import *
from App.Const import RIGHT_COLOR
from App.Grid import Grid

grid = Grid()
mouseReady = True
steps = 0
time = 0
timestamp = 0
win = False

button1_move = False
button2_move = False

def drawGrid(window):
    for i in range(4):
        for j in range(4):
            color = WRONG_COLOR
            font = pg.font.Font('Fonts/UbuntuMono-Regular.ttf', 52)

            value = grid.getCellValue(i, j)

            if value == 0:
                color = BG_COLOR
            elif value == i * 4 + j + 1:
                color = RIGHT_COLOR
            
            x = CELL_SIZE * j + SPACE_SIZE * (j + 1)
            y = CELL_SIZE * i + SPACE_SIZE * (i + 1)
            
            pg.draw.rect(window, color, (x, y, CELL_SIZE, CELL_SIZE))

            if value > 0:
                number = font.render(str(value), True, TEXT_COLOR)
            
                if 1 <= value <= 9:
                    window.blit(number, (x + 36, y + 22))
                else:
                    window.blit(number, (x + 23, y + 22))

def drawWinMenu(window):
    pg.draw.rect(window, MENU_BG_COLOR, (CELL_SIZE // 2, CELL_SIZE, MENU_WIDTH, MENU_HEIGHT))
    font1 = pg.font.Font('Fonts/UbuntuMono-Regular.ttf', 52)
    font2 = pg.font.Font('Fonts/UbuntuMono-Regular.ttf', 48)
    
    window.blit(font1.render("Вы выиграли!", True, MENU_TEXT_COLOR), (CELL_SIZE // 2 + 25, CELL_SIZE + 20))
    
    if button1_move:
        color = RIGHT_COLOR
    else:
        color = BG_COLOR

    pg.draw.rect(window, color, (CELL_SIZE // 2 + SPACE_SIZE, CELL_SIZE + MENU_HEIGHT - SPACE_SIZE - BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT))
        
    if button2_move:
        color = WRONG_COLOR
    else:
        color = BG_COLOR

    pg.draw.rect(window, color, (CELL_SIZE // 2 + SPACE_SIZE * 2 + BUTTON_WIDTH, CELL_SIZE + MENU_HEIGHT - SPACE_SIZE - BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT))

    window.blit(font2.render("Заново", True, TEXT_COLOR), (CELL_SIZE // 2 + 15, CELL_SIZE + 120))
    window.blit(font2.render("Выход", True, TEXT_COLOR), (CELL_SIZE // 2 + 30 + SPACE_SIZE + BUTTON_WIDTH, CELL_SIZE + 120))

def update():
    mousePos = pg.mouse.get_pos()
    mouseClick = pg.mouse.get_pressed()[0]

    mx, my = mousePos[0], mousePos[1]
    global mouseReady
    global steps
    global win
    global time
    global button1_move
    global button2_move
    
    if not mouseClick:
        mouseReady = True

        if win:
            button1_move = False
            button2_move = False

            x = CELL_SIZE // 2 + SPACE_SIZE
            y = CELL_SIZE + MENU_HEIGHT - SPACE_SIZE - BUTTON_HEIGHT

            if (x <= mx <= x + BUTTON_WIDTH) and (y <= my <= y + BUTTON_HEIGHT):
                button1_move = True

            x += BUTTON_WIDTH + SPACE_SIZE

            if (x <= mx <= x + BUTTON_WIDTH) and (y <= my <= y + BUTTON_HEIGHT):
                button2_move = True

    if mouseClick and mouseReady:
        if not win:
            for i in range(4):
                for j in range(4):
                    x = CELL_SIZE * j + SPACE_SIZE * (j + 1)
                    y = CELL_SIZE * i + SPACE_SIZE * (i + 1)
                
                    if (x <= mx <= x + CELL_SIZE) and (y <= my <= y + CELL_SIZE):
                        result = grid.moveCell(i, j)
                        if result:
                            steps += 1
                            win = grid.checkWin()
                        mouseReady = False
        else:
            x = CELL_SIZE // 2 + SPACE_SIZE
            y = CELL_SIZE + MENU_HEIGHT - SPACE_SIZE - BUTTON_HEIGHT

            if (x <= mx <= x + BUTTON_WIDTH) and (y <= my <= y + BUTTON_HEIGHT):
                win = False
                time = 0
                steps = 0
                grid.shuffleCells()

            x += BUTTON_WIDTH + SPACE_SIZE

            if (x <= mx <= x + BUTTON_WIDTH) and (y <= my <= y + BUTTON_HEIGHT):
               exit()


def main():
    global time
    global win
    global button1_move
    global button2_move

    grid.shuffleCells()

    pg.init()
    pg.display.set_caption("Пятнашки")
    img = pg.image.load('15.png')
    pg.display.set_icon(img)

    window = pg.display.set_mode((WIDTH, HEIGHT))

    timestamp = dt.now()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

        window.fill(BG_COLOR)

        tstmp = dt.now()

        if (tstmp - timestamp).total_seconds() >= 1:
            time += 1
            timestamp = tstmp
            
        drawGrid(window)

        if not win:
            pg.display.set_caption("Пятнашки | Ходы: " + str(steps) + "    Время: " + str(time // 60).rjust(2, '0') + ":" + str(time % 60).rjust(2, '0'))
        else:
            drawWinMenu(window)

        update()
        pg.display.update()

        keys = pg.key.get_pressed()
        
        if keys[pg.K_ESCAPE]:
            break
 
if __name__ == "__main__":
    main()
