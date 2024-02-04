from timeit import default_timer as timer
from sys import getsizeof as sizeof
import array

def stream_test_array(STREAM_ARRAY_SIZE, STREAM_ARRAY_TYPE):
    times = [0] * 4

    # initialize arrays
    a = array.array("f", [0] * STREAM_ARRAY_SIZE)
    b = array.array("f", [0] * STREAM_ARRAY_SIZE)
    c = array.array("f", [0] * STREAM_ARRAY_SIZE)

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
    copy = STREAM_ARRAY_SIZE * sizeof(STREAM_ARRAY_TYPE) / times[0]
    scale = STREAM_ARRAY_SIZE * sizeof(STREAM_ARRAY_TYPE) / times[1]
    add = STREAM_ARRAY_SIZE * sizeof(STREAM_ARRAY_TYPE) / times[2]
    triad = STREAM_ARRAY_SIZE * sizeof(STREAM_ARRAY_TYPE) / times[3]

    return times, copy, add, scale, triad

def stream_test_lists(STREAM_ARRAY_SIZE, STREAM_ARRAY_TYPE):
    times = [0] * 4

    # initialize lists
    a = [0] * STREAM_ARRAY_SIZE
    b = [0] * STREAM_ARRAY_SIZE
    c = [0] * STREAM_ARRAY_SIZE

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
    copy = STREAM_ARRAY_SIZE * sizeof(STREAM_ARRAY_TYPE) / times[0]
    scale = STREAM_ARRAY_SIZE * sizeof(STREAM_ARRAY_TYPE) / times[1]
    add = STREAM_ARRAY_SIZE * sizeof(STREAM_ARRAY_TYPE) / times[2]
    triad = STREAM_ARRAY_SIZE * sizeof(STREAM_ARRAY_TYPE) / times[3]

    return times, copy, add, scale, triad

def get_standard_deviation(times, itterations):
    avrage_time = sum(times) / itterations
    standard_deviation = 0

    for i in range(itterations):
        standard_deviation += (times[i] - avrage_time) ** 2

    standard_deviation = (standard_deviation / itterations) ** 0.5

    return standard_deviation

def print_itteration_to_file(size, itteration, times, copy, add, scale, triad, fun_name):
    with open("result.txt", "w") as file:
        file.write(f"Running test for {fun_name}\n")

        file.write(f"Size: {size}, Itteration: {itteration}\n")
        file.write(f"Copy: {times[0]}, {copy/1000000} MB/s\n")
        file.write(f"Scale: {times[1]}, {scale/1000000} MB/s\n")
        file.write(f"Add: {times[2]}, {add/1000000} MB/s\n")
        file.write(f"Triad: {times[3]}, {triad/1000000} MB/s\n")
        
        file.write(f"---------------------------------\n")

def print_avg_for_excel(size_var, times_avg, copy_avg, add_avg, scale_avg, triad_avg, functions):
    titles = ["Copy", "Scale", "Add", "Triad", "Time"]

    print("Writing to file")

    with open("result_excel.txt", "w") as file:
        file.write("Start\n")
        for i in range(len(functions)):
            file.write(f"{functions[i].__name__}\n")
            for j in range(5):
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
                    elif j == 4:
                        file.write(f"{times_avg[k+len(size_var)*i]}\n")
                file.write("\n")
    
    print("Done writing to file")
                    
                


        

def run_test():
    itterations = 10
    size_variations = [10, 100, 1000, 10000, 50000, 100000, 500000, 1000000, 10000000]
    STREAM_ARRAY_TYPE = float
    functions = [stream_test_array, stream_test_lists]
    final_avg_times = [0] * len(size_variations)*2
    final_avg_copy = [0] * len(size_variations)*2
    final_avg_add = [0] * len(size_variations)*2
    final_avg_scale = [0] * len(size_variations)*2
    final_avg_triad = [0] * len(size_variations)*2

    for fun in functions:
        print(f"Running test for {fun.__name__}")

        for size in size_variations:
            total_times_0 = [0] * itterations
            total_times_1 = [0] * itterations
            total_times_2 = [0] * itterations
            total_times_3 = [0] * itterations
            total_copy = [0] * itterations
            total_add = [0] * itterations
            total_scale = [0] * itterations
            total_triad = [0] * itterations

            for i in range(itterations):
                times, copy, add, scale, triad = fun(size, STREAM_ARRAY_TYPE)
                
                print_itteration_to_file(size, i, times, copy, add, scale, triad, fun.__name__)

                total_times_0[i] = times[0]
                total_times_1[i] = times[1]
                total_times_2[i] = times[2]
                total_times_3[i] = times[3]
                total_copy[i] = copy
                total_add[i] = add
                total_scale[i] = scale
                total_triad[i] = triad

            print(f"Running test for {fun.__name__} with size {size}")

            #Get avrage time
            avg_time = [0] * 4
            avg_time[0] = sum(total_times_0)/itterations
            avg_time[1] = sum(total_times_1)/itterations
            avg_time[2] = sum(total_times_2)/itterations
            avg_time[3] = sum(total_times_3)/itterations

            print(f"Avrage time copy: {sum(total_times_0)/itterations} seconds")
            print(f"Avrage time scale: {sum(total_times_1)/itterations} seconds")
            print(f"Avrage time add: {sum(total_times_2)/itterations} seconds")
            print(f"Avrage time triad: {sum(total_times_3)/itterations} seconds")
            print("")

            #Get average memory bandwidth in MB/s
            avg_copy = sum(total_copy)/itterations
            avg_scale = sum(total_scale)/itterations
            avg_add = sum(total_add)/itterations
            avg_triad = sum(total_triad)/itterations

            avg_copy = (avg_copy/1000000)
            avg_scale = (avg_scale/1000000)
            avg_add = (avg_add/1000000)
            avg_triad = (avg_triad/1000000)

            print(f"Avrage bandwidth copy: {avg_copy} MB/s")
            print(f"Avrage bandwidth scale: {avg_scale} MB/s")
            print(f"Avrage bandwidth add: {avg_add} MB/s")
            print(f"Avrage bandwidth triad: {avg_triad} MB/s")
            print("---------------------------------")
            print("")

            final_avg_times[size_variations.index(size)+len(size_variations)*functions.index(fun)] = avg_time
            final_avg_copy[size_variations.index(size)+len(size_variations)*functions.index(fun)] = avg_copy
            final_avg_add[size_variations.index(size)+len(size_variations)*functions.index(fun)] = avg_add
            final_avg_scale[size_variations.index(size)+len(size_variations)*functions.index(fun)] = avg_scale
            final_avg_triad[size_variations.index(size)+len(size_variations)*functions.index(fun)] = avg_triad

    
    print_avg_for_excel(size_variations, final_avg_times, final_avg_copy, final_avg_add, final_avg_scale, final_avg_triad, functions)

if __name__ == "__main__":
    run_test()
    print("Done")
        
