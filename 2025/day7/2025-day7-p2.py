def main():
  with open('./2025/day7/2025-day7-input.txt') as f:
    grid = [[x for x in line.strip()] for line in f.readlines()]

  prev_row = [1 if cell == 'S' else 0 for cell in grid[0]]
  for i in range(1, len(grid)):
    new_row = [0 for _ in range(len(grid[i]))]
    for j in range(len(grid[i])):
      if grid[i][j] == '.':
        new_row[j] += prev_row[j]
      elif grid[i][j] == '^':
        new_row[j - 1] += prev_row[j]
        new_row[j + 1] += prev_row[j]
    prev_row = new_row
  print(sum(prev_row))

if __name__ == "__main__":
  main()