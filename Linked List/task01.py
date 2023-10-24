# You must run this cell to install dependency
! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np

#Run this cell
class Node:
  def __init__(self,elem,next = None):
    self.elem,self.next = elem,next

def createList(arr):
  head = Node(arr[0])
  tail = head
  for i in range(1,len(arr)):
    newNode = Node(arr[i])
    tail.next = newNode
    tail = newNode
  return head

def printLinkedList(head):
  temp = head
  while temp != None:
    if temp.next != None:
      print(temp.elem, end = '-->')
    else:
      print(temp.elem)
    temp = temp.next
  print()

def rotation_times(head):
  temp = head
  count = 1
  loopCount = 1
  while temp.next != None:
    if temp.elem < temp.next.elem:
      return count
    else:
      count += 1
    temp = temp.next
    loopCount += 1

  if loopCount == count:
    return 0



print('==============Test Case 1=============')
head = createList(np.array([13,10,6,20,17]))
print('Rearranged Necklace: ', end = ' ')
printLinkedList(head)
returned_value = rotation_times(head)
print(f'Rotated: {returned_value} times') #This should print 3
unittest.output_test(returned_value, 3)
print()

print('==============Test Case 2=============')
head = createList(np.array([6,20,17,13,10]))
print('Rearranged Necklace: ', end = ' ')
printLinkedList(head)
returned_value = rotation_times(head)
print(f'Rotated: {returned_value} times') #This should print 1
unittest.output_test(returned_value, 1)
print()

print('==============Test Case 3=============')
head = createList(np.array([20,17,13,10,6]))
print('Rearranged Necklace: ', end = ' ')
printLinkedList(head)
returned_value = rotation_times(head)
print(f'Rotated: {returned_value} times') #This should print 0
unittest.output_test(returned_value, 0)
print()