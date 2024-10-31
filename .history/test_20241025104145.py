import numpy as np


def generate_data(N, M):
    C = np.random.randint(1, 10, size=(N, M))  # Chi phí sản xuất
    P = np.random.randint(100, 500, size=N)    # Năng lực sản xuất
    D = np.random.randint(100, 500, size=M)    # Nhu cầu sản phẩm
    return C, P, D


# Danh sách số nhà máy và số sản phẩm
Ns = [10, 50, 100, 200, 300]  # Số nhà máy
Ms = [10, 50, 100, 200, 300]  # Số sản phẩm

# Vòng lặp để tạo dữ liệu cho từng cặp (N, M)
for N in Ns:
    for M in Ms:
        C, P, D = generate_data(N, M)  # Gọi hàm để tạo dữ liệu
        print(f"Số nhà máy (N): {N}, Số sản phẩm (M): {M}")
        print("Chi phí sản xuất (C):")
        print(C)
        print("Năng lực sản xuất (P):")
        print(P)
        print("Nhu cầu sản phẩm (D):")
        print(D)
        print("-" * 40)  # Dòng phân cách giữa các cặp (N, M)
