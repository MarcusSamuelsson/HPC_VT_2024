import numpy as np
import time
import h5py

def gauss_seidel(f):
    return (
        0.25 * 
        (np.roll(f, 1, 0) + 
        np.roll(f, -1, 0) + 
        np.roll(f, 1, 1) + 
        np.roll(f, -1, 1))
    )

if __name__ == "__main__":
    f = np.zeros((1000,1000))
    f[0] = 1
    f[-1] = 1
    f[:,0] = 1
    f[:,-1] = 1

    for j in range(1000):
        f = gauss_seidel(f)

    file_h5py = h5py.File("result.hdf5", "w")
    file_h5py.create_dataset(name = "f",
                            shape = f.shape,
                            dtype = f.dtype)
    file_h5py["f"][:,:] = f
    file_h5py.close()

    #Read result of h5py
    file_h5py = h5py.File("result.hdf5", "r")
    r_f = file_h5py["f"][:,:]
    print(r_f)

    file_h5py.close()

    




    