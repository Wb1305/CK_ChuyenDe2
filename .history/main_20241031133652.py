import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

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
    cp.sum(X, axis=1) <= P,  # Ràng buộc năng lực sản xuất, tổng hàng ngang
    cp.sum(X, axis=0) >= D   # Ràng buộc đáp ứng nhu cầu, tổng hàng dọc
]

# Thiết lập bài toán và giải
problem = cp.Problem(objective, constraints)
problem.solve()

# Kết quả chi phí tối thiểu
print("Chi phí tối thiểu:", np.round(problem.value, 2))

# Kết quả số lượng sản phẩm tại các nhà máy (đã làm tròn)
print("Số lượng sản phẩm sản xuất tại các nhà máy (sau khi làm tròn):\n",
      np.round(X.value, 2))

total_production_per_factory = np.sum(X.value, axis=1)

plt.figure(figsize=(10, 6))
# plt.subplot(2, 1, 1)
plt.bar([f"Nhà máy {i+1}" for i in range(N)],
        total_production_per_factory, color='skyblue')
plt.xlabel("Nhà máy")
plt.ylabel("Tổng sản lượng sản xuất")
plt.title("Biểu đồ tổng sản lượng sản xuất của mỗi nhà máy")
plt.show()

# Chi phí sản xuất tại từng nhà máy cho từng sản phẩm
plt.figure(figsize=(10, 6))
# plt.subplot(2, 1, 2)
bar_width = 0.35
index = np.arange(N)

for j in range(M):
    plt.bar(index + j * bar_width,
            X.value[:, j], bar_width, label=f"Sản phẩm {j+1}")

plt.xlabel("Nhà máy")
plt.ylabel("Số lượng sản phẩm sản xuất")
plt.title("Biểu đồ số lượng sản phẩm sản xuất tại mỗi nhà máy")
plt.xticks(index + bar_width * (M - 1) / 2,
           [f"Nhà máy {i+1}" for i in range(N)])
plt.legend()
plt.tight_layout()
plt.show()

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
