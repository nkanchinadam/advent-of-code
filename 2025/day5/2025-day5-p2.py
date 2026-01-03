def are_intersecting(range1, range2):
  return [range1[0], max(range1[1], range2[1])] if range1[1] >= range2[0] else None

def main():
  with open('./2025/day5/2025-day5-input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

  blank_index = lines.index('')

  fresh_ranges = [[int(x) for x in line.split('-')] for line in lines[:blank_index]]
  fresh_ranges.sort(key=lambda x: x[0])

  i = 0
  while i < len(fresh_ranges) - 1:
    are_intersecting_res = are_intersecting(fresh_ranges[i], fresh_ranges[i + 1])
    while are_intersecting_res is not None and len(fresh_ranges) > i + 1:
      fresh_ranges[i] = are_intersecting_res
      fresh_ranges.pop(i + 1)
      if len(fresh_ranges) == i + 1:
        break
      are_intersecting_res = are_intersecting(fresh_ranges[i], fresh_ranges[i + 1])
    i += 1
  print(sum([range[1] - range[0] + 1 for range in fresh_ranges]))

if __name__ == "__main__":
  main()