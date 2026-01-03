import math

def main():
  with open('./2025/day6/2025-day6-input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
  symbols = [[x for x in line.split(' ') if x != ''] for line in lines]
  problems = [(problem[-1], [int(x) for x in problem[:-1]]) for problem in zip(*symbols)]
  print(sum([math.prod(problem[1]) if problem[0] == "*" else sum(problem[1]) for problem in problems]))

if __name__ == "__main__":
  main()