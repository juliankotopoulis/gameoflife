#game_of_life

# Add systems
import pygame
#import tkinter as tk
#from tkinter import messagebox
from button import button
from buttons import buttons
from slider import slider
from grid_class import grid_class

# Define the shapes that will be called when a button is pressed
def add_floater(x,y):
    grib.add_shape(x,y,[[1,0],[2,1],[0,2],[1,2],[2,2]])

def add_explosion(x,y):
    grib.add_shape(x,y,[[1,0],[0,1],[1,1],[2,1],[0,2],[2,2],[1,3]])

def add_big_explosion(x,y):
    grib.add_shape(x,y,[[0,0],[0,1],[0,2],[0,3],[0,4],[2,0],[2,4],[4,0],[4,1],[4,2],[4,3],[4,4]])

def add_spaceship(x,y):
    grib.add_shape(x,y,[[0,1],[0,3],[1,0],[2,0],[3,0],[4,0],[4,1],[4,2],[3,3]])

def add_floater_eater(x,y):
    grib.add_shape(x,y,[[0,0],[0,1],[1,0],[2,1],[2,2],[2,3],[3,3]])

def add_spaceship_eater(x,y):
    grib.add_shape(x,y,[[0,0],[0,1],[1,0],[2,1],[2,2],[2,3],[3,3]])

def add_R_pentomino(x,y):
    grib.add_shape(x,y,[[0,1],[1,0],[1,1],[1,2],[2,0]])

def add_glider_gun(x,y):
    grib.add_shape(x, y, [[0,4],[0,5],[1,4],[1,5],[10,4],[10,5],[10,6],[11,3],[11,7],[12,2],[13,2],[12,8],[13,8],[14,5],[15,3],[15,7],[16,4],[16,5],[16,6],[17,5],
                     [20,2],[20,3],[20,4],[21,2],[21,3],[21,4],[22,1],[22,5],[24,0],[24,1],[24,5],[24,6],[34,2],[34,3],[35,2],[36,3]])

def add_glider_gun_eater(x,y):
    grib.add_shape(x, y, [[0, 0], [0, 1], [1, 0], [2, 1], [2, 2], [2, 3], [3, 3]])

def add_reverse_glider_gun(x,y):
    grib.add_shape(x, y, [[0,5],[0,6],[1,5],[1,6],[11,2],[11,3],[11,7],[11,8],[13,3],[13,7],[14,4],[14,5],[14,6],[15,4],[15,5],[15,6],[18,3],[19,2],[19,3],
                     [19,4],[20,1],[20,5],[21,3],[22,0],[22,6],[23,0],[23,6],[24,1],[24,5],[25,2],[25,3],[25,4],[34,3],[34,4],[35,3],[35,4]])

def add_medium_spaceship(x,y):
    grib.add_shape(x, y, [[0, 1], [0, 3], [2, 0], [1, 4], [2, 4], [3, 4], [4, 4],[5, 4],[5, 3],[5, 2],[4, 1]])

def add_large_spaceship(x,y):
    grib.add_shape(x, y, [[0, 1], [0, 3], [2, 0], [1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4],[6, 3], [6, 2], [5, 1],[3, 0]])

def add_John_Conway(x,y):
    grib.add_shape(x, y, [[2,0],[3,0],[4,0],[4,1],[2,1],[2,2],[4,2],[3,3],[2,4],[4,4],[0,4],[1,5],[3,4],[3,5],[3,6],[2,7],[2,8],[4,7],[4,8],
                     [5,5],[6,6]])

def add_smile(x,y):
    grib.add_shape(x, y, [[0,2],[1,0],[1,3],[2,3],[3,3],[4,2],[3,0]])

def add_ten_cell_line(x,y):
    grib.add_shape(x, y, [[0,0],[1,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0]])

def add_scp_096(x,y):
    grib.add_shape(x, y, [[0,0],[1,0],[2,0],[4,0],[5,0],[6,0],[8,0],[9,0],[10,0],[16,0],[17,0],[18,0],[20,0],[21,0],[22,0],[24,0],[25,0],[26,0],
                     [0,1],[4,1],[8,1],[10,1],[16,1],[18,1],[20,1],[22,1],[24,1],[0,2],[1,2],[2,2],[4,2],[8,2],[9,2],[10,2],[12,2],[13,2],[14,2],
                     [16,2],[18,2],[20,2],[21,2],[22,2],[24,2],[25,2],[26,2],[2,3],[4,3],[8,3],[16,3],[18,3],[22,3],[24,3],[26,3],[0,4],[1,4],[2,4],
                     [4,4],[5,4],[6,4],[8,4],[16,4],[17,4],[18,4],[22,4],[24,4],[25,4],[26,4]])

def add_sirenhead(x,y):
    grib.add_shape(x, y, [[3,0],[3,1],[4,1],[6,1],[7,1],[3,2],[4,2],[5,2],[6,2],[7,2],[10,2],[3,3],[4,3],[5,3],[6,3],[7,3],[9,3],[10,3],[3,4],[4,4],[6,4],
                     [7,4],[8,4],[9,4],[10,4],[3,5],[6,5],[7,5],[8,5],[9,5],[10,5],[6,6],[7,6],[9,6],[10,6],[6,7],[7,7],[10,7],[6,8],[7,8],[0,9],[1,9],
                     [2,9],[3,9],[4,9],[5,9],[6,9],[7,9],[8,9],[9,9],[10,9],[11,9],[12,9],[13,9],[0,10],[1,10],[2,10],[3,10],[4,10],[5,10],[6,10],[7,10],
                     [8,10],[9,10],[10,10],[11,10],[12,10],[13,10],[0,11],[1,11],[5,11],[6,11],[7,11],[8,11],[12,11],[13,11],[0,12],[1,12],[3,12],[4,12],
                     [6,12],[7,12],[9,12],[10,12],[12,12],[0,13],[5,13],[6,13],[7,13],[8,13],[12,13],[13,13],[0,14],[1,14],[3,14],[4,14],[6,14],[7,14],[9,14],
                     [10,14],[12,14],[13,14],[0,15],[1,15],[0,15],[5,15],[6,15],[7,15],[8,15],[12,15],[13,15],[0,16],[1,16],[3,16],[4,16],[6,16],[7,16],
                     [9,16],[10,16],[12,16],[13,16],[0,17],[1,17],[5,17],[6,17],[7,17],[8,17],[12,17],[13,17],[0,18],[1,18],[3,18],[4,18],[6,18],[7,18],[9,18],
                     [10,18],[12,18],[13,18],[0,19],[1,19],[5,19],[6,19],[7,19],[8,19],[12,19],[13,19],[0,20],[1,20],[3,20],[4,20],[6,20],[7,20],[9,20],[10,20],
                     [12,20],[13,20],[6,21],[7,21],[4,22],[5,22],[6,22],[7,22],[8,22],[9,22],[4,22],[4,23],[5,23],[8,23],[9,23],[4,24],[5,24],[8,24],[9,24],
                     [4,25],[5,25],[8,25],[9,25],[4,26],[5,26],[8,26],[9,26],[4,27],[5,27],[8,27],[9,27],[4,28],[5,28],[8,28],[9,28],[4,29],[5,29],[8,29],
                     [9,29],[4,30],[5,30],[8,30],[9,30],[4,31],[5,31],[8,31],[9,31],[4,32],[5,32],[8,32],[9,32],])

def add_line(x,y):
    grib.add_shape(x, y, [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],[15,0],[16,0],[17,0],[18,0],[19,0],
                          [20,0],[21,0],[22,0],[23,0],[24,0],[25,0],[26,0],[27,0],[28,0],[29,0],[30,0],])

# Something happens when a key is pressed.
def move():
    global myButtons
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        myButtons.proc_event(event)
        grib.proc_event(event)
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
                if greenslider.isOver(pos):
                    greenslider.clicked(pos)

        keys = pygame.key.get_pressed()

        # what shaped is added when which key is pressed
        for key in keys:
            if keys[pygame.K_UP]:
                add_floater(0, 0)
            if keys[pygame.K_DOWN]:
                add_explosion(28, 30)
            if keys[pygame.K_LEFT]:
                add_big_explosion(27,10)
            if keys[pygame.K_RIGHT]:
                add_spaceship(0,30)
            if keys[pygame.K_1]:
                add_spaceship_eater(30,33)
            if keys[pygame.K_2]:
                add_floater_eater(33,33)
            if keys[pygame.K_3]:
                add_R_pentomino(28,30)
            if keys[pygame.K_4]:
                add_glider_gun(0,0)
            if keys[pygame.K_5]:
                add_glider_gun_eater(47,33)
            if keys[pygame.K_6]:
                add_reverse_glider_gun(23,25)
            if keys[pygame.K_7]:
                add_medium_spaceship(0,28)
            if keys[pygame.K_8]:
                add_large_spaceship(0,25)
            if keys[pygame.K_9]:
                add_John_Conway(28,30)
            if keys[pygame.K_0]:
                add_smile(28,30)
            if keys[pygame.K_q]:
                add_ten_cell_line(25,40)
            if keys[pygame.K_w]:
                add_scp_096(18,30)
            if keys[pygame.K_e]:
                add_sirenhead(23,10)

# Grid updates to show changes (which spates have died and which survived)
def redrawWindow(surface):
    global rows, width,screenwidth, screenheight, greenslider, grib
    surface.fill((0,0,0))
    grib.draw(surface)

    grib.draw_cells(surface)
    pygame.draw.rect(surface, (0,0,255), (width, 0, 580, screenheight), 0)
    pygame.draw.rect(surface, (0,0,255), (0, width, screenwidth, 50), 0)
    myButtons.draw(surface)
    greenslider.draw(surface)
    pygame.display.update()

# Not currently used
'''
def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass
'''

# button to clear the screen
def clickclear(pos):
    grib.create_grid_empty()

# Where each spawns in when called
def floater(pos):
    add_floater(0, 0)
def explosion(pos):
    add_explosion(28, 30)
def big_explosion(pos):
    add_big_explosion(27, 10)
def spaceship(pos):
    add_spaceship(0, 30)
def spaceship_eater(pos):
    add_spaceship_eater(30, 33)
def floater_eater(pos):
    add_floater_eater(33, 33)
def R_pentomino(pos):
    add_R_pentomino(28, 30)
def glider_gun(pos):
    add_glider_gun(0, 0)
def glider_gun_eater(pos):
    add_glider_gun_eater(47, 33)
def reverse_glider_gun(pos):
    add_reverse_glider_gun(23, 25)
def medium_spaceship(pos):
    add_medium_spaceship(0, 28)
def large_spaceship(pos):
    add_large_spaceship(0, 25)
def john_conway(pos):
    add_John_Conway(28, 30)
def smile(pos):
    add_smile(28, 30)
def ten_cell_line(pos):
    add_ten_cell_line(25, 40)
def scp_096(pos):
    add_scp_096(18, 30)
def sirenhead(pos):
    add_sirenhead(23, 10)
def line(pos):
    add_line(15,30)

# Main function to run the game
def main():
    global myButtons, greenslider, grib
    pygame.init()
    myButtons = buttons()
    global width, rows, grid, screenwidth, screenheight
    screenwidth = 1300
    screenheight = 770
    width = 720
    rows = 60
    grib = grid_class(0,0,width,width,rows)
    win = pygame.display.set_mode((screenwidth, screenheight))
    labels =["Floater", "Small Spaceship","Medium Spaceship","Large Spaceship","Floater Eater","Spaceship Eater","Floater Gun","Reverse Floater Gun","Floater Gun Eater","Explosion","Big Explosion","R Pentomino","John Conway","Smile","Ten Cell Line","SCP 096","Sirenhead","Line"]
    calls =[floater, spaceship, medium_spaceship, large_spaceship, floater_eater, spaceship_eater, glider_gun, reverse_glider_gun, glider_gun_eater, explosion, big_explosion, R_pentomino, john_conway, smile, ten_cell_line, scp_096, sirenhead, line]
    for i in range(18):
        myButtons.add(button( 734, 9 + i * 42, 550, 30, calls[i], labels[i],nomousecolor=(255,255,0),mouseovercolor=(0,255,255)))
    myButtons.add(button( 10, 728, 225, 35, clickclear, "clear",nomousecolor=(255,255,255),mouseovercolor=(255,0,255)))
    greenslider = slider(400, 725, 250, 25, 27, 0, 1000, 'Speed')
    flag = True
    clock = pygame.time.Clock()
    grib.create_grid_empty()

    while flag:
        pygame.time.delay(greenslider.value)
        clock.tick(100)
        move()
        redrawWindow(win)
        grib.update_grid()

main()