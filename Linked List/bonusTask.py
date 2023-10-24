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

def countElementNumber(head):
  temp = head
  count = 0
  while temp != None:
    count += 1
    temp = temp.next
  return count

def assemble_conga_line(conga_line, candidate_line, idx):

    temp = conga_line
    count = 1
    tempHead = conga_line

    while temp != None:
        if count == idx:
            tempHead = temp
        temp = temp.next
        count += 1

    prev = tempHead
    next = tempHead.next

    curr = candidate_line
    element = None
    diff = float('inf')

    if tempHead == conga_line:
        tempElement = tempHead.elem

        while curr != None:
            if curr.elem < tempElement:
                diff1 = tempElement - curr.elem
                if diff1 < diff:
                    diff = diff1
                    element = curr.elem
            curr = curr.next

        newNode = Node(element)
        newNode.next = prev
        return newNode

    else:
        prevElement = tempHead.elem
        nextElement = tempHead.next.elem

        while curr != None:
            if prevElement <= curr.elem <= nextElement:
                diff1 = prevElement - curr.elem
                diff2 = nextElement - curr.elem
                newDiff = 0

                if diff1 < diff2:
                    newDiff = diff1
                else:
                    newDiff = diff2

                if newDiff < diff:
                    diff = newDiff
                    element = curr.elem
            curr = curr.next

        if element == None:
            return conga_line
        else:
          newNode = Node(element)
          prev.next = newNode
          newNode.next = next
          return conga_line



print('==============Test Case 1=============')
conga_line = createList(np.array([10,15,34,41,56,72]))
print('Original Conga Line: ', end = ' ')
printLinkedList(conga_line)
candidate_line = createList(np.array([16,2,36,52,40,77]))
print('Original candidate Line: ', end = ' ')
printLinkedList(candidate_line)
insertion_idx = 3
returned_value = assemble_conga_line(conga_line, candidate_line, insertion_idx)
print('Changed Conga Line: ', end = ' ') #This should print 10-->15-->34-->40-->41-->56-->72
printLinkedList(returned_value)

print('==============Test Case 2=============')
conga_line = createList(np.array([10,15,34,41,56,72]))
print('Original Conga Line: ', end = ' ')
printLinkedList(conga_line)
candidate_line = createList(np.array([6,16,8,36,7,40,77]))
print('Original candidate Line: ', end = ' ')
printLinkedList(candidate_line)
insertion_idx = 0
returned_value = assemble_conga_line(conga_line, candidate_line, insertion_idx)
print('Changed Conga Line: ', end = ' ') #This should print 8-->10-->15-->34-->41-->56-->72
printLinkedList(returned_value)

print('==============Test Case 3=============')
conga_line = createList(np.array([10,15,34,41,56,72]))
print('Original Conga Line: ', end = ' ')
printLinkedList(conga_line)
candidate_line = createList(np.array([6,12,8,36,7,40,77]))
print('Original candidate Line: ', end = ' ')
printLinkedList(candidate_line)
insertion_idx = 2
returned_value = assemble_conga_line(conga_line, candidate_line, insertion_idx)
print('Changed Conga Line: ', end = ' ') #This should print 10-->15-->34-->41-->56-->72
printLinkedList(returned_value)