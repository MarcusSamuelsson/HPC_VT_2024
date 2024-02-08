from timeit import default_timer as timer

def stream_test(STREAM_ARRAY_SIZE, STREAM_ARRAY_TYPE, a, b, c):
    times = [0] * 4

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

    return copy, add, scale, triad