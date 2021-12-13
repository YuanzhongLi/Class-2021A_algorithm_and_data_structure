from heapq import heapify, heappop, heappush, heappushpop

# 小さい順にpopする
class PriorityQueue:
  def __init__(self, heap):
    '''
    heap ... list
    '''
    self.heap = heap
    heapify(self.heap)

  def push(self, item):
    heappush(self.heap, item)

  def pop(self):
    return heappop(self.heap)

  def pushpop(self, item):
    return heappushpop(self.heap, item)

  def __call__(self):
    return self.heap

  def __len__(self):
    return len(self.heap)

  def __repr__(self):
    return str(self.heap)

H = 10
W = 11
dy = [-1, 0, 1, 0] # up, right, down, left
dx = [0, 1, 0, -1]
grid = [[' ' for _ in range(W)] for _ in range(H)] # A* 用
grid2 = [[' ' for _ in range(W)] for _ in range(H)] # 貪欲最良優先探索　用

S = []
G = []
for i in range(H):
  str = input().rstrip()
  for j, ch in enumerate(str):
    if (ch == 'S'):
      S = [i, j]
    if (ch == 'G'):
      G = [i, j]
    grid[i][j] = ch
    grid2[i][j] = ch

# 距離の2乗を使用しても同じなのでこっちを使用
def calc_dist2(a, b):
  return abs(a[0] - b[0])**2 + abs(a[1] - b[1])**2

def print_grid(grid):
  for line in grid:
    print(''.join(line))


# A*
# [直線距離, y, x, 距離]
pq = PriorityQueue([[calc_dist2(S, G), S[0], S[1], 0]])
archive = False
min_dist = -1
print("実行結果 A*探索")
print()
while (len(pq) > 0 and (not archive)):
  top = pq.pop()
  y = top[1]
  x = top[2]
  grid[y][x] = '*'
  d = top[3]
  print_grid(grid)
  print()
  if (y == G[0] and x == G[1]):
    min_dist = d
    archive = True

  for i in range(4):
    yy = y + dy[i]
    xx = x + dx[i]
    if (0 <= yy and yy <= H and 0 <= x and x <= W):
      if (grid[yy][xx] == ' ' or grid[yy][xx] == 'G'):
        pq.push([calc_dist2([yy, xx], G), yy, xx, d + 1])

print("A*探索での最短距離: {0}".format(min_dist))
print()
print("===================")
print()

# 貪欲最良優先探索
# [距離, 直線距離, y, x] 距離を最優先にして直線距離をヒューリスティックスとすることで
# 貪欲最良優先探索となる
print("実行結果 貪欲最良優先探索")
print()
pq = PriorityQueue([[0, calc_dist2(S, G), S[0], S[1]]])
archive = False
min_dist = -1
while (len(pq) > 0 and (not archive)):
  top = pq.pop()
  y = top[2]
  x = top[3]
  grid2[y][x] = '*'
  d = top[0]
  print_grid(grid2)
  print()
  if (y == G[0] and x == G[1]):
    min_dist = d
    archive = True

  for i in range(4):
    yy = y + dy[i]
    xx = x + dx[i]
    if (0 <= yy and yy <= H and 0 <= x and x <= W):
      if (grid2[yy][xx] == ' ' or grid2[yy][xx] == 'G'):
        pq.push([d + 1, calc_dist2([yy, xx], G), yy, xx])

print("貪欲最良優先探索での最短距離: {0}".format(min_dist))
