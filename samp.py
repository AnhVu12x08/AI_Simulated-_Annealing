import random
import math
import matplotlib.pyplot as plt

# Tìm giá trị min của hàm số sử dụng thuật toán Luyện Kim

TMax = 1000
TMin = 0.005
ETh = 0.005
Alpha = 0.9
Initial = [-6, 3]


def Energy(x, y): 
    return x ** 4 + y ** 2

def AcceptanceFunction(Temperature, deltaE):
    if deltaE < 0:
        return True
    else:
        r = random.uniform(0, 1)
        if r < math.exp(-deltaE / Temperature):
            return True
        else:
            return False

def SimulatedAnnealing(T_max, T_min, E_th, Alpha, Initial):
    T = T_max
    x = Initial[:]
    E = Energy(x[0], x[1])

    points = [x]

    while T > T_min or E > E_th:
        x_new = [x[0] + random.uniform(-1, 1), x[1] + random.uniform(-1, 1)]
        E_new = Energy(x_new[0], x_new[1])
        deltaE = E_new - E

        print(
            f"Temperature: {T:.8f}, Next Energy: {E_new:.4f}, Current Energy: {E:.4f}, DeltaE: {deltaE:.4f}")

        if AcceptanceFunction(T, deltaE):
            x = x_new
            E = E_new
            print(f"--Accept: [{x_new[0]:.3f}, {x_new[1]:.3f}]")

        points.append(x)

        T = T * Alpha

    return x, points


result, points = SimulatedAnnealing(TMax, TMin, ETh, Alpha, Initial)
print(f"The last result: [{result[0]:.3f}, {result[1]:.3f}]")

x_points = [point[0] for point in points]
y_points = [point[1] for point in points]

plt.figure(figsize=(8, 6))
plt.plot(x_points, y_points, 'r.-', linewidth=1)

plt.xlabel('x')
plt.ylabel('y')

plt.grid(True)
plt.show()
