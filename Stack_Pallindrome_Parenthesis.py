import array as array
import ctypes as c
import string as string
#Dynamic Array
class MyList:
    def __init__(self):
        self._capacity = 10
        self._length = 0
        self._elements = (self._capacity * c.py_object)()
        for i in range(self._capacity):
            self._elements[i] = 0
    
    def get_cap(self):
        return self._capacity

    def _len_(self):
        return self._length

    def get_elem(self):
        return self._elements

    def _getitem_(self,index):
        return self._elements[index]

    def append(self, item):
        if self._length <= self._capacity-1:
            self._elements[self._length] = item
            self._length += 1 
        else:
            temp = (self._capacity * c.py_object)()
            len = 0
            for i in range(self._length):
                temp[i] = self._elements[i]
                len += 1
            self._capacity += 10
            self._elements = (self._capacity * c.py_object)()
            for i in range(self._capacity):
                self._elements[i] = 0
            for i in range(len):
                self._elements[i] = temp[i]
            self._elements[self._length] = item
            self._length += 1

    def remove(self, item):
        temp = (self._length * c.py_object)()
        for i in range(self._length):
            temp[i] = self._elements[i]
        bindex = 0
        for i in range(self._length):
            if temp[i] == item:
                bindex = 0 + i
        ntemp1 = ((self._length-1) * c.py_object)()
        ntemp = self.removehelper(ntemp1,temp,bindex,self._length)
        for i in range(self._capacity):
                self._elements[i] = 0
        for i in range(self._length-1):
            self._elements[i] = ntemp[i]
        self._length -= 1   

    def removehelper(self,l1,l2,bi,len):
        i = 0
        b = 0
        while i <= len-2:
            if i != bi:
                l1[i] = l2[b]
                i = i + 1
                b = b + 1
                #print(i)
            elif i == bi:
                b = b + 1
                l1[i] = l2[b]
                print(b)
                i = i + 1
                b = b + 1
        return l1                 
    
    def print_elements(self):
        print(self._elements[0:self._length])
#############################################################################################
class Stack_Dynamic_Array:

    def __init__(self):
        LIST = MyList()
        self._items = LIST
    
    def isEmpty(self):
        return self._items._len_() == 0

    def push(self, data):
        self._items.append(data)

    def pop(self):
        item = self._items._getitem_(self._items._len_()-1)
        self._items.remove(item)
        return item

    def top(self):
        return self._items._getitem_(self._items._len_()-1)

    def _len_(self):
        return self._items._len_()

    def index(self,index):
        return self._items._getitem_(index)

    def print(self):
        i = self._len_() - 1
        while i != -1:
            print(self._items._getitem_(i))
            i = i - 1

#Tests
'''
MyStack = Stack_Dynamic_Array()
print(MyStack.isEmpty())
for i in range(15):
    MyStack.push(i+1)
print(MyStack.isEmpty())
MyStack.push(16)
print(MyStack.pop())
print(MyStack.top())
print(MyStack._len_()
MyStack.print()
'''

#############################################################################

def pallindrome():
    LIST = Stack_Dynamic_Array()
    input1 = input("Enter the pallindrome word: ")
    for i in input1:
        LIST.push(i)
    LIST2 = Stack_Dynamic_Array()
    for i in input1[::-1]:
        LIST2.push(i)
    Equal = True
    while Equal == True and LIST.isEmpty() != True:
        if LIST.pop() != LIST2.pop():
            Equal = False
    if Equal == True:
        print("The word you entered is a Palllindrome")
        pallindrome()
    else:
        print("The Word you entered is not a Pallindrome")
        pallindrome()
#pallindrome()

##################################################################################
def parenthesis():
    input1 = input("Enter the parenthesis: ")
    openers = ["[","{","("]
    closers = ["]","}",")"] 
    stack = Stack_Dynamic_Array()
    for i in input1:
        if i in openers:
            stack.push(i)
        elif i in closers:
            posn = closers.index(i)
            l = stack._len_()
            if l > 0 and openers[posn] == stack.index(l-1):
                stack.pop()
            else:
                print("The parenthesis you entered is not balanced")
                parenthesis()
    if stack.isEmpty():
        print("The parenthesis you entered is balanced")
        parenthesis()

#parenthesis()
    
    
    