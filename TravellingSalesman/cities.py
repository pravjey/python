import math
import random

def clean_data(element):
    """
    Clean each element(record) in "cities.txt" by:
    (a) removing tabs
    (b) identify end of last field
    (c) convert the second and third fields (latitude and longitude) to floating point numbers
    (d) convert state, city, latitude and longitude fields into a four-tuple
    """ 
    element = element.split('\t')
    element[3] = element[3][0:(len(element[3])-1)]
    element[2] = float(element[2])
    element[3] = float(element[3])
    element = tuple(element)
    return element
            
def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples:
    [(state, city, latitude, longitude), ...] 
    """
    stream = open(file_name)
    data = stream.readlines()
    stream.close()
    roadmap = []
    for city_info in data: # For each record in data file
        if city_info != "\n": # Ignore new line characters
            city_info = clean_data(city_info) # Clean the record
            roadmap.append(city_info) # Add each cleaned record to a list
    return roadmap
  
def print_cities(road_map):
    # For each city record in the road map tuple:
    # Print the city, latitude and longitude fields in three columns of 15 characters
    # with the the latitude and longitude rounded to two decimal places
    for city_info in road_map:
        print('{0:15} {1:15} {2:15}'.format(city_info[1], round(city_info[2],2), round(city_info[3],2)))
    print('\n')

def euler_dist(x1,x2,y1,y2):
    # Calculate the distance between (x1,y1) and (x2,y2)
    return math.sqrt(((x1-x2)**2)+((y1-y2)**2))

def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the`road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    distance = 0 # Assume starting distance is zero
    i = 0 # Assume starting city is first city
    while i < len(road_map):
        a = i # Current city record
        b = (i+1) % len(road_map) # Next city record
        # Add the distance between current and next city to total distance travelled
        distance = distance + euler_dist(road_map[a][2],road_map[b][2],road_map[a][3],road_map[b][3]) 
        i = i + 1 # Move to next city record
    return distance

def swap(city1, city2):
    temp = city1
    city1 = city2
    city2 = temp
    return city1, city2

def swap_adjacent_cities(road_map, index):
    """
    Take the city at location `index` in the `road_map`, and the city at 
    location `index+1` (or at `0`, if `index` refers to the last element 
    in the list), swap their positions in the `road_map`, compute the 
    new total distance, and return the tuple 

        (new_road_map, new_total_distance)
    """
    # Index of next city record
    next_index = (index + 1) % len(road_map)
    # Swap cities adjacent in list
    road_map[index], road_map[next_index] = swap(road_map[index], road_map[next_index])
    # Calculate the new total distance after swapping adjacent cities
    new_total_distance = compute_total_distance(road_map)
    # Store new road map and new total distance in a tuple
    return (road_map,new_total_distance)

def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    # index1 and index2 are not the same, then the records at those indices are
    # swapped. If they are the same, no swap needs to take place, so nothing happens
    if index1 != index2:
        road_map[index1], road_map[index2] = swap(road_map[index1], road_map[index2])
    else:
        pass
    # Calculate the new total distance after swapping adjacent cities
    new_total_distance = compute_total_distance(road_map)
    # Store new road map and new total distance in a tuple
    return (road_map,new_total_distance)

def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `swap_adjacent_cities`, 
    try `10000` swaps, and each time keep the best cycle found so far. 
    After `10000` swaps, return the best cycle found so far.
    """
    #Assume the best_cycle is the initial road map and calculate total distance 
    best_cycle = road_map
    best_cycle_dist = compute_total_distance(road_map)
    best_attempts = [best_cycle_dist]
    # For each city in the road map
    for i in range(len(road_map)):
        for swaps in range(10000):
            #A random number between 0 and total number of cities is generated.
            number = int(len(road_map) * random.random())
            # Create a test tuple where the first field in the tuple is the road map,
            # with two cities swapped, and second field is total distance.
            # The type of swap depends on whether the random number is odd or even.
            # If even or if i is equal to number, the cities at index i and i+1 is swapped.
            # If odd and i is not equal to number, the cities at index i and number are swapped.
            # As a result, on each swap, there is
            # 50% chance of either type of swap being selected.
            if number % 2 == 1 and i != number:
                test = swap_cities(best_cycle,i,number)
            else:
                test = swap_adjacent_cities(best_cycle,i)
            # Compare the second field with current best cycle distance
            # If current best cycle distance is greater, then set best cycle
            # to the road map after swapping 
            if best_cycle_dist > test[1]:
                best_cycle = test[0]
                best_cycle_dist = test[1]
        if best_attempts[len(best_attempts)-1] > best_cycle_dist:
            best_attempts.append(best_cycle_dist)
    return best_cycle, best_cycle_dist, best_attempts
        
def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """
    # For each city index in the road map
    for i in range(len(road_map)):
        # Identify the index of the current city and next city
        a = i
        b = (i+1) % len(road_map)
        # Calculate distance between the current city and next city
        distance = euler_dist(road_map[a][2],road_map[b][2],road_map[a][3],road_map[b][3])
        print('{0:15} {1:3} {2:15} {3:15}'.format(road_map[a][1],'->',road_map[b][1],round(distance,2)))

def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    try_again = 'y'
    road_map = read_cities("city-data.txt")
    while try_again in {'y', 'Y', 'yes', 'Yes'}:
        print("City data")
        print("=========")
        print_cities(road_map)
        print('\n')
        print('Searching for best solution...')
        print('\n')
        best_cycle, best_cycle_dist, best_attempts = find_best_cycle(road_map)
        print("Total distance for best attempts")
        print("================================")
        print(best_attempts)
        print('\n')
        print("Best cycle")
        print("==========")
        print_map(best_cycle)
        print("Total distance = ",round(best_cycle_dist,2))
        print('\n')
        road_map = best_cycle
        try_again = input("Do you want to try again using best cycle so far?")


if __name__ == "__main__":
    main()
