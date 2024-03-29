import pygame as pg
from App.Const import *
from App.Const import RIGHT_COLOR
from App.Grid import Grid

grid = Grid()

def drawGrid(window):
    for i in range(4):
        for j in range(4):
            color = WRONG_COLOR

            if grid.getCellValue(i, j) == 0:
                color = BG_COLOR
            elif grid.getCellValue(i, j) == i * 4 + j + 1:
                color = RIGHT_COLOR
            
            x = CELL_SIZE * j + SPACE_SIZE * (j + 1)
            y = CELL_SIZE * i + SPACE_SIZE * (i + 1)
            
            pg.draw.rect(window, color, (x, y, CELL_SIZE, CELL_SIZE))

def main():

    grid.shuffleCells()

    pg.init()
    pg.display.set_caption("Пятнашки")

    window = pg.display.set_mode((WIDTH, HEIGHT))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

        window.fill(BG_COLOR)

        drawGrid(window)

        pg.display.update()
 
if __name__ == "__main__":
    main()
