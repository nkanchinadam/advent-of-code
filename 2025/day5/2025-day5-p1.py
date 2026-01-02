def main():
  with open('./2025/day5/2025-day5-input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

  blank_index = lines.index('')

  fresh_ranges = [[int(x) for x in line.split('-')] for line in lines[:blank_index]]
  available_ingredients = [int(line) for line in lines[blank_index + 1:]]

  num_fresh = 0
  for ingredient in available_ingredients:
    for range in fresh_ranges:
      if range[0] <= ingredient <= range[1]:
        num_fresh += 1
        break
  print(num_fresh)

if __name__ == "__main__":
  main()