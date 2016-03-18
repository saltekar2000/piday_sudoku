# special pi-day sudoku solver
# http://brainfreezepuzzles.com/piday2008.html

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

piday_digits = [3,1,4,1,5,9,2,6,5,3,5,8]

def parse_grid( piday_grid ):
    grid = -np.ones((GRIDSIZE,GRIDSIZE),dtype = int)
    for i in range(GRIDSIZE):
        for j in range(GRIDSIZE):
            grid[i][j] = int(piday_grid[i][j]) if piday_grid[i][j] != 'x' else -1
    return grid
    
def parse_blobs( piday_blobs ):
    pb = np.array([list(r) for r in piday_blobs])
    uniq_id = list(set(pb.flatten()))
    blob_map = -np.ones(pb.shape,dtype=int)
    for i in range(len(uniq_id)):
        blob_map[pb == uniq_id[i]] = i
    return blob_map

def parse_digits( piday_digits ):
    digit_limit = np.zeros((10,1),dtype=int)
    for idx in piday_digits:
        digit_limit[idx] += 1
    return digit_limit

def too_many_repeats( x, digit_limit ):
    count = np.zeros((10,1),dtype=int)
    for idx in x:
        if idx >= 0:
            count[idx] += 1
    return any(count > digit_limit)

def valid_grid( grid, blob_map, digit_limit, i, j ):
    if too_many_repeats(grid[blob_map==blob_map[i][j]], digit_limit):
        return False
    if too_many_repeats(grid[i,:], digit_limit):
        return False
    if too_many_repeats(grid[:,j], digit_limit):
        return False
    return True

sudoku_solution = []

def find_solution( grid, blob_map, digit_limit, i = 0, j = 0 ):
    while grid[i][j] >= 0:
        i += 1
        if i == GRIDSIZE:
            j += 1
            if j == GRIDSIZE:
                print grid
                sudoku_solution = deepcopy(grid) 
                return True
            i = 0
    flag = False
    for value in set(piday_digits):
        grid[i][j] = value
        if valid_grid( grid, blob_map, digit_limit, i, j ):
            flag = find_solution( grid, blob_map, digit_limit, i, j )
            if flag: break
    grid[i][j] = -1
    return flag
    
grid = parse_grid(piday_grid ) 
blob_map = parse_blobs(piday_blobs )
digit_limit = parse_digits( piday_digits )

find_solution(grid, blob_map, digit_limit)


