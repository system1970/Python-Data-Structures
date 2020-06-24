import math

MinHeap = []

def GetLeftChild(parentIndex):
    return 2* parentIndex +1
def GetRightChild(parentIndex):
    return 2* parentIndex +2
def GetParentIndex(childIndex):
    return math.ceil((childIndex - 1) / 2)

def hasLeftChild(index):
    return GetLeftChild(index) < len(MinHeap)
def hasRightChild(index):
    return GetRightChild(index) < len(MinHeap)
def hasParent(index):
    return GetParentIndex(index) >= 0

def leftChild(index):
    return MinHeap[GetLeftChild(index)]
def rightChild(index):
    return MinHeap[GetRightChild(index)]
def parent(index):
    return MinHeap[GetParentIndex(index)]

def swap(index1,index2):
    temp = MinHeap[index1]
    MinHeap[index1] = MinHeap[index2]
    MinHeap[index2] = temp


def peek():
    if len(MinHeap)==0:
        return "No Elements Available"
    return MinHeap[0]

def poll():
    if len(MinHeap)==0:
        return "No Elements Available"
    item = MinHeap[0]
    MinHeap[0] = MinHeap[-1]
    heapifyDown()
    return item

def add(item):
    MinHeap.append(item)
    heapifyUp()

def heapifyUp():
    index = len(MinHeap)-1
    while(hasParent(index) and parent(index) > MinHeap[index]):
        swap(GetParentIndex(index), index)
        index = GetParentIndex(index)

def heapifyDown():
    index = 0
    while hasLeftChild(index):
        smallerIndex = GetLeftChild(index)

        if hasRightChild(index) and rightChild(index) < leftChild(index):
            smallerIndex = GetRightChild(index)
        
        if MinHeap[index] < MinHeap[smallerIndex]:
            break
        else:
            swap(index,smallerIndex)
        index = smallerIndex

add(10)
add(20)
add(15)
add(17)
add(25)
add(10)
add(20)
add(15)
add(17)
add(25)



print("Min Heap: "+str(MinHeap))

for i in MinHeap:
    print(poll(),end=" ")
