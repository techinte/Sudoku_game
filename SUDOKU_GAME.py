#!/usr/bin/env python
# coding: utf-8

# In[13]:


m=9
def puzzle(a):
    for i in range(m):
        for j in range(m):
            print(a[i][j],end=" ")
        print()
def solve(grid,row,col,num):
    for x in range(9):
        if grid[row][x]==num:
            return False
    for x in range(9):
        if grid[x][col]==num:
            return False
    startrow=row-row%3
    startcol=col-col%3
    for i in range(3):
        for j in range(3):
            if grid[i+startrow][j+startcol]==num:
                return False
    return True
def sudoku(grid,row,col):
    if row==m-1 and col==m:
        return True
    if col==m:
        row+=1
        col=0
    if grid[row][col]>0:
        return sudoku(grid,row,col+1)
    for num in range(1,m+1,1):
        if solve(grid,row,col,num):
            grid[row][col]=num
            if sudoku(grid,row,col+1):
                return True
        grid[row][col]=0
    return False
grid=[[4,0,2,8,0,0,1,6,0],
      [8,0,0,2,0,9,5,4,0],
      [0,0,0,0,4,0,2,8,0],
      [9,4,1,0,2,0,8,3,5],
      [2,0,0,3,8,4,6,9,1],
      [6,8,3,0,9,0,4,7,2],
      [7,0,8,0,0,0,9,2,4],
      [3,2,4,9,0,8,7,0,6],
      [0,0,0,4,7,2,3,0,8]]
if(sudoku(grid,0,0)):
    puzzle(grid)
else:
    print('no solution')


# In[ ]:




