"""
TQC Practice Exercise 02: Multiplication Table
TQC 練習題 02：九九乘法表

Category: Loop Structure (第三類：迴圈結構)

題目說明：
Read an integer n (1-9) and print the multiplication table for n.
請讀取整數 n (1-9)，印出 n 的乘法表。

Example Input / 輸入範例：7
Expected Output / 預期輸出：
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63
"""

# Write your code below / 請在下方撰寫程式碼
# ============================================

n = int(input())

for i in range(1, 10):
    print(f"{n} * {i} = {n * i}")

# ============================================
# Bonus: Print the FULL 9x9 multiplication table
# 加分：印出完整的九九乘法表
