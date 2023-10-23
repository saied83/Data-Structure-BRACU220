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


def create_fence(district, depth):
    district_row, district_col = district.shape
    new_row = district_row + 2 * depth
    new_column = district_col + 2 * depth
    newArray = np.zeros((new_row, new_column), dtype = int)
    print(new_row, new_column)

    row = 0
    column = 0
    while row < new_row:
        while column < new_column:

            if row < depth or row > new_row-(depth+1) or column < depth or column > new_column -(depth+1):
                newArray[row][column] = 8

            else:
                newArray[row][column] = district[row-depth][column-depth]
            column += 1

        row += 1
        column = 0

    return newArray

depth = 1
district = np.array([[2,3,4], [3,4,6], [2,1,4]])
print_matrix(district)
ans = create_fence(district, depth)
print_matrix(ans)
#This will print
# |  8  |  8  |  8  |  8  |  8  |
# -------------------------------
# |  8  |  2  |  3  |  4  |  8  |
# -------------------------------
# |  8  |  3  |  4  |  6  |  8  |
# -------------------------------
# |  8  |  2  |  1  |  4  |  8  |
# -------------------------------
# |  8  |  8  |  8  |  8  |  8  |
# -------------------------------
print('################')
depth = 2
district = np.array([
                 [2,3,4,1],
                 [3,4,6,5],
                 [2,1,4,7]
                ])
print_matrix(district)
ans = create_fence(district, depth)
print_matrix(ans)
