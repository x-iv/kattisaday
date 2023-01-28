n = int(input())
at_bats = list(map(int, input().split()))

total_bases = 0
at_bats_not_walk = 0

for i in at_bats:
    if i != -1:
        total_bases += i
        at_bats_not_walk += 1

slugging_percentage = total_bases / at_bats_not_walk

print(slugging_percentage)
