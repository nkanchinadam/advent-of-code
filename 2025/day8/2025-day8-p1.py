import math

def dist_squared(a, b):
  return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2

def find_rep(dsu, i):
  if dsu[i] == i:
    return i
  dsu[i] = find_rep(dsu, dsu[i])
  return dsu[i]

def main():
  with open('./2025/day8/2025-day8-input.txt') as f:
    boxes = [[int(x) for x in line.strip().split(',')] for line in f.readlines()]

  dists = []
  for i in range(len(boxes) - 1):
    for j in range(i + 1, len(boxes)):
      dists.append((i, j, dist_squared(boxes[i], boxes[j])))
  dists.sort(key=lambda x: x[2])

  dsu = [i for i in range(len(boxes))]
  for i in range(min(1000, len(dists))):
    box1_rep = find_rep(dsu, dists[i][0])
    box2_rep = find_rep(dsu, dists[i][1])
    if box1_rep != box2_rep:
      dsu[box1_rep] = box2_rep

  reps = [find_rep(dsu, i) for i in dsu]
  counts = {}
  for rep in reps:
    if rep not in counts:
      counts[rep] = 0
    counts[rep] += 1
  three_largest_circuits = sorted([(rep, counts[rep]) for rep in counts.keys()], key=lambda x : x[1])[-3:]
  print(math.prod([circuit[1] for circuit in three_largest_circuits]))
    
if __name__ == "__main__":
  main()