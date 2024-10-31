import create_test_data from '././testCase.py'


def mySolve(N, M):
    C, P, D = create_test_data(N, M)

    # Biến số X_ij
    X = cp.Variable((N, M), nonneg=True)

    # Hàm mục tiêu: Minimize Z
    objective = cp.Minimize(cp.sum(cp.multiply(C, X)))

    # Ràng buộc
    constraints = [
        cp.sum(X, axis=1) <= P,  # Ràng buộc năng lực sản xuất
        cp.sum(X, axis=0) >= D   # Ràng buộc đáp ứng nhu cầu
    ]

    # Thiết lập bài toán và giải
    problem = cp.Problem(objective, constraints)
    start_time = time.time()
    problem.solve()
    end_time = time.time()

    return end_time - start_time


# Khảo sát với kích thước tăng dần
Ns = [10, 50, 100, 200]  # Số nhà máy
Ms = [10, 50, 100, 200]  # Số sản phẩm
for N in Ns:
    for M in Ms:
        run_time = mySolve(N, M)
        if run_time < 10:
            print(f"Kích thước (N={N}, M={M}): {run_time:.4f} giây")
