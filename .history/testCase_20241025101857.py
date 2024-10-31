import time
import numpy as np
import cvxpy as cp

# Hàm tạo dữ liệu ngẫu nhiên


def create_test_data(N, M):
    C = np.random.randint(1, 10, size=(N, M))
    P = np.random.randint(100, 500, size=N)
    D = np.random.randint(100, 500, size=M)
    return C, P, D


# Hàm giải bài toán và đo thời gian chạy


def solveProblem(N, M):
    C, P, D = create_test_data(N, M)
    X = cp.Variable((N, M), nonneg=True)
    objective = cp.Minimize(cp.sum(cp.multiply(C, X)))
    constraints = [cp.sum(X, axis=1) <= P, cp.sum(X, axis=0) >= D]
    problem = cp.Problem(objective, constraints)
    problem.solve()
    return problem


# Khảo sát với kích thước tăng dần
Ns = [10, 50, 100, 200]  # Số nhà máy
Ms = [10, 50, 100, 200]  # Số sản phẩm
for N in Ns:
    for M in Ms:
        run_time = solve_and_time(N, M)
        if run_time < 10:
            print(f"Kích thước (N={N}, M={M}): {run_time:.4f} giây")
            # Kết quả chi phí tối thiểu
            print("Chi phí tối thiểu:", np.round(problem.value, 2))

            # Kết quả số lượng sản phẩm tại các nhà máy (đã làm tròn)
            print("Số lượng sản phẩm sản xuất tại các nhà máy (sau khi làm tròn):\n",
                  np.round(X.value, 2))
