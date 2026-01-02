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

def main():
  with open('./2025/day4/2025-day4-input.txt') as f:
    input = f.readlines()
  grid = [[ch for ch in row.strip()] for row in input]
  num_accessible = 0
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      if grid[r][c] == '@' and is_accessible(grid, r, c):
        num_accessible += 1
  print(num_accessible)

if __name__ == "__main__":
  main()