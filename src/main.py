# Modules
import pygame
import math
from queue import PriorityQueue

# Defining Windows
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE= (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.call = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows

        def get_pos(self):
            return self.row, self.col
        
        def is_closed(self):
            return self.color == RED

        def is_open(self):
            return self.color == GREEN
        
        def is_barrier(self):
            return self.color == BLACK
        
        def is_start(self):
            return self.color == ORANGE
        
        def is_end(self):
            return self.color == TURQUOISE
        
        def reset(self):
            self.color == WHITE


        def make_closed(self):
            self.color == RED
        
        def make_open(self):
            self.color == GREEN
        
        def make_barrier(self):
            self.color == BLACK
        
        def make_start(self):
            self.color == ORANGE

        def make_end(self):
            self.color = TURQUOISE
        
        def make_path(self):
            self.color = PURPLE

        def draw(self, win):
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
        
        def update_neighbours(self, grid):
            pass

        def __lt__(self, other): # lt: less than 
            return False # two spot objects compared
        

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2 + abs(y1 - y2))


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap)) # Multiply current index in row by the gap.
    
    for j in range(rows):
        pygame.draw.line(win, GREY, (0, j * gap, 0), (j * gap, width)) # Multiply current index in row by the gap.


def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(win)
    
    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y,x = pos

    row = y // gap
    col = x // gap

    return row, col


def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    started = False
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if started:
                continue

            if pygame.mouse.get_pressed()[0]: # LEFT-CLICK
                    pos = pygame.mouse.get_pos()
                    row, col = get_clicked_pos(pos, ROWS, width)
                    node = grid[row][col]

                    if not start:
                        start = node
                        start.make_start()

                    elif not end:
                        end = node
                        end.make_end()
                    
                    elif node != end and node != start:
                        node.make_barrier()

            elif pygame.mouse.get_pressed()[2]: # RIGHT-CLICK
                pass
    
    pygame.quit()

main(WIN, WIDTH)
