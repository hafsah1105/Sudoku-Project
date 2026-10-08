import pygame
import sys
from pygame.locals import QUIT
import random
from random import randint
import time

#declaring screen & display size
pygame.init()
screen = pygame.display.set_mode((550, 600))
font = pygame.font.SysFont("Arial", 30)
fontsmaller = pygame.font.SysFont("Arial", 20)
font_exit = pygame.font.SysFont("Arial", 50)

def createGrid(size):
    global grid
    grid = [[0 for n in range(size)] for m in range(size)]
    global solution
    solution = [[0 for n in range(size)] for m in range(size)]
    global initial_problem
    initial_problem = [[0 for n in range(size)] for m in range(size)]

#this makes the background white and draws the grid
def draw_grid(size):
    screen.fill((255,255,255)) #make background white
    if size==9:
        cell_size=50
        subgrid_size=3
    elif size==4:
        cell_size=110
        subgrid_size=2
    grid_size=cell_size*size
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(10,10,grid_size,grid_size),5)
     #start coordinates, size of the grid, line width
    i=1
    while (i*cell_size)<grid_size:
        line_width=2 if i%subgrid_size>0 else 5
        pygame.draw.line(screen,pygame.Color("black"),pygame.Vector2((i*cell_size)+10,10),pygame.Vector2((i*cell_size)+10,grid_size+10),line_width)
        pygame.draw.line(screen,pygame.Color("black"),pygame.Vector2(10,(i*cell_size)+10),pygame.Vector2(grid_size+10,(i*cell_size)+10),line_width)
        i+=1
    #draw_numbuttons(size)

def create_button(text, topleft, size, colour, border):
    xtopleft, ytopleft = topleft
    width, height = size
    r, g, b = colour
    button_rect=pygame.Rect(xtopleft,ytopleft,width,height)
    pygame.draw.rect(screen,(r,g,b),button_rect)
    if border>0:
        pygame.draw.rect(screen, (0, 0, 0), button_rect,border)
    button_text= font.render(text, True, pygame.Color("black"))
    button_text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, button_text_rect)
    return button_rect

def draw_buttons(size):
#first button - solve, will solve sudoku on screen
    global solve_button_rect
    solve_button_rect=create_button("Solve", (10, 500), (100, 40), (176, 213, 230),0)
#next button - check, this button will check user's answers
    global check_button_rect
    check_button_rect=create_button("Check", (120, 500), (100, 40), (176, 213, 230),0)
#next button - delete, will delete selected cell value, only if the user entered this value, can't delete a set value
    global delete_button_rect
    delete_button_rect=create_button("Delete", (230, 500), (100, 40), (176, 213, 230),0)
#next button - enter problem to solve
    global enter_button_rect
    enter_button_rect=create_button("Solve Your Own", (10, 550), (225, 40), (176, 213, 230),0)
#next button - classic sudoku (re)generate
    global classic_button_rect
    classic_button_rect=create_button("Classic", (245, 550), (110, 40), (176, 213, 230),0)
#next button - 4x4 sudoku (re)generate
    global four_button_rect
    four_button_rect=create_button("4x4", (364, 550), (70, 40), (176, 213, 230),0)
#next button - exit, to exit the program
    global exit_button_rect
    exit_button_rect=create_button("EXIT", (410, 480), (120, 50), (200, 100, 100),0)
#draw buttons for each number onto right side of the grid
    button_size = 40
    button_start_x = 475
    button_start_y = 10
    for i in range(1, size+1):
      num_button_rect = create_button(str(i), (button_start_x, button_start_y + ((button_size) * (i - 1))), (button_size, button_size), (200, 200, 200),2)

#this draws all of the numbers onto the grid, making user's input blue rather than black
#so the user can easily differentiate
def draw_numbers(size):
    if size==9:
        cell_size=50
        x_gap=26
        y_gap=20
    elif size==4:
        cell_size=110
        x_gap=55
        y_gap=50
    row=0
    while row<size:
        col=0
        while col<size:
            output=grid[row][col]
            if initial_problem[row][col]!="":
                n_text=font.render(str(output),True,pygame.Color("black"))
            if initial_problem[row][col]=="":
                n_text=font.render(str(output),True,pygame.Color("blue"))
            screen.blit(n_text,pygame.Vector2((row*cell_size)+x_gap,(col*cell_size)+y_gap))
            col+=1
        row+=1

#this fills the cells in rows, rather than cell by cell
#for every row in the grid make a list of 1-9 and add to grid
def fill_cells(size):
    for i in range(0,size):
            row_values=[]
            for y in range (1, size+1):
                row_values.append(y)
            random.shuffle(row_values)
            if size==9:
                #until the rows are shuffled to form a grid where there are no repeats with new values generated and previous values
                while is_repeats(row_values,i,9,3)!=True:
                    random.shuffle(row_values)
            elif size==4:
                while is_repeats(row_values,i,4,2)!=True:
                    random.shuffle(row_values)
            for j in range(0,size):
                grid[i][j] = row_values[j]
                solution[i][j] = row_values[j]
                initial_problem[i][j] = row_values[j]
#as the rows are filled in one go there is no need for a check for each row
#this only checks each column and 3x3 grid

def is_repeats(row_values,row,size,boxsize):
    for i in range(0,size):
        for j in range(0,size):
            if row_values[j]==grid[i][j]:
                return False
#although only checking column need to include i to iterate through rows
#and j as row_values is a list with multiple values
    for j in range(0,size):
        num=row_values[j]
        startrow=(row//boxsize)*boxsize 
        startcol=(j//boxsize)*boxsize
#values from 0-2, *3 to get correct start value
        for i in range(startrow,startrow+boxsize):
            for j in range(startcol,startcol+boxsize):
                if num==grid[i][j]:
                    return False
    return True

#this needs to remove values from the grid to then display - does exactly 40
def hide_values():
    empty=20
    while empty!=0:
        i = randint(0,8)
        j = randint(0,8)
        if grid[i][j]!="":
            if len(possible_values(grid,i,j, 9, 3))==1:
                grid[i][j]=""
                initial_problem[i][j]=""
                empty-=1
    hide=True
    while hide==True:
        i = randint(0,8)
        j = randint(0,8)
        if grid[i][j]!="":
            grid_copy=grid
            if len(possible_values(grid_copy,i,j, 9, 3))<=3:
                grid[i][j]=""
                initial_problem[i][j]=""
        emptycount=0
        for i in range(0,9):
            for j in range(0,9):
                if initial_problem[i][j]=="":
                    emptycount+=1
        if emptycount>=40:
            hide=False


#this needs to remove values from the grid to then display
def fourxhide_values():
    empty=7
    while empty!=0:
       i = randint(0,3)
       j = randint(0,3)
       fourxgrid_copy=grid
       if len(possible_values(fourxgrid_copy,i,j,4,2))==1:
          grid[i][j]=""
          initial_problem[i][j]=""
          empty-=1

#by checking possible values & possible using recursion/backtracking we can get to a solution
#this checks the possible values for the cell chosen
def possible_values(g,i,j, size, boxsize):
    temp=g[i][j]
    g[i][j]=""
    pvalues=[]
    for y in range (1, size+1):
        pvalues.append(y)
    for x in range(0,size):
        #check numbers in column
        if g[x][j] in pvalues:
            pvalues.remove(g[x][j])
        #check numbers in row
        if g[i][x] in pvalues:
            pvalues.remove(g[i][x])
    startrow=(i//boxsize)*boxsize
    startcol=(j//boxsize)*boxsize
    for x in range(startrow,startrow+boxsize):
        for y in range(startcol,startcol+boxsize):
            if g[x][y] in pvalues:
                pvalues.remove(g[x][y])
    g[i][j]=temp
    return pvalues

#this value checks to see if user's input is valid
def check_input(row, col, num, size, boxsize):
    for x in range(0,size):
#check column & row
        if grid[x][col]==num:
            return False
        if grid[row][x]==num:
            return False
    startrow=(row//boxsize)*boxsize 
    startcol=(col//boxsize)*boxsize
#values from 0-2, *3 to get correct start value
    for i in range(startrow,startrow+boxsize):
        for j in range(startcol,startcol+boxsize):
            if num==grid[i][j]:
                 return False
    return True

#check user's input against solution, check button function
#displaying either the cell as red or green to indicate whether correct or incorrect
def check_correct(size):
    if size==9:
        cell_size=50
        x_gap=26
        y_gap=20
    elif size==4:
        cell_size=110
        x_gap=55
        y_gap=50
    for i in range(0,size):
        for j in range(0,size):
            if initial_problem[i][j]=="" and  grid[i][j]!="":
                print("checking")
                print(solution)
                print(initial_problem)
                if grid[i][j]==solution[i][j]:
                    pygame.draw.rect(screen, (0,200,0), pygame.Rect(i*cell_size+10,j*cell_size+10,cell_size,cell_size))
                    #not including rect width to fill entire rectangle
                    num = font.render(str(grid[i][j]), True, (0, 0, 0))
                    screen.blit(num, (i * cell_size + x_gap, j * cell_size + y_gap))
                    pygame.display.flip()
                    time.sleep(1)
                elif grid[i][j]!=solution[i][j]:
                    pygame.draw.rect(screen, (200,0,0), pygame.Rect(i*cell_size+10,j*cell_size+10,cell_size,cell_size))
                    #not including rect width
                    num = font.render(str(grid[i][j]), True, (0, 0, 0))
                    screen.blit(num, (i * cell_size + x_gap, j * cell_size + y_gap))
                    pygame.display.flip()
                    time.sleep(1)

#this solves sudoku using recursion/backtracking 
def solvesudoku(size):
    for i in range(0,size):
        for j in range(0,size):
            if grid[i][j]=="":
                if size==9:
                    pvalues=possible_values(grid,i,j, 9, 3)
                elif size==4:
                    pvalues=possible_values(grid,i,j,4,2)
                if len(pvalues)==1:
                    grid[i][j]=pvalues
                #one value so put into cell
                for value in pvalues:
                    grid[i][j]=value
                    #multiple values test every single one
                    #just in case ends up being last, can iterate through
                    if solvesudoku(size):
                        return True
                    grid[i][j]=""
                return False
    return True

#clearing grid for user to enter their own problem
def clear_grid(size):
    for i in range(0,size):
        for j in range(0,size):
            grid[i][j]=""
            initial_problem[i][j]=""
            solution[i][j]=""

#made separate gameloops for each as then the code for each function for both would be crammed into one
#and for example entering keys 5-9 may accidentally be accepted into a 4x4
#this is for the classic 9x9 grid
def game_loop_classic(size):
    global val
    val=0
    if size==9:
        cell_size=50
        grid_size=cell_size*size
        box_size=3
    elif size==4:
        cell_size=110
        grid_size=cell_size*size
        box_size=2
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
#if left button on mouse has been clicked,get coordinate/position for cell, to then fill when key is selected
                pos=pygame.mouse.get_pos()
                try:
                  #this is defined to match the grid, to be able to identify coordinates
                  if pos[0]<=(grid_size+10) and pos[0]>=10 and pos[1]<=(grid_size+10) and pos[1]>=10:
                    global x
                    x=int(pos[0])//(grid_size//size)
                    global y
                    y=int(pos[1])//(grid_size//size)
                    if grid[x][y]=="":
                        print(x,y) 
                  #this is defined to match the buttons, to be able to identify value selected
                  if pos[0]>=475 and pos[0]<=515 and pos[1]>=10 and pos[1]<=370:
                    for i in range(0,size):
                        if pos[1]>=10+(i*40) and pos[1]<=10+((i*40)+40):
                            val=i+1
                            print(val)
                except:
                    time.sleep(0.001)
                #try except used to avoid error when anywhere else on screen selected
                if solve_button_rect.collidepoint(event.pos):
                    solved=solvesudoku(size)
                    if solved!=True:
                        errormessage = fontsmaller.render("Unsolvable sudoku",True, (255,0,0))
                        screen.blit(errormessage,pygame.Vector2(10,470))
                        pygame.display.flip()
                        time.sleep(2)
                    draw_numbers(size)
                    print(grid)
                #if check button selected checks user inputs by calling subroutine
                if check_button_rect.collidepoint(event.pos):
                    check_correct(size)
                #if delete button selected, deletes selected cell, as long as it's not a set value
                if delete_button_rect.collidepoint(event.pos):
                    if initial_problem[x][y]=="":
                        grid[x][y]=""
                    else:
                        errormessage = fontsmaller.render("Can't delete set value",True, (255,0,0))
                        screen.blit(errormessage,pygame.Vector2(10,470))
                        pygame.display.flip()
                        time.sleep(2)
                if enter_button_rect.collidepoint(event.pos):
                    clear_grid(size)
                #code below clear_grid followed by mainclassic to generate a classic sudoku
                #so that new values can be assigned to each cell without any errors 
                if classic_button_rect.collidepoint(event.pos):
                    clear_grid(size)
                    mainclassic() 
                #code below clear_grid followed by mainfour to generate a 4x4 sudoku
                #so that new values can be assigned to each cell without any errors
                if four_button_rect.collidepoint(event.pos):
                    clear_grid(size)
                    mainfour() 
                if exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
        if event.type == pygame.KEYDOWN:
            key_mapping = {
                pygame.K_1: 1,
                pygame.K_2: 2,
                pygame.K_3: 3,
                pygame.K_4: 4,
                pygame.K_5: 5 if size == 9 else None,
                pygame.K_6: 6 if size == 9 else None,
                pygame.K_7: 7 if size == 9 else None,
                pygame.K_8: 8 if size == 9 else None,
                pygame.K_9: 9 if size == 9 else None,
            }
            val = key_mapping.get(event.key)
        #if event.type==pygame.KEYDOWN:
        #    if event.key == pygame.K_1:
        #        val = 1                => etc if i were to write it this way
    try:
      if val!=0:
        #have to check against initial as the grid changes with user input
        if initial_problem[x][y]=="":
            if check_input(x, y, val, size, box_size)==False:
                errormessage1 = fontsmaller.render("This value can't go here, try again",True, (255,0,0))
                screen.blit(errormessage1,pygame.Vector2(10,465))
                pygame.display.flip()
                time.sleep(1)
            if check_input(x, y, val, size, box_size)==True:
                grid[x][y]=val
                pygame.display.flip()
        else:
            if  initial_problem[x][y]!="":
                errormessage2 = fontsmaller.render("Can't overwrite this value",True, (255,0,0))
                screen.blit(errormessage2,pygame.Vector2(10,465))
                pygame.display.flip()
                time.sleep(1)
    except:
        errormessage4 = fontsmaller.render("No cell selected",True, (255,0,0))
        screen.blit(errormessage4,pygame.Vector2(10,465))
        pygame.display.flip()
        time.sleep(1)
    #the try except is to avoid the program crashing when no cell is selected

    draw_grid(size)
    draw_buttons(size)
    draw_numbers(size)
    pygame.display.flip()

def mainclassic():
    createGrid(9)
    fill_cells(9)
    hide_values()
    print(solution)
    print(initial_problem)
    while True:
        game_loop_classic(9)

def mainfour():
    createGrid(4)
    fill_cells(4)
    fourxhide_values()
    print(solution)
    print(initial_problem)
    while True:
        game_loop_classic(4)

#initiates the game
mainclassic()