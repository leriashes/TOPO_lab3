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

def update():
    mousePos = pg.mouse.get_pos()
    mouseClick = pg.mouse.get_pressed()[0]

    mx, my = mousePos[0], mousePos[1]
    global mouseReady
    global steps
    
    if not mouseClick:
        mouseReady = True

    if mouseClick and mouseReady:
        for i in range(4):
            for j in range(4):
                x = CELL_SIZE * j + SPACE_SIZE * (j + 1)
                y = CELL_SIZE * i + SPACE_SIZE * (i + 1)
                
                if (x <= mx <= x + CELL_SIZE) and (y <= my <= y + CELL_SIZE):
                    result = grid.moveCell(i, j)
                    if result:
                        steps += 1
                    mouseReady = False

def main():
    global time

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

        pg.display.set_caption("Пятнашки | Ходы: " + str(steps) + "    Время: " + str(time // 60).rjust(2, '0') + ":" + str(time % 60).rjust(2, '0'))
        drawGrid(window)

        update()

        pg.display.update()

        keys = pg.key.get_pressed()
        
        if keys[pg.K_ESCAPE]:
            break
 
if __name__ == "__main__":
    main()
