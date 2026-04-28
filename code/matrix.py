import random
import time


def generate_matrix(n):
    return [[random.random() for _ in range(n)] for _ in range(n)]


# Multiplica matrices
def multiply_matrices(A, B, n):
    C = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C

def run_experiment(n, runs):
    times = []

    for run in range(runs):
        A = generate_matrix(n)
        B = generate_matrix(n)

        start = time.time()
        multiply_matrices(A, B, n)
        end = time.time()

        t = end - start
        times.append(t)

        print(f"Run {run + 1}: {t:.6f}")

    average = sum(times) / len(times)
    print(f"Average: {average:.6f}")

    return average

if __name__ == "__main__":
    n = 200     
    runs = 5     

    run_experiment(n, runs)
