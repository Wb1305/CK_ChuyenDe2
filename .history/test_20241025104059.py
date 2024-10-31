import numpy as np


def generate_data(N, M):
    C = np.random.randint(1, 10, size=(N, M))
    P = np.random.randint(100, 500, size=N)
    D = np.random.randint(100, 500, size=M)
    return C, P, D


# Gọi hàm với N=3 và M=2
C, P, D = generate_data(3, 2)

print("Chi phí sản xuất (C):")
print(C)
print("Năng lực sản xuất (P):")
print(P)
print("Nhu cầu sản phẩm (D):")
print(D)
