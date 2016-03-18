from __future__ import division
import numpy as np
import re
from copy import deepcopy

# pi-day sudoku sizes
GRIDSIZE = 12    # 12x12 grid

piday_grid =   ['3xx154xx1x95',
                'x1xx3xxxx136',
                'xx4xx3x8xx2x',
                '5xx1xx925xx1',
                'x9xx5xx5xxxx',
                '581xx9xx3x6x',
                'x5x8xx2xx553',
                'xxxx5xx6xx1x',
                '2xx515xx5xx9',
                'x6xx4x1xx3xx',
                '151xxxx5xx5x',
                '55x4xx316xx8']
                
piday_blobs =  ['000111111222',
                '000111111222',
                '003333444422',
                '003333444422',
                '003333444422',
                '555667788999',
                '555667788999',
                '555667788999',
                '555667788999',
                'aaa667788bbb',
                'aaa667788bbb',
                'aaaaaabbbbbb']
                
                

def repeated_value( x ):
    count = np.zeros((GRIDSIZE+1,1),dtype=int)
    for idx in x:
        count[idx] += 1
    return any(count[1:]>1)

def valid_grid( grid, i, j ):
    slice_i = slice((i//BOXSIZE)*BOXSIZE,(1+i//BOXSIZE)*BOXSIZE)
    slice_j = slice((j//BOXSIZE)*BOXSIZE,(1+j//BOXSIZE)*BOXSIZE)
    if repeated_value(grid[slice_i, slice_j].flatten('F')):
        return False
    if repeated_value(grid[i,:]):
        return False
    if repeated_value(grid[:,j]):
        return False
    return True

sudoku_solution = []

def find_solution( grid, i = 0, j = 0 ):
    #print grid
    while grid[i][j] > 0:
        i += 1
        if i == GRIDSIZE:
            j += 1
            if j == GRIDSIZE:
                print grid
                sudoku_solution = deepcopy(grid) 
                return True
            i = 0
    flag = False
    for value in range(1,GRIDSIZE+1):
        grid[i][j] = value
        if valid_grid( grid, i, j ):
            flag = find_solution( grid, i, j )
            if flag: break
    grid[i][j] = 0
    return flag
    
            

