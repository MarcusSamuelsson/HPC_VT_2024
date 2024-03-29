import time
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
def stream_test(int STREAM_ARRAY_SIZE, double STREAM_ARRAY_TYPE, a, b, c):
    cdef double start, sizemem
    cdef unsigned int i
    cdef double copy, scale, add, triad
    times = [0] * 4

    # Get size of memory
    sizemem = STREAM_ARRAY_SIZE * STREAM_ARRAY_TYPE

    # Copy
    start = time.perf_counter()
    for i in range(STREAM_ARRAY_SIZE):
        a[i] = b[i]
    times[0] = time.perf_counter() - start

    # Scale
    start = time.perf_counter()
    for i in range(STREAM_ARRAY_SIZE):
        a[i] = 3.0 * b[i]
    times[1] = time.perf_counter() - start

    # Add
    start = time.perf_counter()
    for i in range(STREAM_ARRAY_SIZE):
        a[i] = b[i] + c[i]
    times[2] = time.perf_counter() - start
    
    # Triad
    start = time.perf_counter()
    for i in range(STREAM_ARRAY_SIZE):
        a[i] = b[i] + 3.0 * c[i]
    times[3] = time.perf_counter() - start

    # Get memory bandwidth triad
    copy = (2 * sizemem) / times[0]
    scale = (2 * sizemem) / times[1]
    add = (3 * sizemem) / times[2]
    triad = (3 * sizemem) / times[3]

    return copy, add, scale, triad