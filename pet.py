points = [0, 0, 0, 0, 0]

for i in range(5):
    grades = list(map(int, input().split()))
    for j in range(4):
        points[i] += grades[j]

winner = points.index(max(points)) + 1
print(winner, max(points))
