from cities import *

def test_clean_data(element):
    try:
        a = clean_data(element)
        assert type(a[3]) == type(a[2]) == "float" and type(a) == "tuple"
    except AssertionError:
        return "Data not cleaned successfully"
    else:
        return "Data cleaned successfully"

def test_euler_dist(x1,x2,y1,y2):
    try:
        answer = euler_dist(x1,x2,y1,y2)
        test = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
        assert answer == test
    except AssertionError:
        return "Calculation unsuccessful"
    else:
        return "Calculation successful"

def test_compute_total_distance(road_map):
    try:
        answer = compute_total_dista = nce(road_map)
        assert type(answer) == "float"
    except AssertionError:
        return "Calculation unsuccessful"
    else:
        return "Calculation successful"

def test_swap(city1, city2):
    try:
        a,b = swap(city1, city2):
        assert a == city2 and b == city2
    except AssertionError:
        return "Variable swap unsuccessful"
    else:
        return "Variable swap successful"

def test_swap_adjacent_cities(road_map, index):
    try:
        a = swap_adjacent_cities(road_map, index)
        assert a[0][index] == road_map[index+1]
    except AssertionError:
        return "Adjacent cities swap unsuccessful"
    else:
        return "Adjacent cities swap successful"

def test_swap_cities(road_map, index1, index2):
    try:
        a = swap_cities(road_map, index1,index2)
        assert a[0][index1] == road_map[index2] and a[0][index2] == road_map[index1]
    except AssertionError:
        return "City swap unsuccessful"
    else:
        return "City swap successful"

def test_find_best_cycle(road_map):
    try:
        a,b,c = find__best_cycle(road_map)
        assert b == c[len(c)]
        except AssertionError:
            return "Best cycle found after 10,000 swaps"
        else:
            return "Best cycle not found after 10,000 swaps"

def main():
    pass
 
if __name__ == "__main__":
    main()
