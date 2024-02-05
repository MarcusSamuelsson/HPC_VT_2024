import pytest
import numpy as np
from DGEMM_Benchmark import DGEMM as dgemm

@pytest.mark.parametrize("n", [100, 200, 300])

def test_dgemm(n):
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)
    C = np.zeros((n, n))
    dgemm(A, B, C)

    C_blas = np.zeros((n, n))
    C_blas = np.dot(A, B)
    assert np.allclose(C, C_blas, atol=1e-10)
