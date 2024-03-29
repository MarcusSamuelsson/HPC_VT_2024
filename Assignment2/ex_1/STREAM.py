from time import perf_counter as timer
from sys import getsizeof as sizeof
import array
from objsize import get_deep_size

def stream_test(STREAM_ARRAY_SIZE, STREAM_ARRAY_TYPE_SIZE, a, b, c):
    times = [0] * 4

    sizemem = STREAM_ARRAY_SIZE * STREAM_ARRAY_TYPE_SIZE

    # Copy
    start = timer()
    for i in range(STREAM_ARRAY_SIZE):
        a[i] = b[i]
    times[0] = timer() - start

    # Scale
    start = timer()
    for i in range(STREAM_ARRAY_SIZE):
        a[i] = 3.0 * b[i]
    times[1] = timer() - start

    # Add
    start = timer()
    for i in range(STREAM_ARRAY_SIZE):
        a[i] = b[i] + c[i]
    times[2] = timer() - start
    
    # Triad
    start = timer()
    for i in range(STREAM_ARRAY_SIZE):
        a[i] = b[i] + 3.0 * c[i]
    times[3] = timer() - start

    # Get memory bandwidth
    copy = (2 * sizemem)/times[0]
    scale = (2 * sizemem)/times[1]
    add = (3 * sizemem)/times[2]
    triad = (3 * sizemem)/times[3]

    return copy, add, scale, triad

def print_avg_for_excel(size_var, copy_avg, add_avg, scale_avg, triad_avg, functions):
    titles = ["Copy", "Scale", "Add", "Triad", "Time"]

    print("Writing to file")

    with open("result_excel.txt", "w") as file:
        file.write("Start\n")
        for i in range(len(functions)):
            file.write(f"{functions[i]}\n")
            for j in range(4):
                file.write(f"{titles[j]}\n")
                for k in range(len(size_var)):
                    if j == 0:
                        file.write(f"{copy_avg[k+len(size_var)*i]}\n")
                    elif j == 1:
                        file.write(f"{scale_avg[k+len(size_var)*i]}\n")
                    elif j == 2:
                        file.write(f"{add_avg[k+len(size_var)*i]}\n")
                    elif j == 3:
                        file.write(f"{triad_avg[k+len(size_var)*i]}\n")
                file.write("\n")
    
    print("Done writing to file")
                    
def run_test():
    itterations = 10
    size_variations = [10, 100, 1000, 10000, 50000, 100000, 500000, 1000000, 10000000]
    functions = ["arrays.array", "python.list"]
    final_avg_copy = [0] * len(size_variations)*2
    final_avg_add = [0] * len(size_variations)*2
    final_avg_scale = [0] * len(size_variations)*2
    final_avg_triad = [0] * len(size_variations)*2

    for fun in functions:
        print(f"Running test for {fun}")

        for size in size_variations:
            total_copy = [0] * itterations
            total_add = [0] * itterations
            total_scale = [0] * itterations
            total_triad = [0] * itterations

            for i in range(itterations):
                if fun == "arrays.array":
                    a = array.array("d", [1.0] * size)
                    b = array.array("d", [2.0] * size)
                    c = array.array("d", [0.0] * size)
                    STREAM_ARRAY_TYPE_SIZE = sizeof(array.array("d", [0])) - sizeof(array.array("d", []))
                elif fun == "python.list":
                    a = [1.0] * size
                    b = [2.0] * size
                    c = [0.0] * size
                    STREAM_ARRAY_TYPE_SIZE = sizeof([0]) - sizeof([])

                copy, add, scale, triad = stream_test(size, STREAM_ARRAY_TYPE_SIZE, a, b, c)
                total_copy[i] = copy
                total_add[i] = add
                total_scale[i] = scale
                total_triad[i] = triad

            print(f"Running test for {fun} with size {size}")

            #Get average memory bandwidth in MB/s
            avg_copy = (sum(total_copy)/itterations)/1000000
            avg_scale = (sum(total_scale)/itterations)/1000000
            avg_add = (sum(total_add)/itterations)/1000000
            avg_triad = (sum(total_triad)/itterations)/1000000

            print(f"Avrage bandwidth copy: {avg_copy} MB")
            print(f"Avrage bandwidth scale: {avg_scale} MB")
            print(f"Avrage bandwidth add: {avg_add} MB")
            print(f"Avrage bandwidth triad: {avg_triad} MB")
            print("---------------------------------")
            print("")

            final_avg_copy[size_variations.index(size)+len(size_variations)*functions.index(fun)] = avg_copy
            final_avg_add[size_variations.index(size)+len(size_variations)*functions.index(fun)] = avg_add
            final_avg_scale[size_variations.index(size)+len(size_variations)*functions.index(fun)] = avg_scale
            final_avg_triad[size_variations.index(size)+len(size_variations)*functions.index(fun)] = avg_triad

    
    print_avg_for_excel(size_variations, final_avg_copy, final_avg_add, final_avg_scale, final_avg_triad, functions)

if __name__ == "__main__":
    run_test()
    print("Done")
        
