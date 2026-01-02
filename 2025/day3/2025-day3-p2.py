def main():
  with open('./2025/day3/2025-day3-input.txt') as f:
    lines = f.readlines()
  banks = [[int(x) for x in line.strip()] for line in lines]
  
  sum = 0
  for bank in banks:
    digits = []
    start_idx = 0
    for i in range(12):
      num_to_exclude = 12 - i - 1
      candidates = bank[start_idx : len(bank) - num_to_exclude]
      digits.append(max(candidates))
      max_idx = candidates.index(digits[-1])
      start_idx += max_idx + 1
    for i in range(12):
      sum += digits[i] * 10 ** (12 - i - 1)
  print(sum)

if __name__ == "__main__":
  main()