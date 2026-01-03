def main():
  with open('./2025/day7/2025-day7-input.txt') as f:
    grid = [[x for x in line.strip()] for line in f.readlines()]

  num_split = 0
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == 'S':
        grid[i][j] = '|'
      elif i != 0 and grid[i - 1][j] == '|':
        if grid[i][j] == '.':
          grid[i][j] = '|'
        elif grid[i][j] == '^':
          grid[i][j - 1] = grid[i][j + 1] = '|'
          num_split += 1
  print(num_split)

if __name__ == "__main__":
  main()