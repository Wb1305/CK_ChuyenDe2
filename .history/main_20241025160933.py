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
print("X=", objective)

# Ràng buộc
constraints = [
    cp.sum(X, axis=1) <= P,  # Ràng buộc năng lực sản xuất
    cp.sum(X, axis=0) >= D   # Ràng buộc đáp ứng nhu cầu
]

# Thiết lập bài toán và giải
problem = cp.Problem(objective, constraints)
problem.solve()

# Kết quả chi phí tối thiểu
print("Chi phí tối thiểu:", np.round(problem.value, 2))

# Kết quả số lượng sản phẩm tại các nhà máy (đã làm tròn)
print("Số lượng sản phẩm sản xuất tại các nhà máy (sau khi làm tròn):\n",
      np.round(X.value, 2))

# # Kiểm tra các ràng buộc có được thỏa mãn không
# print("\nKiểm tra các ràng buộc:")

# # Kiểm tra ràng buộc năng lực sản xuất
# production_check = np.all(np.sum(X.value, axis=1) <= P)
# print("Ràng buộc năng lực sản xuất có được thỏa mãn?", production_check)

# # Kiểm tra ràng buộc nhu cầu sản phẩm
# demand_check = np.all(np.sum(X.value, axis=0) >= D)
# print("Ràng buộc nhu cầu sản phẩm có được thỏa mãn?", demand_check)
# total_capacity = np.sum(P)
# total_demand = np.sum(D)
# print(f"Tổng năng lực sản xuất: {total_capacity}")
# print(f"Tổng nhu cầu sản phẩm: {total_demand}")
# print("Tổng số sản phẩm được sản xuất (theo loại sản phẩm):",
#       np.sum(X.value, axis=0))
# print("Nhu cầu sản phẩm:", D)
# demand_check = np.all(np.sum(X.value, axis=0) >= D - 1e-5)
# print("Ràng buộc nhu cầu sản phẩm có được thỏa mãn (với sai số nhỏ)?", demand_check)
