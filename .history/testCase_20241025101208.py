import time

# Hàm tạo dữ liệu ngẫu nhiên


def create_test_data(N, M):
    C = np.random.randint(1, 10, size=(N, M))
    P = np.random.randint(100, 500, size=N)
    D = np.random.randint(100, 500, size=M)
    return C, P, D

# Hàm giải bài toán và đo thời gian chạy


# def solve_and_time(N, M):
#     C, P, D = create_test_data(N, M)
#     X = cp.Variable((N, M), nonneg=True)
#     objective = cp.Minimize(cp.sum(cp.multiply(C, X)))
#     constraints = [cp.sum(X, axis=1) <= P, cp.sum(X, axis=0) >= D]
#     problem = cp.Problem(objective, constraints)

#     start_time = time.time()
#     problem.solve()
#     end_time = time.time()

#     return end_time - start_time


# # Khảo sát với kích thước tăng dần
# Ns = [10, 50, 100, 200]  # Số nhà máy
# Ms = [10, 50, 100, 200]  # Số sản phẩm
# for N in Ns:
#     for M in Ms:
#         run_time = solve_and_time(N, M)
#         if run_time < 10:
#             print(f"Kích thước (N={N}, M={M}): {run_time:.4f} giây")
