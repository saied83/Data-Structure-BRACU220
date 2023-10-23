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


def atm_triangle(n):
    newArray = np.full((n,n), None)
    row, column = newArray.shape


    for rowIndex in range(row):
        for columnIndex in range(column):

            if rowIndex == columnIndex:
                newArray[rowIndex][columnIndex] = rowIndex + 1
                newArray[rowIndex][0] = rowIndex + 1

            elif rowIndex > 1 and columnIndex > 0 and rowIndex > columnIndex:
                sum = 0
                for p in range(columnIndex+1):
                    sum += newArray[rowIndex-1][p]
                newArray[rowIndex][columnIndex] = sum
    return newArray


def print_without_none(matrix):
  row, col = matrix.shape
  for i in range(row):
    for j in range(col):
        if matrix[i][j] != None:
            print(matrix[i][j], end=" ")
    print()
n = 5
returned_value = atm_triangle(n)
print_without_none(returned_value)
#This should print
# 1
# 2  2
# 3  4  3
# 4  7  10  4
# 5  11 21  25  5