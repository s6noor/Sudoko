# This program is written to solve a soduko puzzle
# In the test version, ill just be putting in a puzzle myself and focus on solving the case first

# Rules of soduko
# numbers 1-9 exist only once in every row, column and 3 by 3 box.

# My steps for solving a puzzle:
# 1- Find out all the rows and columns a number cant be in (in the entire 9 x 9)
# 2- What other number can be in this box? i.e what other number is needed in this row, column or 3x3 area that can possibly go here
# 3- if no other number can be in the box, then we put that number in the empty spot
# 4- Repeat until a box is completed.

import numpy as np
#sample puzzle for solving
puzzle = np.array([[4,0,6,3,1,0,0,0,8],
                    [0,0,0,0,0,2,5,0,0],
                    [9,8,0,0,6,0,0,7,3],
                    [0,3,0,0,0,1,8,5,9],
                    [0,4,0,0,0,0,0,6,0],
                    [2,1,9,8,0,0,0,3,0],
                    [5,9,0,0,4,0,0,1,7],
                    [0,0,1,6,0,0,0,0,0],
                    [7,0,0,0,9,5,3,0,2]])
print(puzzle)
# 1- check the neighborhood of a particular cell and find the 3 by 3 around
def get_neighborhood(matrix,index1,index2):
    mrow = int(index1/3)*3
    mcolumn = int(index2/3)*3
    cube = matrix[mrow:mrow+2,mcolumn:mcolumn+2]
    return cube

# 2- identify the restrictions for all number based on a matrix
def find_restrictions(matrix):
    restricted_areas = list()
    count = 0;
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0: continue #if its 0, it just means its empty
            # otherwise, if the number is between 1-9 then find its row and column and
            # make a restriction, thus the number cant be in that row or column anymore.
            # the format of the output will be [number,list_rows,list_columns]
            restricted_areas.append([matrix[i][j],i,j])
    return restricted_areas

# 3- Just realized how silly the array declaration was, have to generate a loop to
# extract columns each time
def find_colnums(matrix,c):
    cols = list()
    for i in range(len(matrix)):
        cols.append(matrix[i][c])
    return cols

#check output of function
#x=find_restrictions(puzzle)
#print(x)
#print(get_neighborhood(puzzle,0,6))
#print(find_colnums(puzzle,0))
#print(find_colnums(x,0))
#YAAAYYY IT WORKSSS

# 4- check if a certain number can be in a certain position, if there are no restrictions
# return false, if there is a restriction on the particular row and column return true
def check_restrictions(matrix,row,column,number):
    x = find_restrictions(matrix)
    #print(x)
    count = list()
    for i in range(0,len(x)):
        if x[i][0] == number and (x[i][1] == row or x[i][2] == column):
            count.append(i)
    if len(count) >= 1: return True
    else: return False

# 5- check all the numbers that can be in a certain position
# for this, i need to check all three: rows, columns and the cube around
def find_options(matrix,r,c):
    options = list()
    for i in range(1,10):
        if check_restrictions(matrix,r,c,i) is False:
            options.append(i)

    #now check if the number is already somewhere in the neighborhood cube, if so
    #remove it
    x = get_neighborhood(matrix,r,c)
    #print(x)
    for i in range(0,2):
        for j in range(0,2):
            if x[i][j] in options:
                options.remove(x[i][j])
    return options

#Validate results
#print(check_restrictions(puzzle,0,6,2))
#print(find_options(puzzle,0,6))
#HELL YAAASSS IT WORKSSS

# 6- find the positions for all the empty spots in the puzzle
def find_zeros(matrix):
    locations = list()
    for i in range(0,9):
        for j in range(0,9):
            if matrix[i][j] == 0: locations.append([i,j])
    return locations

#7 - fill in the numbers when no other option
def fill_nums(matrix):
    zeros = find_zeros(matrix)
    #print(zeros)
    for i in zeros:
        row = i[0]
        column = i[1]
        x= find_options(matrix,row,column)
        #print(x)
        if len(x) > 1: continue
        if len(x) == 1:
            matrix[row][column] = x[0]
    return matrix

#8 - main loop
while(True):
    num_zeros = len(find_zeros(puzzle))
    if num_zeros <= 0: break
    puzzle = fill_nums(puzzle)

print(puzzle)
