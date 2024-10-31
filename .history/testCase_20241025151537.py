import time
import numpy as np
import cvxpy as cp

# Hàm tạo dữ liệu ngẫu nhiên


# def create_test_data(N, M):
#     C = np.random.randint(1, 11, size=(N, M))
#     P = np.random.randint(1000+N*10, 5000 + N*10, size=N)
#     D = np.random.randint(1000+M*10, 5000+M*10, size=M)
#     return C, P, D


# Hàm giải bài toán


def solveProblem(N, M, C, P, D):
    # C, P, D = create_test_data(N, M)
    X = cp.Variable((N, M), nonneg=True)
    objective = cp.Minimize(cp.sum(cp.multiply(C, X)))
    constraints = [cp.sum(X, axis=1) <= P, cp.sum(X, axis=0) >= D]
    problem = cp.Problem(objective, constraints)
    problem.solve()
    return problem, X

# Hàm tính thời gian chạy


def time_solver(N, M):
    start_time = time.time()
    problem, X = solveProblem(N, M)  # Gọi hàm giải bài toán
    end_time = time.time()
    return end_time - start_time, problem, X


# Khảo sát với kích thước tăng dần
# Ns = [10, 50, 100, 200, 300]  # Số nhà máy
# Ms = [10, 50, 100, 200, 300]  # Số sản phẩm


for N in Ns:
    for M in Ms:
        run_time, problem, X = time_solver(N, M)
        c, p, d = create_test_data(N, M)
        if run_time < 10:
            # print("C, P, D: ", c, p, d)
            print(f"Kích thước (N={N}, M={M}): {run_time:.4f} giây")

            # Kiểm tra xem bài toán có nghiệm không
            if X.value is not None:
                # Kết quả chi phí tối thiểu
                print("Chi phí tối thiểu:", np.round(problem.value, 2))

                # Kết quả số lượng sản phẩm tại các nhà máy (đã làm tròn)
                # print("Số lượng sản phẩm sản xuất tại các nhà máy (sau khi làm tròn):\n",
                #       np.round(X.value, 0))
            else:
                print("Không có nghiệm khả thi cho bài toán.")
