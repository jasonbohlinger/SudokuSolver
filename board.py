import pygame as pg

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_sudoku_grid():
    #box = pg.Rect((50, 50), (700, 700))
    pg.draw.line(screen, BLACK, (50, 50), (50, 750), 3)
    pg.draw.line(screen, BLACK, (50, 50), (750, 50), 3)
    pg.draw.line(screen, BLACK, (50, 750), (750, 750), 3)
    pg.draw.line(screen, BLACK, (750, 50), (750, 750), 3)

    #pg.draw.rect(screen, BLACK, box, 3)
    for offset in range(3):
        pg.draw.line(screen, BLACK, (50 + ((700 * offset) / 3), 50), (50 + ((700 * offset) / 3), 750), 3)

        pg.draw.line(screen, BLACK, (50, 50 + (700 * offset) / 3), (750, (50 + (700 * offset) / 3)), 3)
    #pg.draw.line(screen, BLACK, ())

(screen_width, screen_height) = (800, 800)

screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Sudoku')
screen.fill(WHITE)

draw_sudoku_grid()
pg.display.flip()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


