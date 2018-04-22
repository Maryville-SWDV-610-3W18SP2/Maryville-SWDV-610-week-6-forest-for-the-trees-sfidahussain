'''
1) Generate a random list of integers.  
Show the binary heap tree resulting from inserting the integers on the list
one at a time.
2) Using the list from the previous question, show the binary heap tree resulting
from the list as a parameter to the buildHeap method.  
Show both the tree and list form.
3) Extend the buildParseTree function to handle mathematical expressions that do not
have spaces between every character.
4) Extend the buildParseTree and evaluate functions to handle boolean statements.
Remember that "not" is a unary operator, so this will complicate your code somewhat.
'''

import math
import string

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval

    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1
        
        # root arr[0]
        # Arr[(i-1)/2]	Returns the parent node
        # Arr[(2*i)+1]	Returns the left child node
        # Arr[(2*i)+2]	Returns the right child node
        
    def displayHeapList(self):
        print(self.heapList)
    
    def showTree(self):
        tree = self.heapList
        total_width=36
        fill = ' '
        output = ''
        last_row = -1
        for i, n in enumerate(tree[1:]):
            if i:
                row = int(math.floor(math.log(i+1, 2)))
            else:
                row = 0
            if row != last_row:
                print()
            columns = 2**row
            col_width = int(math.floor((total_width * 1.0) / columns))
            print(str(n).center(col_width, fill), end="")
            last_row = row
        print(output)
        print('-' * total_width)
        print()
        return
        
def main():
    bh = BinHeap()
    data = [1, 3, 6, 5, 9, 8]
    
    for n in data:
        print('Adding {}: '.format(n))
        bh.insert(n)
        bh.showTree()
    
    bh2 = BinHeap()
    bh2.buildHeap(data)
    print()
    print('buildHeap List Form: ')
    bh2.displayHeapList()
    
    print('buildHeap Tree Form: ')
    bh2.showTree()

main()