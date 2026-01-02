def main():
  with open('./2025/day3/2025-day3-input.txt') as f:
    lines = f.readlines()
  banks = [[int(x) for x in line.strip()] for line in lines]
  
  sum = 0
  for bank in banks:
    max_digit = max(bank[:len(bank) - 1])
    max_digit_index = bank.index(max_digit)
    second_digit = max(bank[max_digit_index + 1:])
    sum += max_digit * 10 + second_digit
  print(sum)

if __name__ == "__main__":
  main()