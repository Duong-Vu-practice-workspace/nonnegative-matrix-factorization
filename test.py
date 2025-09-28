import numpy as np
from mu import mu
A = np.array(
    [
        [1, 1, 0],
        [1, 0, 1],
        [1, 0, 0],
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 1]
    ]
, dtype=float)
k = 2
W0 = np.array(
    [
        [1, 2],
        [2, 1],
        [1, 1],
        [2, 2],
        [1, 2],
        [2, 1]
    ]
, dtype=float)
H0 = np.array(
    [
        [1, 1, 2],
        [2, 1, 1]
    ]
, dtype=float)
print(A.shape)
print(W0.shape)
print(H0.shape)

W, H = mu(A, k, delta = 0, num_iter=50, init_W=W0, init_H=H0, print_enabled=True)
print(W)
print("================================")
print(H)