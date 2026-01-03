import math

def main():
  with open('./2025/day6/2025-day6-input.txt') as f:
    lines = f.readlines()
  symbols = [[x for x in line] for line in lines]

  operators = [symbol for symbol in symbols[-1] if symbol != ' ']
  operands = [''.join(operand).strip() for operand in zip(*symbols[:-1])]
  problems = [[]]
  for (idx, operand) in enumerate(operands):
    if operand == '':
      if idx == len(operands) - 1:
        break
      problems.append([])
      continue
    problems[-1].append(int(operand))
  print(sum([math.prod(problems[i]) if operators[i] == '*' else sum(problems[i]) for i in range(len(operators))]))
  

if __name__ == "__main__":
  main()