def main():
  with open('./2025/day1/2025-day1-input.txt') as f:
    lines = f.readlines()

  lines = [(line[0], int(line[1:].strip())) for line in lines]

  curr = 50
  zeroCount = 0
  for line in lines:
    if line[0] == 'L':
      curr = (curr + 100 - line[1]) % 100
    else:
      curr = (curr + line[1]) % 100
    
    if curr == 0:
      zeroCount += 1
  
  print(zeroCount)

if __name__ == "__main__":
  main()