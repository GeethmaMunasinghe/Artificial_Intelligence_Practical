import random


def f(x):
    return -x ** 2 + 4 * x


def hill_climb(x_min, x_max, step_size=0.1):
    # Step 1: Choose a random starting point
    x = random.uniform(x_min, x_max)

    while True:
        # Step 2: Evaluate neighbors
        left_neighbor = x - step_size
        right_neighbor = x + step_size

        # Ensure neighbors are within bounds
        if left_neighbor < x_min:
            left_neighbor = x_min
        if right_neighbor > x_max:
            right_neighbor = x_max

        # Compute function values
        current_value = f(x)
        left_value = f(left_neighbor)
        right_value = f(right_neighbor)

        # Step 3: Move to the best neighbor
        if left_value > current_value:
            x = left_neighbor
        elif right_value > current_value:
            x = right_neighbor
        else:
            # Step 4: Stop when no better neighbor is found (local maximum)
            break

    return x, f(x)


# Define the range for x
x_min, x_max = -2, 6

# Run the hill climbing algorithm
optimal_x, optimal_f = hill_climb(x_min, x_max)

print(f"Optimal x: {optimal_x}")
print(f"Maximum value of f(x): {optimal_f}")

