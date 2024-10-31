import numpy as np
import json

# Hàm đọc file JSON và trả về các mảng N, M, C, P, D


def read_testcases(file_path):
    with open(file_path, 'r') as f:
        testcases = json.load(f)

    # Tạo các danh sách để lưu giá trị riêng biệt
    N_list = []
    M_list = []
    C_list = []
    P_list = []
    D_list = []

    # Duyệt qua từng testcase và lưu giá trị vào các danh sách
    for testcase in testcases:
        N = testcase['N']
        M = testcase['M']
        C = np.array(testcase['C'])
        P = np.array(testcase['P'])
        D = np.array(testcase['D'])

        # Thêm giá trị vào danh sách tương ứng
        N_list.append(N)
        M_list.append(M)
        C_list.append(C)
        P_list.append(P)
        D_list.append(D)

    return N_list, M_list, C_list, P_list, D_list


# Đọc file testcases.json và lưu các giá trị vào danh sách riêng
# file_path = 'testcases.json'
# N_list, M_list, C_list, P_list, D_list = read_testcases(file_path)

# In thử một số kết quả
# print("N_list:", N_list)
# print("M_list:", M_list)
# print("C_list[0]:", C_list[0])  # In giá trị ma trận C của testcase đầu tiên
# print("P_list[0]:", P_list[0])  # In giá trị P của testcase đầu tiên
# print("D_list[0]:", D_list[0])  # In giá trị D của testcase đầu tiên
