import pygame
import time
import collections
from color_sheet import *

class Grid_Array:
    def __init__(self, rows=10, columns=10, box_size=50, margin_size=3, start_point=(1,1)):
        self.num_rows = rows if rows > 0 else 10
        self.num_columns = columns if columns > 0 else 10
        self.box_size = box_size if box_size > 5 else 10
        self.margin_size = margin_size if margin_size > 0 else 1
        self.start_point = start_point
        self.end_point = (self.num_rows-2,self.num_columns-2)

        self.grid_array = []

    def init_grid(self):
        self.grid_array = []
        for row in range(self.num_columns):
            self.grid_array.append([])
            for column in range(self.num_rows):
                self.grid_array[row].append(0)

        self.grid_array[self.start_point[0]][self.start_point[1]] = 2
        self.grid_array[self.end_point[0]][self.end_point[1]] = 3

    def draw_grid(self):
        for row in range(self.num_columns):
            for column in range(self.num_rows):
                color = white
                if self.grid_array[row][column] == 1:
                    color = wall_color
                elif self.grid_array[row][column] == 2:
                    color = start_color
                elif self.grid_array[row][column] == 3:
                    color = finish_color
                elif self.grid_array[row][column] == 4:
                    color = path_color
                pygame.draw.rect(screen,
                                 color,
                                 [(self.margin_size + self.box_size) * column + self.margin_size,
                                  (self.margin_size + self.box_size) * row + self.margin_size,
                                  self.box_size,
                                  self.box_size])

    def erase_path(self):
        for row in range(self.num_columns):
            for column in range(self.num_rows):
                if self.grid_array[row][column] != 1:
                    self.grid_array[row][column] = 0

        self.grid_array[self.start_point[0]][self.start_point[1]] = 2
        self.grid_array[self.end_point[0]][self.end_point[1]] = 3
        self.draw_grid()

    def BFS(self):
        queue = collections.deque([[self.start_point]])
        seen = set([self.start_point])
        while queue:
            path = queue.popleft()
            x, y = path[-1]
            if self.grid_array[x][y] == 3:
                return path
            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if 0 <= x2 < self.num_columns and 0 <= y2 < self.num_rows and self.grid_array[x2][y2] != 1 and (x2, y2) not in seen:
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))

    def create_path(self):
        l = self.BFS()
        if l == None:
            print("No Solution Possible")
        else:
            for x,y in l:
                if self.grid_array[x][y] != 2 and self.grid_array[x][y] != 3:
                    self.grid_array[x][y] = 4
                    if animate:
                        pygame.event.poll()
                        pygame.time.wait(animate_speed)

                    pygame.draw.rect(screen,
                                 path_color,
                                 [(self.margin_size + self.box_size) * y + self.margin_size,
                                  (self.margin_size + self.box_size) * x + self.margin_size,
                                  self.box_size,
                                  self.box_size])
                    pygame.display.update()
 

num_rows = 10
num_columns = 10
box_size = 50
margin_size = 2
start_point = (1,1)
grid = Grid_Array(num_rows, num_columns, box_size, margin_size, start_point)
grid.init_grid()

pygame.init()

animate = True ## Animate finding path
animate_speed = 50 ## Ticks in between frames. Lower value = higher speed
 
window_height = (grid.box_size * grid.num_rows) + (grid.margin_size * grid.num_rows) + grid.margin_size
window_width = (grid.box_size * grid.num_columns) + (grid.margin_size * grid.num_columns) + grid.margin_size
screen = pygame.display.set_mode((window_width,window_height))

grid_drawn = 0
 
pygame.display.set_caption("Pathfinding!")
 
running = True
 
clock = pygame.time.Clock()

wall_color = gray
start_color = green
finish_color = yellow
path_color = purple
fill_color = black

while running:

    ## Controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                grid.create_path()
                grid.draw_grid()
            if event.key == pygame.K_SPACE:
                grid.init_grid()
                grid.draw_grid()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            grid.erase_path()

    ## Mouse Dragging for creating and erasing walls
    if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2]:
        pos = pygame.mouse.get_pos()

        column = pos[0] // (grid.box_size + grid.margin_size)
        row = pos[1] // (grid.box_size + grid.margin_size)

        if column >= grid.num_columns:
            column = grid.num_columns-1
        if row >= grid.num_rows:
            row = grid.num_rows-1

        if pygame.mouse.get_pressed()[0]:
            color = wall_color
            grid.grid_array[row][column] = 1
        else:
            color = white
            grid.grid_array[row][column] = 0

        pygame.draw.rect(screen,
                            color,
                            [(grid.margin_size + grid.box_size) * column + grid.margin_size,
                            (grid.margin_size + grid.box_size) * row + grid.margin_size,
                            grid.box_size,
                            grid.box_size])


    # Draw the grid
    if grid_drawn == 0 or grid_drawn == 1:
        screen.fill(fill_color)
        grid.draw_grid()
        grid_drawn = 1

 
    clock.tick(80)

    pygame.display.flip()
  

pygame.quit()