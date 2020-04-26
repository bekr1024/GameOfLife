# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 19:13:19 2020

@author: BenK
"""
import random

# Personal attempt at a Conway Game of Life.

rand_grid = [[random.randint(0,1) for x in range(25)] for y in range(25)]

                #1       5         10        15        20
initial_grid = [[0,0,0,0,1,0,1,0,1,1,0,0,1,0,1,1,0,1,1,0], #1
                [0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,1,0,0], 
                [1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0],
                [0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,1,0], 
                [0,0,0,1,1,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0], #5
                [1,0,1,0,0,0,0,1,0,1,0,1,1,1,0,1,1,0,0,1], 
                [1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1],
                [1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,1,0,1,1], 
                [0,1,1,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,1,0],
                [0,0,0,0,1,0,0,0,0,0,1,1,1,0,1,1,1,1,1,0], #10
                [0,0,0,0,1,0,0,0,0,0,1,1,1,0,1,1,1,1,1,0],
                [0,0,0,0,1,0,0,0,0,0,1,1,1,0,1,1,1,1,1,0],
                [1,0,1,0,0,0,0,1,0,1,0,1,1,1,0,1,1,0,0,1],
                [1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0],
                [0,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0,1,0,0], #15
                [0,0,0,0,1,0,1,0,1,1,0,0,1,0,1,1,0,1,1,0],
                [1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1],
                [1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1],
                [0,0,0,0,1,0,0,0,0,0,1,1,1,0,1,1,1,1,1,0],
                [0,0,0,0,1,0,0,0,0,0,1,1,1,0,1,1,1,1,1,0]] #20

block = [[0,0,0,0],
         [0,1,1,0],
         [0,1,1,0],
         [0,0,0,0]]

beehive = [[0,0,0,0,0,0],
           [0,0,1,1,0,0],
           [0,1,0,0,1,0],
           [0,0,1,1,0,0],
           [0,0,0,0,0,0],
           [0,0,0,0,0,0]]

loaf = [[0,0,0,0,0,0],
        [0,0,1,1,0,0],
        [0,1,0,0,1,0],
        [0,0,1,1,0,0],
        [0,0,0,0,0,0]]

boat = [[0,0,0,0,0],
        [0,1,1,0,0],
        [0,1,0,1,0],
        [0,0,1,0,0],
        [0,0,0,0,0]]

tub = [[0,0,0,0,0],
       [0,0,1,0,0],
       [0,1,0,1,0],
       [0,0,1,0,0],
       [0,0,0,0,0]]

blinker = [[0,0,0,0,0],
           [0,0,0,0,0],
           [0,1,1,1,0],
           [0,0,0,0,0],
           [0,0,0,0,0]]

toad = [[0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,1,1,1,0],
        [0,1,1,1,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]]

beacon = [[0,0,0,0,0,0],
          [0,1,1,0,0,0],
          [0,1,0,0,0,0],
          [0,0,0,0,1,0],
          [0,0,0,1,1,0],
          [0,0,0,0,0,0]]

def update(grid):
    a = len(grid[0])
    
    new_grid = [[0 for x in range(a)] for y in range(a)]
    
    for i in range(a):
        for j in range(a):
            sum = (grid[(i-1)%a][(j-1)%a]       # Number 1 position
                + grid[(i+1)%a][(j-1)%a]        # Number 7 position
                + grid[(i-1)%a][(j+1)%a]        # Number 3 position
                + grid[(i+1)%a][(j+1)%a]        # Number 9 position
                + grid[(i+1)%a][j]              # Number 8 position
                + grid[(i-1)%a][j]              # Number 2 position
                + grid[i][(j+1)%a]              # Number 6 position
                + grid[i][(j-1)%a])             # Number 4 position
            #print(str(grid[(i-1)%a][(j-1)%a]))
            #print("[i][j] sum for[" + str(i) + "][" + str(j) + "] is:\t" + str(sum))
            if(grid[i][j] == 1):
                if(sum < 2 or sum > 3):
                    new_grid[i][j] = 0
                else:
                    new_grid[i][j] = 1
            elif(grid[i][j] == 0 and sum == 3):
                new_grid[i][j] = 1
    return new_grid

def one_update(grid):
    a = len(grid[0])
    new_grid = [[0 for x in range(a)] for y in range(a)]
    
    i = 1
    j = 1
    
    sum = (grid[(i-1)%a][(j-1)%a]       # Number 1 position
        + grid[(i+1)%a][(j-1)%a]        # Number 7 position
        + grid[(i-1)%a][(j+1)%a]        # Number 3 position
        + grid[(i+1)%a][(j+1)%a]        # Number 9 position
        + grid[(i+1)%a][j]              # Number 8 position
        + grid[(i-1)%a][j]              # Number 2 position
        + grid[i][(j+1)%a]              # Number 6 position
        + grid[i][(j-1)%a])             # Number 4 position
            
    if(grid[i][j] == 1):
        if(sum < 2 or sum > 3):
            new_grid[i][j] = 0
        else:
            new_grid[i][j] = 1
        
    elif(grid[i][j] == 0 and sum == 3):
        new_grid[i][j] = 1
    return new_grid    
    

def display(grid):
    row = ""
    for i in range(len(grid[0])):
        for j in range(len(grid[0])):
            if(grid[i][j] == 1):
                row = row + "O " 
            elif(grid[i][j] == 0):
                row = row + "- "
        row = row + "\n"
    print("\n")
    print(row)
    print("\n\n")

ex_grid = rand_grid

#print("ORIGINAL GRID\n")
#display(ex_grid)
#new_grid = update(ex_grid)
#print("\n\n\n")
#print("NEW GRID\n")
#display(new_grid)


while(True):
    display(ex_grid)
    
    try:
        input("")
        ex_grid = update(ex_grid)
        
    except KeyboardInterrupt:
        exit()
    

