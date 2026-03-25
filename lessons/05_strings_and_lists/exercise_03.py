"""
TQC Practice Exercise 03: Matrix Operations
TQC 練習題 03：矩陣運算

Category: Lists (第五類：串列操作)

題目說明：
Read a 3x3 matrix (3 rows, each row has 3 space-separated integers).
Output:
1. The matrix itself
2. Sum of all elements
3. Sum of the main diagonal
4. The transposed matrix

請讀取一個 3x3 矩陣並輸出以上四項資訊。

Example Input / 輸入範例：
1 2 3
4 5 6
7 8 9
Expected Output / 預期輸出：
Matrix:
1 2 3
4 5 6
7 8 9
Total sum: 45
Diagonal sum: 15
Transposed:
1 4 7
2 5 8
3 6 9
"""

# Write your code below / 請在下方撰寫程式碼
# ============================================

# Read matrix
matrix = []
for _ in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)

# Print matrix
print("Matrix:")
for row in matrix:
    print(" ".join(map(str, row)))

# Total sum
total = sum(sum(row) for row in matrix)
print(f"Total sum: {total}")

# Diagonal sum
diag_sum = sum(matrix[i][i] for i in range(3))
print(f"Diagonal sum: {diag_sum}")

# Transpose
print("Transposed:")
for j in range(3):
    for i in range(3):
        print(matrix[i][j], end=" " if i < 2 else "")
    print()

# ============================================
