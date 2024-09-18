import random
import math
import numpy as np
import matplotlib.pyplot as plt

# Sử dụng thuật toán luyện kim để giải quyết bài toán Travelling Saleman Problem

TMax = 1000
TMin = 0.005
Alpha = 0.95
cities = [(0, 0), (1.5, 3), (3, 1), (2, 4), (5, 3), (2, 5), (1, 6), (4, 4), (3, 3), (0, 2), (2, 2)]


def create_initial_route(cities):
    start_city = cities[0]
    remaining_cities = cities[1:]
    random_order = random.sample(remaining_cities, len(remaining_cities))
    return [start_city] + random_order

def calculate_total_distance(route):
    total_distance = 0

    # khoảng cách giữa mỗi cặp thành phố liền kề
    for i in range(len(route) - 1):
        city1 = route[i]
        city2 = route[i + 1]
        # Theo công thức ước lượng khoảng cách Euclidean trên lưới
        distance = math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
        total_distance += distance

    # khoảng cách từ thành phố cuối cùng quay lại thành phố đầu tiên
    first_city = route[0]
    last_city = route[-1]
    return_distance = math.sqrt((last_city[0] - first_city[0]) ** 2 + (last_city[1] - first_city[1]) ** 2)

    # Tổng khoảng cách cho toàn bộ quảng đường
    total_distance += return_distance

    return total_distance

def get_neighbors(route):
    neighbors = []
    for i in range(1, len(route) - 1):
        for j in range(i + 1, len(route)):
            neighbor = route.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors


def simulated_annealing(cities, initial_temp, cooling_rate, T_min):
    current_route = create_initial_route(cities)
    current_distance = calculate_total_distance(current_route)

    best_route = current_route.copy()
    best_distance = current_distance
    temperature = initial_temp

    while temperature > T_min:
        neighbors = get_neighbors(current_route)
        next_route = random.choice(neighbors)
        next_distance = calculate_total_distance(next_route)

        delta_distance = next_distance - current_distance

        if delta_distance < 0 or random.uniform(0, 1) < np.exp(-delta_distance / temperature):
            current_route, current_distance = next_route, next_distance
            print(current_route, f"{current_distance:.4f}")
            if current_distance < best_distance:
                best_route, best_distance = current_route, current_distance

        temperature *= cooling_rate

    return best_route, best_distance


if __name__ == "__main__":
    best_route, best_distance = simulated_annealing(cities, TMax, Alpha, TMin)
    print("\nBest Route:", best_route + [[0, 0]])
    print(f"Best Distance: {best_distance:.4f}")

    plt.figure(figsize=(8, 6))
    plt.title("TSP")
    plt.xlabel("X")
    plt.ylabel("Y")


    for i in range(len(best_route) - 1):
        city1 = best_route[i]
        city2 = best_route[i + 1]
        plt.plot([city1[0], city2[0]], [city1[1], city2[1]], 'r*-', linewidth=1)

    plt.plot([best_route[-1][0], best_route[0][0]], [best_route[-1][1], best_route[0][1]], 'r*-', linewidth=1)

    plt.grid(True)
    plt.show()
