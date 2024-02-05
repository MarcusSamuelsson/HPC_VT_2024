import numpy as np
from timeit import default_timer as timer

def DGEMM(A, B, C):
    n = len(A)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

def get_standard_deviation(times, avg):
    return sum([(x - avg) ** 2 for x in times]) / len(times)

def run_time_test(size_var, itter):
    times = [0] * itter
    average = [0] * len(size_var)
    std_dev = [0] * len(size_var)
    
    for i in range(len(size_var)):
        n = size_var[i]

        print(f"Running test for n = {n}")

        A = np.random.rand(n, n)
        B = np.random.rand(n, n)
        C = np.zeros((n, n))
        
        for j in range(itter):
            start = timer()
            DGEMM(A, B, C)
            times[j] = timer() - start

        average[i] = sum(times) / itter
        std_dev[i] = get_standard_deviation(times, average[i])

    return average, std_dev

def print_for_excel(size_var, avg, std_dev):
    print("Writing to file")

    with open("result_excel.txt", "w") as file:
        file.write("Start\n")
        file.write("Average\n")
        for i in range(len(size_var)):
            file.write(f"{avg[i]}\n")
        file.write("\n")
        file.write("Standard deviation\n")
        for i in range(len(size_var)):
            file.write(f"{std_dev[i]}\n")

if __name__ == "__main__":
    size_var = [10, 20, 30, 40, 50, 100, 150, 200, 300, 400, 500]
    itter = 10

    avg, std_dev = run_time_test(size_var, itter)
    print_for_excel(size_var, avg, std_dev)