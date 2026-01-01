def main():
  with open('./2025/day2/2025-day2-input.txt') as f:
    input = f.readlines()
  ranges = [[int(x) for x in id_range.split('-')] for id_range in input[0].strip().split(',')]
  
  sum = 0
  for id_range in ranges:
    curr_id = id_range[0]
    while curr_id <= id_range[1]:
      num_digits = len(str(curr_id))
      if num_digits % 2 == 1:
        curr_id = int('1' + ''.join(['0' for _ in range(num_digits)]))
        continue
      if str(curr_id)[:num_digits // 2] == str(curr_id)[num_digits // 2:]:
        sum += curr_id
      curr_id += 1
  print(sum)

if __name__ == "__main__":
  main()