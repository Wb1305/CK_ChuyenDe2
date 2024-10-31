

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
    problem.solve()
