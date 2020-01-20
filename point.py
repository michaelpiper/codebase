from collections import deque
class Point:
  def __init__(self, x, y, distance):
    self.x = x
    self.y = y
    self.distance = distance

  def get_neighbors(self):
    return [
      self.get_up(),
      self.get_down(),
      self.get_right(),
      self.get_left()
    ]

  def get_up(self):
    return Point(self.x - 1, self.y, self.distance + 1)

  def get_down(self):
    return Point(self.x + 1, self.y, self.distance + 1)

  def get_right(self):
    return Point(self.x, self.y + 1, self.distance + 1)

  def get_left(self):
    return Point(self.x, self.y - 1, self.distance + 1)

  def is_valid_point(self, matrix):
    return self.is_valid_x(matrix) and self.is_valid_y(matrix)

  def is_valid_x(self, matrix):
    max_x = len(matrix) - 1
    return 0 <= self.x <= max_x

  def is_valid_y(self, matrix):
    max_y = len(matrix[0]) - 1
    return 0 <= self.y <= max_y


def get_path_length(m):
  if len(m) == 0 or len(m[0]) == 0:
    return -1

  matrix = [row[:] for row in m]

  start_point = Point(0, 0, 0)
  q = deque()
  q.append(start_point)
  matrix[start_point.x][start_point.y] = 'D'

  while q:
    point = q.popleft()
    for neighbor in point.get_neighbors():
     
      if neighbor.is_valid_point(matrix):
        
        if matrix[neighbor.x][neighbor.y] == 'X':
          print(neighbor.x,neighbor.y)
          return neighbor.distance
        elif matrix[neighbor.x][neighbor.y] == 'O':
          print(neighbor.x,neighbor.y)
          matrix[neighbor.x][neighbor.y] = 'D'
          q.append(neighbor)
  return -1

if __name__ == '__main__':
    treasure_map = [['O', 'O', 'O', 'O'],
    ['D', 'O', 'D', 'O'],
    ['O', 'O', 'O', 'O'],
    ['X', 'D', 'D', 'O']]
    print(get_path_length(treasure_map))