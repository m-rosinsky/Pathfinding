import pygame
import time
import collections
from color_sheet import *
 
grid_square_width = 40
grid_square_height = 40

grid_columns = 21
grid_rows = 21
 
grid_margin = 4
grid_margin_color = blue

grid_array = []
for row in range(grid_columns):

    grid_array.append([])
    for column in range(grid_rows):
        grid_array[row].append(0)
 
current_x = 1
current_y = 1
grid_array[current_x][current_y] = 2

end_x = 19
end_y = 19
grid_array[end_x][end_y] = 3
 
pygame.init()
 
window_height = (grid_square_width * grid_columns) + (grid_margin * grid_columns) + grid_margin
window_width = (grid_square_height * grid_rows) + (grid_margin * grid_rows) + grid_margin
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

def BFS(grid, start):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[x][y] == 3:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < grid_columns and 0 <= y2 < grid_rows and grid[x2][y2] != 1 and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

def drawGrid():
    for row in range(grid_columns):
        for column in range(grid_rows):
            color = white
            if grid_array[row][column] == 1:
                color = wall_color
            elif grid_array[row][column] == 2:
                color = start_color
            elif grid_array[row][column] == 3:
                color = finish_color
            elif grid_array[row][column] == 4:
                color = path_color
            pygame.draw.rect(screen,
                             color,
                             [(grid_margin + grid_square_width) * column + grid_margin,
                              (grid_margin + grid_square_height) * row + grid_margin,
                              grid_square_width,
                              grid_square_height])

def erasePath():
    for row in range(grid_columns):
        for column in range(grid_rows):
            if grid_array[row][column] != 1:
                grid_array[row][column] = 0

    grid_array[current_x][current_y] = 2
    grid_array[end_x][end_y] = 3
    drawGrid()

def resetGrid():
    for row in range(grid_columns):
        for column in range(grid_rows):
            grid_array[row][column] = 0
    grid_array[current_x][current_y] = 2
    grid_array[end_x][end_y] = 3
    drawGrid()

def createPath():
    l = BFS(grid_array, (current_x,current_y))
    if l == None:
        print("No Solution Possible")
    else:
        for square in l:
            if grid_array[square[0]][square[1]] != 2 and grid_array[square[0]][square[1]] != 3:
                grid_array[square[0]][square[1]] = 4

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                createPath()
                drawGrid()
            if event.key == pygame.K_SPACE:
                resetGrid()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            erasePath()

    if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2]:
        pos = pygame.mouse.get_pos()

        column = pos[0] // (grid_square_width + grid_margin)
        row = pos[1] // (grid_square_height + grid_margin)

        if column >= grid_columns:
            column = grid_columns-1
        if row >= grid_rows:
            row = grid_rows-1

        if pygame.mouse.get_pressed()[0]:
            color = wall_color
            grid_array[row][column] = 1
        else:
            color = white
            grid_array[row][column] = 0

        pygame.draw.rect(screen,
                             color,
                             [(grid_margin + grid_square_width) * column + grid_margin,
                              (grid_margin + grid_square_height) * row + grid_margin,
                              grid_square_width,
                              grid_square_height])


    # Draw the grid
    if grid_drawn == 0:
        screen.fill(fill_color)
        drawGrid()
        grid_drawn = 1

 
    clock.tick(120)
 
    pygame.display.flip()
 

pygame.quit()