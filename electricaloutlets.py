# Get the number of test cases
num_tests = int(input())

# Iterate through each test case
for i in range(num_tests):
    # Get the number of power strips and the number of outlets in each strip
    power_strips = list(map(int, input().split()))
    num_power_strips = power_strips[0]
    outlets = power_strips[1:]

    # Calculate the number of appliances that can be powered
    total_outlets = 1 # Starting with the one wall outlet
    for outlet in outlets:
        total_outlets += outlet - 1
    
    # Print the result
    print(total_outlets)
