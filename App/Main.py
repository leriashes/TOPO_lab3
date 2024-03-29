import pygame as pg
from App.Grid import Grid

WIDTH, HEIGHT = 640, 640
BG_COLOR = (229, 223, 189)

def main():
    grid = Grid()

    grid.shuffleCells()

    pg.init()
    pg.display.set_caption("Пятнашки")

    window = pg.display.set_mode((WIDTH, HEIGHT))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

        window.fill(BG_COLOR)

        pg.display.update()
 
if __name__ == "__main__":
    main()
