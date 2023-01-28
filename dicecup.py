# Get the number of faces for the two dice
num_faces_1, num_faces_2 = map(int, input().split())

# Create a list of possible outcomes by rolling two dice
outcomes = []
for i in range(1, num_faces_1+1):
    for j in range(1, num_faces_2+1):
        outcomes.append(i+j)

# Count the frequency of each outcome
counts = {}
for outcome in outcomes:
    if outcome in counts:
        counts[outcome] += 1
    else:
        counts[outcome] = 1

# Identify the outcomes with the highest frequency
most_likely_outcomes = []
max_count = max(counts.values())
for outcome, count in counts.items():
    if count == max_count:
        most_likely_outcomes.append(outcome)

# Sort and print the most likely outcomes
most_likely_outcomes.sort()
for outcome in most_likely_outcomes:
    print(outcome)
