import cvxpy as cp
import numpy as np

# Dữ liệu đầu vào
N = 3  # Số nhà máy
M = 2  # Số sản phẩm
C = np.array([[4, 6], [5, 3], [7, 8]])  # Chi phí sản xuất C_ij
P = np.array([100, 150, 200])  # Năng lực sản xuất P_i
D = np.array([130, 220])  # Nhu cầu sản phẩm D_j

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

# Kết quả
# Kết quả chi phí tối thiểu
print("Chi phí tối thiểu:", np.round(problem.value, 2))

# Kết quả số lượng sản phẩm tại các nhà máy (đã làm tròn)
print("Số lượng sản phẩm sản xuất tại các nhà máy (sau khi làm tròn):\n",
      np.round(X.value, 2))
