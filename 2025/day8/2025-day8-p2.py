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

  connections_made = 0
  dsu = [i for i in range(len(boxes))]
  for dist in dists:
    box1_rep = find_rep(dsu, dist[0])
    box2_rep = find_rep(dsu, dist[1])
    if box1_rep != box2_rep:
      dsu[box1_rep] = box2_rep
      connections_made += 1
      if connections_made == len(boxes) - 1:
        print(boxes[dist[0]][0] * boxes[dist[1]][0])
        break
    
if __name__ == "__main__":
  main()