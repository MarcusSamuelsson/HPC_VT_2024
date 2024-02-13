import numpy as np
import time
import cythonfn



def print_avg_for_excel(avg_time):
    titles = ["Copy", "Scale", "Add", "Triad", "Time"]

    print("Writing to file")

    with open("result_excel.txt", "w") as file:
        file.write("Start\n")
        for avg in avg_time:
            file.write(f"{avg}\n")
    
    print("Done writing to file")

if __name__ == "__main__":
    VARYING_GRID_SIZES = [10, 50, 100, 500, 1000, 2000]
    avgtimes = [0] * len(VARYING_GRID_SIZES)
    itterations = 10

    for size in VARYING_GRID_SIZES:
        print(f"Running test for size {size}")
        times = [0] * itterations

        for i in range(itterations):
            f = np.zeros((size,size))
            f[0] = 1
            f[-1] = 1
            f[:,0] = 1
            f[:,-1] = 1

            time_before = time.perf_counter()
            for j in range(1000):
                f = cythonfn.gauss_seidel(f)
            time_after = time.perf_counter()

            times[i] = time_after - time_before
        
        avgtimes[VARYING_GRID_SIZES.index(size)] = sum(times) / itterations
    
    print_avg_for_excel(avgtimes)


    