def get_factors(n):
  factors = [1]
  for i in range(2, (n // 2) + 1):
    if n % i == 0:
      factors.append(i)
  return factors

def is_repeat(id, repeat_len):
  repeat = id[:repeat_len]
  for i in range(repeat_len, len(id), repeat_len):
    if id[i:i + repeat_len] != repeat:
      return False
  return True

def main():
  with open('./2025/day2/2025-day2-input.txt') as f:
    input = f.readlines()
  ranges = [[int(x) for x in id_range.split('-')] for id_range in input[0].strip().split(',')]
  
  sum = 0
  for id_range in ranges:
    curr_id = max(10, id_range[0])
    while curr_id <= id_range[1]:
      num_digits = len(str(curr_id))
      factors = get_factors(num_digits)
      for factor in factors:
        if is_repeat(str(curr_id), factor):
          sum += curr_id
          break
      curr_id += 1
  print(sum)

if __name__ == "__main__":
  main()