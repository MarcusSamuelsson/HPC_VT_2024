import time
import timeit
import numpy as np

def checktickTimeTime():
    M = 200
    timesfound = np.empty((M,))
    for i in range(M):
        t1 =  time.time() # get timestamp from timer
        t2 = time.time() # get timestamp from timer
        while (t2 - t1) < 1e-16: # if zero then we are below clock granularity, retake timing
            t2 = time.time() # get timestamp from timer
        t1 = t2 # this is outside the loop
        timesfound[i] = t1 # record the time stamp
    minDelta = 1000000
    Delta = np.diff(timesfound) # it should be cast to int only when needed
    minDelta = Delta.min()
    return minDelta

def checktickTimeNano():
    M = 200
    timesfound = np.empty((M,))
    for i in range(M):
        t1 =  time.time_ns()*pow(10, -9) # get timestamp from timer
        t2 = time.time_ns()*pow(10, -9) # get timestamp from timer
        while (t2 - t1) < 1e-16: # if zero then we are below clock granularity, retake timing
            t2 = time.time_ns()*pow(10, -9) # get timestamp from timer
        t1 = t2 # this is outside the loop
        timesfound[i] = t1 # record the time stamp
    minDelta = 1000000
    Delta = np.diff(timesfound) # it should be cast to int only when needed
    minDelta = Delta.min()
    return minDelta

def checktickTimeit():
    M = 200
    timesfound = np.empty((M,))
    for i in range(M):
        t1 = timeit.default_timer() # get timestamp from timer
        t2 =  timeit.default_timer() # get timestamp from timer
        while (t2 - t1) < 1e-16: # if zero then we are below clock granularity, retake timing
            t2 = timeit.default_timer() # get timestamp from timer
        t1 = t2 # this is outside the loop
        timesfound[i] = t1 # record the time stamp
    minDelta = 1000000
    Delta = np.diff(timesfound) # it should be cast to int only when needed
    minDelta = Delta.min()
    return minDelta

if __name__ == "__main__":
    minDeltaTimeTime = checktickTimeTime()
    minDeltaTimeNano = checktickTimeNano()
    minDeltaTimeTimeit = checktickTimeit()
    print("minDeltaTimeTime: ", minDeltaTimeTime)
    print("minDeltaTimeNano: ", minDeltaTimeNano)
    print("minDeltaTimeTimeit: ", minDeltaTimeTimeit)