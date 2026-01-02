def is_accessible(grid, x, y):
  dirs = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1]
  ]

  num_adjacent = 0
  for dir in dirs:
    if x + dir[0] >= 0 and x + dir[0] < len(grid) and y + dir[1] >= 0 and y + dir[1] < len(grid[0]) and grid[x + dir[0]][y + dir[1]] == '@':
      num_adjacent += 1
      if num_adjacent == 4:
        return False
  return True

def remove_accessible_rolls(grid):
  num_accessible = 0
  new_grid = [['.' for _ in range(len(grid[0]))] for _ in range(len(grid))]
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      if grid[r][c] == '@':
        if is_accessible(grid, r, c):
          num_accessible += 1
        else:
          new_grid[r][c] = '@'
  return num_accessible, new_grid

def main():
  with open('./2025/day4/2025-day4-input.txt') as f:
    input = f.readlines()
  grid = [[ch for ch in row.strip()] for row in input]
  num_accessible = 0
  while True:
    num_accessible_iter, new_grid = remove_accessible_rolls(grid)
    if num_accessible_iter == 0:
      break
    grid = new_grid
    num_accessible += num_accessible_iter
  print(num_accessible)

if __name__ == "__main__":
  main()