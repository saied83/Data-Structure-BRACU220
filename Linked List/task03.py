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

def remove_compartment(head,n):
  temp = head
  rem = None

  if temp.elem ==n:
    return head.next

  while temp.next != None:
    if temp.next.elem == n:
      rem = temp
    temp = temp.next

  if rem != None:
    rem.next = rem.next.next
  return head



print('==============Test Case 1=============')
head = createList(np.array([14,10,15,10,41,10,72]))
number = 10
print('Original Compartment Sequence: ', end = ' ')
printLinkedList(head)
head = remove_compartment(head,number)
print('Changed Compartment Sequence: ', end = ' ')
printLinkedList(head) #This should print 14-->10-->15-->10-->41-->72
print()

print('==============Test Case 2=============')
head = createList(np.array([10,15,33,41,14,72]))
number = 10
print('Original Compartment Sequence: ', end = ' ')
printLinkedList(head)
head = remove_compartment(head,number)
print('Changed Compartment Sequence: ', end = ' ')
printLinkedList(head) #This should print 15-->33-->41-->14-->72
print()

print('==============Test Case 3=============')
head = createList(np.array([10,15,33,41,14,72]))
number = 56
print('Original Compartment Sequence: ', end = ' ')
printLinkedList(head)
head = remove_compartment(head,number)
print('Changed Compartment Sequence: ', end = ' ')
printLinkedList(head) #This should print 10-->15-->33-->41-->14-->72
print()