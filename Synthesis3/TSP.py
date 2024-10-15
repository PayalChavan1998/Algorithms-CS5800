# Payal Chavan
# Summer 2024 
# Algorithms CS 5800
# Synthesis3 - P and NP: Traveling Salesman Problem (TSP)
# Date: 08/09/2024




from itertools import permutations
from typing import List, Tuple

def tsp_solver(cities: List[str], distance_matrix: List[List[int]]):
    n = len(cities)
    min_route = []
    min_distance = float('inf')
    
    # Generate all permutations of cities (excluding the starting city)
    for perm in permutations(range(1, n)):
        current_distance = 0
        # Create a route with {Start City + remaining cities permutation + Start City}
        current_route = [0] + list(perm) + [0]
        
        # Calculate the total distance for the current permutation
        for i in range(n):
            current_distance += distance_matrix[current_route[i]][current_route[i + 1]]

        # Update the minimum distance and route if the current one is shorter
        if current_distance < min_distance:
            min_distance = current_distance
            min_route = current_route

    # Convert the route indices back to city names
    min_route_cities = [cities[i] for i in min_route]

    return min_route_cities, min_distance

# Execute the main function to test the code.
if __name__ == '__main__':
    cities = ["A", "B", "C", "D"]
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    route, total_distance = tsp_solver(cities, distance_matrix)
    print("Shortest route:", route)  # Example output: ["A", "B", "D", "C", "A"]
    print("Total distance:", total_distance)  # Example output: 80





'''
Output:
Shortest route: ['A', 'B', 'D', 'C', 'A']
Total distance: 80
'''