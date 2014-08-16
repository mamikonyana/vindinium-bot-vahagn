from game import AIR


def find_path(start, destination, board):
    explored = set()
    current_paths = [[start]]
    while current_paths:
        new_paths = []
        for path in current_paths:
            point = path[-1]
            neightbors = get_neightbors(point)
            for new_point in neightbors:
                if new_point in explored:
                    continue 
                explored.add(new_point)
                if new_point == destination:
                    return path + [new_point]
                if can_occupy(new_point, board):
                    new_paths.append(path + [new_point])
        current_paths = new_paths
    return []


def navigate(start, destination, board):
    path = find_path(start, destination, board)
    direction = get_direction(path[0], path[1])
    return direction


def get_direction(start, destination):
    dx = destination[0] - start[0]
    dy = destination[1] - start[1]
    if abs(dx) > abs(dy):
        if dx > 0:
            return 'South'
        if dx < 0:
            return 'North'
    else:
        if dy > 0:
            return 'East'
        if dy < 0:
            return 'West'
    return 'Stay'

def get_neightbors(point):
  return [(point[0], point[1] + 1),
          (point[0], point[1] - 1),
          (point[0] + 1, point[1]),
          (point[0] - 1, point[1])]


def can_occupy(point, board):
  if 0 > point[0] or board.size <= point[0]:
    return False
  if 0 > point[1] or board.size <= point[1]:
    return False
  tile = board.tiles[point[0]][point[1]]
  return tile == AIR
  
