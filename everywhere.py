t = int(input()) # get the number of test cases
for _ in range(t):
    n = int(input()) # get the number of trips
    cities = set() # create an empty set
    for _ in range(n):
        city = input() # get the name of the city
        cities.add(city) # add the city to the set
    print(len(cities)) # print the length of the set
