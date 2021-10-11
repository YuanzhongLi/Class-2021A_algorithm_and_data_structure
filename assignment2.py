from copy import deepcopy as dcp

# 0-indexed
def Left(i):
  return ((i+1)<<1)-1

def Right(i):
  return ((i+1)<<1)

def Parent(i):
  return (i-1)>>1


# H: size of Heap (Array)
def maxHeapify(A, i, H):
  if i >= H:
    return
  l, r = Left(i), Right(i)
  largest = None
  if l < H and A[l] > A[i]: largest = l
  else: largest = i
  if r < H and A[r] > A[largest]: largest = r

  if largest != i:
    A[i], A[largest] = A[largest], A[i]
    maxHeapify(A, largest, H)

# H: size of Heap (Array)
def minHeapify(A, i, H):
  if i >= H:
    return
  l, r = Left(i), Right(i)
  smallest = None
  if l < H and A[l] < A[i]: smallest = l
  else: smallest = i
  if r < H and A[r] < A[smallest]: smallest = r

  if smallest != i:
    A[i], A[smallest] = A[smallest], A[i]
    minHeapify(A, smallest, H)

# O(N) Note: not NlogN
def Heapify(A, type="max"):
  H = len(A)
  if type == "max":
    for i in range((H-1)>>1, -1, -1):
      maxHeapify(A, i, H)
  else:
    for i in range((H-1)>>1, -1, -1):
      minHeapify(A, i, H)

# O(logN)
def Heappush(A, x, type="max"):
  i = len(A)
  A.append(x)
  if type == "max":
    while i > 0:
      p = Parent(i)
      if A[p] < A[i]:
        A[p], A[i] = A[i], A[p]
        i = p
      else:
        break
  else:
    while i > 0:
      p = Parent(i)
      if A[p] > A[i]:
        A[p], A[i] = A[i], A[p]
        i = p
      else:
        break

# O(logN)
def Heappop(A, type="max"):
  ret = A[0]
  A[0] = A[-1]
  A.pop()
  if type == "max":
    maxHeapify(A,0,len(A))
  else:
    minHeapify(A,0,len(A))
  return ret

class MyHeap():
  def __init__(self, A, type="max"):
    self.Array = dcp(A)
    self.type = type
    Heapify(self.Array, self.type)

  def __pr__(self):
    return self.type + " heap: " + self.Array.join(', ')

  def push(self, x):
    type = self.type
    Heappush(self.Array, x, type)

  def pop(self):
    type = self.type
    return Heappop(self.Array, type)

from random import randint
H = 20
A = [0 for _ in range(H)]
for i in range(H):
  A[i] = randint(-H, H)

B = dcp(A)
B.sort()
heap = MyHeap(A, "min")

print(A)
print(B)
print(heap)

for _ in range(H):
  print(heap.pop())
