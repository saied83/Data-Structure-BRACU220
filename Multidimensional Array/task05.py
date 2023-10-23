# You must run this cell to install dependency
! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np

#You must run this cell to print matrix and for the driver code to work
def print_matrix(m):
  row,col = m.shape
  for i in range(row):
    c = 1
    print('|', end='')
    for j in range(col):
      c += 1
      if(len(str(m[i][j])) == 1):
        print(' ',m[i][j], end = '  |')
        c += 6
      else:
        print(' ',m[i][j], end = ' |')
        c += 6
    print()
    print('-'*(c-col))


def moving_around(cmds):
    grid = np.full((7, 7), '.')
    positionX = 3
    positionY = 3

    indx = 0
    while indx < len(cmds):
        if indx == 0:
            grid[positionX][positionY] = "-"
        elif indx == len(cmds)-1:
            grid[positionX][positionY] = "/"
        else:
            grid[positionX][positionY] = "*"
        element = cmds[indx]

        if element == 1:
                positionX -= 2
                positionY -= 3

        elif element == 2:
                positionX -= 2
                positionY -= 1

        elif element == 3:
                positionX -= 3
                positionY -= 2

        elif element == 4:
                positionX -= 1
                positionY -= 2

        elif element == 5:
                positionX -= 2
                positionY += 1

        elif element == 6:
                positionX -= 2
                positionY += 3

        elif element == 7:
                positionX -= 3
                positionY += 2

        elif element == 8:
                positionX -= 1
                positionY += 2

        elif element == 9:
                positionX += 2
                positionY -= 3

        elif element == 10:
                positionX += 2
                positionY -= 1

        elif element == 11:
                positionX += 1
                positionY -= 2

        elif element == 12:
                positionX += 3
                positionY -= 2

        if 0 <= positionX <= 7 and 0 <= positionY <= 7:
            grid[positionX][positionY] = "/"
        indx += 1
    return grid


cmds = np.array([5,11,2,9])
result = moving_around(cmds)
print_matrix(result)
#This should print
# -------------------------------------------
# |  .  |  /  |  .  |  .  |  .  |  .  |  .  |
# -------------------------------------------
# |  .  |  .  |  .  |  .  |  *  |  .  |  .  |
# -------------------------------------------
# |  .  |  .  |  *  |  .  |  .  |  .  |  .  |
# -------------------------------------------
# |  .  |  .  |  .  |  -  |  .  |  .  |  .  |
# -------------------------------------------
# |  .  |  .  |  .  |  .  |  .  |  .  |  .  |
# -------------------------------------------
# |  .  |  .  |  .  |  .  |  .  |  .  |  .  |
# -------------------------------------------
# |  .  |  .  |  .  |  .  |  .  |  .  |  .  |
# -------------------------------------------