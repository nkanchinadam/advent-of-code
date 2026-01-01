def main():
  with open('./2025/day1/2025-day1-input.txt') as f:
    lines = f.readlines()

  lines = [(line[0], int(line[1:].strip())) for line in lines]

  curr = 50
  zeroCount = 0
  for line in lines:
    zeroCount += line[1] // 100
    if line[1] % 100 == 0: continue
    if line[0] == 'L':
      curr -= line[1] % 100
      if curr <= 0 and abs(curr) != line[1] % 100:
        zeroCount += 1
    else:
      curr += line[1] % 100
      if curr >= 100:
        zeroCount += 1
    curr %= 100
  
  print(zeroCount)

if __name__ == "__main__":
  main()