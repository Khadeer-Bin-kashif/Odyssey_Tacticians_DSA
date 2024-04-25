import matplotlib.pyplot as plt
import time
import random


def dist_matrix_creator(graph):
  cities = list(graph.keys())
  num_cities = len(cities)
  dist_matrix = [[None for _ in range(num_cities)] for _ in range(num_cities)]
  index_dict = {}

  for i, city in enumerate(cities):
    for j, neighbor_city in enumerate(cities):
      if city == neighbor_city:
        dist_matrix[i][j] = 0
      else:
        for destination, distance in graph[city]:
          if destination == neighbor_city:
            dist_matrix[i][j] = distance
            break

  for i in range(num_cities):
    index_dict[i] = cities[i]

  return dist_matrix, index_dict

# Function to generate a greedy cycle based on the provided distance matrix
def greedy_cycle_generator(dist_matrix):
  optimal_route = [0]  # Starting city is always at the start of the route
  total_distance = 0
  city_index = 0

  for i in range(len(dist_matrix)):
    for j in range(len(dist_matrix[i])):
      if dist_matrix[i][j] == 0:
        dist_matrix[i][j] = float("inf")

  while len(optimal_route) != len(dist_matrix):
    min_dist = float("inf")
    for j in range(len(dist_matrix[city_index])):
      if dist_matrix[city_index][j] != float("inf") and j not in optimal_route:
        if dist_matrix[city_index][j] < min_dist:
          min_dist = dist_matrix[city_index][j]
          city_index = j

    if min_dist == float("inf"):
      break
    optimal_route.append(city_index)
    total_distance += min_dist
  optimal_route.append(0)

  return optimal_route


def held_karp_route(dist_matrix):
    n = len(dist_matrix)
    cities = []
    memo = {}  # Memoization to store results of previously solved subproblems
    for i in range(0, n):
        cities.append(i) # List of all cities

    optimal_route = optimal_cycle_finder(1, 0, cities, memo, dist_matrix)   #initially, marker will only contain city 0 marked as 1, ie 0000....1
    return  optimal_route  


def optimal_cycle_finder(marker, last, cities, memo, dist_matrix):
    optimal_route = []
    min_cost = float('inf')

    # Base case: Return to the starting city
    if marker == (1 << len(cities)) - 1:   
        return [last, 0]   #this creates a cycle by adding start city to route again at the end

    if (marker, last) in memo:   #memo is a dict where tuples are keys and previously calculated optimal routes are keys
        return memo[(marker, last)]  #immediately reuse previously computed route if already contained in memo

    for city in cities:   #city is an integer from 0 to n - 1, cities is a list of integers
        if marker & (1 << city) == 0:  #bitwise AND operation to prevent revisits
            partial_route = optimal_cycle_finder(marker | (1 << city), city, cities, memo, dist_matrix)  #bitwise OR operation marks city as 1 in marker
            cost = dist_matrix[0][last] + dist_matrix[last][city] + dist_matrix[city][0]  #distance for a sub-cycle
            if cost < min_cost:  #compare the cost of newly found sub-cycle to older minimum sub-cycle cost
                min_cost = cost
                optimal_route = [last] + partial_route   #partial optimal routes are appended to the main optimal_route.

    if optimal_route != None:
        memo[(marker, last)] = optimal_route
    else:
        memo[(marker, last)] = [last, 0] 

    return memo[(marker, last)]  #retrieve past optimal_route data


# Function to measure the time complexity of the greedy algorithm
def measure_time_complexity_greedy(graph):
  dist_matrix, _ = dist_matrix_creator(graph.copy())
  start_time = time.time()
  greedy_cycle_generator(dist_matrix.copy())
  end_time = time.time()
  return end_time - start_time

def measure_time_complexity_held_karp(graph):
  dist_matrix, _ = dist_matrix_creator(graph.copy())
  start_time = time.time()
  held_karp_route(dist_matrix.copy())
  end_time = time.time()
  return end_time - start_time


graph = {
    'Karachi':[('Lahore', 1211), ('Faisalabad', 1115), ('Gwadar', 622), ('Multan', 884), ('Hyederabad', 163), ('Quetta', 590), ('Islamabad', 1412), ('Peshawar', 1554), ('Gujranwala', 1268), ('Rawalpindi', 1396), ('Sialkot', 1312), ('Sukkur', 470), ('Bahawalpur', 676), ('Gujrat', 1090), ('Chaman', 806), ('Nawabshah', 267), ('Larkana', 455), ('Sargodha', 1221), ('Abbottabad', 1501), ('Sahiwal', 1054)],
    'Lahore':[('Karachi', 1211), ('Faisalabad', 192), ('Gwadar', 1839), ('Multan', 348), ('Hyederabad', 1079), ('Quetta', 984), ('Islamabad', 389), ('Peshawar', 531), ('Gujranwala', 73), ('Rawalpindi', 398), ('Sialkot', 132), ('Sukkur', 768), ('Bahawalpur', 426), ('Gujrat', 168), ('Chaman', 1042), ('Nawabshah', 944), ('Larkana', 847), ('Sargodha', 198), ('Abbottabad', 479), ('Sahiwal', 170)],
    'Faisalabad':[('Karachi', 1115), ('Lahore', 192), ('Gwadar', 1735), ('Multan', 244), ('Hyederabad', 975), ('Quetta', 879), ('Islamabad', 320), ('Peshawar', 462), ('Gujranwala', 186), ('Rawalpindi', 304), ('Sialkot', 260), ('Sukkur', 664), ('Bahawalpur', 322), ('Gujrat', 231), ('Chaman', 937), ('Nawabshah', 839), ('Larkana', 742), ('Sargodha', 129), ('Abbottabad', 410), ('Sahiwal', 102)],
    'Gwadar':[('Karachi', 622), ('Lahore', 1839), ('Faisalabad', 1735), ('Multan', 1501), ('Hyederabad', 780), ('Quetta', 919), ('Islamabad', 2028), ('Peshawar', 2171), ('Gujranwala', 1884), ('Rawalpindi', 2012), ('Sialkot', 1929), ('Sukkur', 1091), ('Bahawalpur', 1452), ('Gujrat', 1905), ('Chaman', 1040), ('Nawabshah', 883), ('Larkana', 1059), ('Sargodha', 1838), ('Abbottabad', 2118), ('Sahiwal', 1671)],
    'Multan':[('Karachi', 884), ('Lahore', 348), ('Gwadar', 1501), ('Faisalabad', 244), ('Hyederabad', 744), ('Quetta', 633), ('Islamabad', 539), ('Peshawar', 681), ('Gujranwala', 395), ('Rawalpindi', 522), ('Sialkot', 439), ('Sukkur', 433), ('Bahawalpur', 100), ('Gujrat', 440), ('Chaman', 690), ('Nawabshah', 609), ('Larkana', 512), ('Sargodha', 348), ('Abbottabad', 628), ('Sahiwal', 181)],
    'Hyederabad':[('Karachi', 163), ('Lahore', 1079), ('Gwadar', 780), ('Multan', 744), ('Faisalabad', 975), ('Quetta', 707), ('Islamabad', 1246), ('Peshawar', 1388), ('Gujranwala', 1102), ('Rawalpindi', 1230), ('Sialkot', 1146), ('Sukkur', 333), ('Bahawalpur', 670), ('Gujrat', 1122), ('Chaman', 832), ('Nawabshah', 112), ('Larkana', 315), ('Sargodha', 1055), ('Abbottabad', 1336), ('Sahiwal', 888)],
    'Quetta':[('Karachi', 590), ('Lahore', 984), ('Gwadar', 919), ('Multan', 633), ('Hyederabad', 707), ('Faisalabad', 879), ('Islamabad', 893), ('Peshawar', 840), ('Gujranwala', 1030), ('Rawalpindi', 910), ('Sialkot', 1074), ('Sukkur', 386), ('Bahawalpur', 767), ('Gujrat', 1064), ('Chaman', 125), ('Nawabshah', 581), ('Larkana', 395), ('Sargodha', 766), ('Abbottabad', 971), ('Sahiwal', 816)],
    'Islamabad':[('Karachi', 1412), ('Lahore', 389), ('Gwadar', 2028), ('Multan', 539), ('Hyederabad', 1246), ('Quetta', 893), ('Faisalabad', 320), ('Peshawar', 186), ('Gujranwala', 219), ('Rawalpindi', 22), ('Sialkot', 229), ('Sukkur', 956), ('Bahawalpur', 614), ('Gujrat',176), ('Chaman', 949), ('Nawabshah', 1132), ('Larkana', 1035), ('Sargodha', 231), ('Abbottabad', 103), ('Sahiwal', 415)],
    'Peshawar':[('Karachi', 1554), ('Lahore', 531), ('Gwadar', 2171), ('Multan', 681), ('Hyederabad', 1388), ('Quetta', 840), ('Islamabad', 186), ('Faisalabad', 462), ('Gujranwala', 402), ('Rawalpindi', 187), ('Sialkot', 411), ('Sukkur', 1102), ('Bahawalpur', 760), ('Gujrat', 359), ('Chaman', 898), ('Nawabshah', 1278), ('Larkana', 1181), ('Sargodha', 377), ('Abbottabad', 199), ('Sahiwal', 561)],
    'Gujranwala':[('Karachi', 1268), ('Lahore', 73), ('Gwadar', 1884), ('Multan', 395), ('Hyederabad', 1102), ('Quetta', 1030), ('Islamabad', 219), ('Peshawar', 402), ('Faisalabad', 186), ('Rawalpindi', 212), ('Sialkot', 51), ('Sukkur', 815), ('Bahawalpur', 473), ('Gujrat', 48), ('Chaman', 1088), ('Nawabshah', 991), ('Larkana', 893), ('Sargodha', 190), ('Abbottabad', 341), ('Sahiwal', 262)],
    'Rawalpindi':[('Karachi', 1396), ('Lahore', 398), ('Gwadar', 2012), ('Multan', 522), ('Hyederabad', 1230), ('Quetta',910 ), ('Islamabad', 22), ('Peshawar', 187), ('Gujranwala', 212), ('Faisalabad', 304), ('Sialkot', 221), ('Sukkur', 944), ('Bahawalpur', 602), ('Gujrat', 168), ('Chaman', 950), ('Nawabshah', 1120), ('Larkana', 1023), ('Sargodha', 220), ('Abbottabad', 106), ('Sahiwal',403)],
    'Sialkot':[('Karachi', 1312), ('Lahore', 132), ('Gwadar', 1929), ('Multan', 439), ('Hyederabad', 1146), ('Quetta', 1074), ('Islamabad', 229), ('Peshawar', 411), ('Gujranwala', 51), ('Rawalpindi', 221), ('Faisalabad', 260), ('Sukkur', 858), ('Bahawalpur', 516), ('Gujrat', 58), ('Chaman', 1131), ('Nawabshah', 1034), ('Larkana', 937), ('Sargodha', 264), ('Abbottabad', 351), ('Sahiwal', 305)],
    'Sukkur':[('Karachi', 470), ('Lahore', 768), ('Gwadar', 1091), ('Multan', 433), ('Hyederabad', 333), ('Quetta', 386), ('Islamabad', 956), ('Peshawar', 1102), ('Gujranwala', 815), ('Rawalpindi', 944), ('Sialkot', 858), ('Faisalabad', 664), ('Bahawalpur', 382), ('Gujrat', 835), ('Chaman', 511), ('Nawabshah', 197), ('Larkana', 82), ('Sargodha', 768), ('Abbottabad', 1048), ('Sahiwal', 601)],
    'Bahawalpur':[('Karachi', 676), ('Lahore', 426), ('Gwadar', 1452), ('Multan', 100), ('Hyederabad', 670), ('Quetta', 767), ('Islamabad', 614), ('Peshawar', 760), ('Gujranwala', 473), ('Rawalpindi', 602), ('Sialkot', 516), ('Sukkur', 382), ('Faisalabad', 322), ('Gujrat', 519), ('Chaman', 776), ('Nawabshah', 556), ('Larkana', 459), ('Sargodha', 427), ('Abbottabad', 707), ('Sahiwal', 244)],
    'Gujrat':[('Karachi', 1090), ('Lahore', 168), ('Gwadar', 1905), ('Multan', 440), ('Hyederabad', 1122), ('Quetta', 1064), ('Islamabad', 176), ('Peshawar', 359), ('Gujranwala', 48), ('Rawalpindi', 168), ('Sialkot', 58), ('Sukkur', 835), ('Bahawalpur', 519), ('Faisalabad', 231), ('Chaman', 1116), ('Nawabshah', 1010), ('Larkana', 913), ('Sargodha', 160), ('Abbottabad', 300), ('Sahiwal', 307)],
    'Chaman':[('Karachi', 806), ('Lahore', 1042), ('Gwadar', 1040), ('Multan', 690), ('Hyederabad', 832), ('Quetta', 125), ('Islamabad', 949), ('Peshawar', 898), ('Gujranwala', 1088), ('Rawalpindi', 950), ('Sialkot', 1131), ('Sukkur', 511), ('Bahawalpur', 776), ('Gujrat', 1116), ('Faisalabad',937), ('Nawabshah', 706), ('Larkana', 520), ('Sargodha', 824), ('Abbottabad', 1029), ('Sahiwal', 875)],
    'Nawabshah':[('Karachi', 267), ('Lahore', 944), ('Gwadar', 883), ('Multan', 609), ('Hyederabad', 112), ('Quetta', 581), ('Islamabad', 1132), ('Peshawar', 1278), ('Gujranwala', 991), ('Rawalpindi', 1120), ('Sialkot', 1034), ('Sukkur', 197), ('Bahawalpur', 556), ('Gujrat', 1010), ('Chaman', 706), ('Faisalabad', 839), ('Larkana', 206), ('Sargodha', 944), ('Abbottabad', 1225), ('Sahiwal', 777)],
    'Larkana':[('Karachi', 455), ('Lahore', 847), ('Gwadar', 1059), ('Multan', 512), ('Hyederabad', 315), ('Quetta', 395), ('Islamabad', 1035), ('Peshawar', 1181), ('Gujranwala', 893), ('Rawalpindi', 1023), ('Sialkot', 937), ('Sukkur', 82), ('Bahawalpur', 459), ('Gujrat', 913), ('Chaman', 520), ('Nawabshah', 206), ('Faisalabad', 742), ('Sargodha', 846), ('Abbottabad', 1127), ('Sahiwal', 680)],
    'Sargodha':[('Karachi', 1221), ('Lahore', 198), ('Gwadar', 1838), ('Multan', 348), ('Hyederabad', 1055), ('Quetta', 766), ('Islamabad', 231), ('Peshawar', 377), ('Gujranwala', 190), ('Rawalpindi', 220), ('Sialkot', 264), ('Sukkur', 768), ('Bahawalpur', 427), ('Gujrat', 160), ('Chaman', 824), ('Nawabshah', 944), ('Larkana', 846), ('Faisalabad', 129), ('Abbottabad', 331), ('Sahiwal', 229)],
    'Abbottabad':[('Karachi', 1501), ('Lahore', 479), ('Gwadar', 2118), ('Multan', 628), ('Hyederabad', 1336), ('Quetta', 971), ('Islamabad', 103), ('Peshawar', 199), ('Gujranwala', 341), ('Rawalpindi', 106), ('Sialkot', 351), ('Sukkur', 1048), ('Bahawalpur', 707), ('Gujrat',300 ), ('Chaman', 1029), ('Nawabshah', 1225), ('Larkana', 1127), ('Sargodha', 331), ('Faisalabad', 410), ('Sahiwal', 509)],
    'Sahiwal':[('Karachi', 1054), ('Lahore', 170), ('Gwadar', 1671), ('Multan', 181), ('Hyederabad', 888), ('Quetta', 816), ('Islamabad', 415), ('Peshawar', 561), ('Gujranwala', 262), ('Rawalpindi', 403), ('Sialkot', 305), ('Sukkur', 601), ('Bahawalpur', 244), ('Gujrat', 307), ('Chaman', 875), ('Nawabshah', 777), ('Larkana', 680), ('Sargodha', 229), ('Abbottabad', 509), ('Faisalabad', 102)]
        }


# Input sizes for varying lengths
input_sizes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]  

# Generate time complexities for each input size
time_complexities_greedy = []
time_complexities_held_karp = []
for size in input_sizes:
  subgraph = {city: graph[city] for city in random.sample(list(graph.keys()), k=size)}

  time_complexity_greedy = measure_time_complexity_greedy(subgraph)
  time_complexities_greedy.append(time_complexity_greedy*10000)
  time_complexity_held = measure_time_complexity_held_karp(subgraph)
  time_complexities_held_karp.append(time_complexity_held)


plt.plot(input_sizes, time_complexities_greedy, label='Greedy', marker='o')
plt.plot(input_sizes, time_complexities_held_karp, label='Held-Karp', marker='s')  
plt.xlabel("Number of Cities")
plt.ylabel("Execution Time (seconds)")
plt.title("Time Complexities of Traveling Salesman Problem Solvers")
plt.legend()  
plt.grid(True)
plt.show()
