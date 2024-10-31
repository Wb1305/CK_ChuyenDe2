import time
import numpy as np
import cvxpy as cp
from readJson import read_testcases

# Hàm giải bài toán


def solveProblem(N, M, C, P, D):
    X = cp.Variable((N, M), nonneg=True)
    objective = cp.Minimize(cp.sum(cp.multiply(C, X)))
    constraints = [cp.sum(X, axis=1) <= P, cp.sum(X, axis=0) >= D]
    problem = cp.Problem(objective, constraints)
    problem.solve()
    return problem, X

# Hàm tính thời gian chạy


def time_solver(N, M, C, P, D):
    start_time = time.time()
    problem, X = solveProblem(N, M, C, P, D)  # Gọi hàm giải bài toán
    end_time = time.time()
    return end_time - start_time, problem, X


file_path = 'testcases.json'
N_list, M_list, C_list, P_list, D_list = read_testcases(file_path)
print("N_list:", N_list)
for i in range(len(N_list)):
    N = N_list[i]
    M = M_list[i]
    C = np.array(C_list[i])  # Assuming we are only using the first set of C
    P = np.array(P_list[i])   # Assuming we are only using the first set of P
    D = np.array(D_list[i])   # Assuming we are only using the first set of D

    run_time, problem, X = time_solver(N, M, C, P, D)

    if run_time < 10:
        print(f"Kích thước (N={N}, M={M}): {run_time:.4f} giây")

        if X.value is not None:
            print("Chi phí tối thiểu:", np.round(problem.value, 2))
        else:
            print("Không có nghiệm khả thi cho bài toán.")
