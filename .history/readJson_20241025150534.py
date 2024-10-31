import json
import numpy as np
# Hàm đọc file JSON và trả về các giá trị N, M, C, P, D


def read_testcases_from_file(file_path):
    with open(file_path, 'r') as f:
        testcases = json.load(f)

    # Trả về danh sách các giá trị N, M, C, P, D
    for testcase in testcases:
        N = testcase['N']
        M = testcase['M']
        C = np.array(testcase['C'])
        P = np.array(testcase['P'])
        D = np.array(testcase['D'])
        # print(f"N: {N}, M: {M}\nC: {C}\nP: {P}\nD: {D}\n")
    return N, M, C, P, D


# Đọc file testcases.json và in ra các giá trị
file_path = 'testcases.json'
N, M, C, P, D = read_testcases_from_file(file_path)
print(f"N: {N}, M: {M}\nC: {C}\nP: {P}\nD: {D}\n")
