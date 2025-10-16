import random

V = 4

def calculate_cost(graph, tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += graph[tour[i]][tour[i+1]]
    return cost

def get_neighbors(tour):
    neighbors = []
    for i in range(1, len(tour) - 1):
        for j in range(i+1, len(tour) - 1):
            neighbor = tour[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def hill_climbing_tsp(graph, start):
    current_tour = [start] + random.sample(range(1, V), V-1) + [start]
    current_cost = calculate_cost(graph, current_tour)
    improving = True
    while improving:
        improving = False
        neighbors = get_neighbors(current_tour)
        for neighbor in neighbors:
            neighbor_cost = calculate_cost(graph, neighbor)
            if neighbor_cost < current_cost:
                current_tour = neighbor
                current_cost = neighbor_cost
                improving = True
                break
    return current_cost, current_tour

if __name__ == "__main__":
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    start_city = 0
    min_cost, best_tour = hill_climbing_tsp(graph, start_city)
    print(f"Best tour: {best_tour}")
    print(f"Minimum cost (approximate): {min_cost}")
