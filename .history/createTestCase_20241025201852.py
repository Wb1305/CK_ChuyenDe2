import json
import numpy as np

# Hàm tạo dữ liệu cho các nhà máy và sản phẩm


def generate_data(N, M):
    C = np.random.randint(1, 10, size=(N, M))  # Chi phí sản xuất
    P = np.random.randint(100 + N*5, 500 + N*5,
                          size=N)    # Năng lực sản xuất
    D = np.random.randint(100 + M*5, 500 + M*5, size=M)    # Nhu cầu sản phẩm
    return C, P, D


# Tạo danh sách các testcase
Ns = [5, 10, 50, 100, 200, 250, 300]  # Số nhà máy
Ms = [5, 10, 50, 100, 200, 250, 300]  # Số loại sản phẩm

testcases = []
for N, M in zip(Ns, Ms):
    C, P, D = generate_data(N, M)
    testcases.append({'N': N, 'M': M, 'C': C.tolist(),
                     'P': P.tolist(), 'D': D.tolist()})

# Lưu testcases vào file
output_file = 'testcases.json'
with open(output_file, 'w') as f:
    json.dump(testcases, f, indent=4)
    print("done created!")
