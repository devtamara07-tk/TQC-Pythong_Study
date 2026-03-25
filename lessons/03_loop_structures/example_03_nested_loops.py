"""
Lesson 03 - Example 03: Nested Loops
第三課 - 範例三：巢狀迴圈

Loops inside loops for 2D patterns and tables.
迴圈中的迴圈，用於2D圖形和表格。
"""

# Simple rectangle pattern / 簡單矩形圖案
print("--- Rectangle Pattern / 矩形圖案 ---")
for row in range(3):
    for col in range(5):
        print("*", end=" ")
    print()

# Right triangle pattern / 直角三角形圖案
print("\n--- Triangle Pattern / 三角形圖案 ---")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# Number triangle / 數字三角形
print("\n--- Number Triangle / 數字三角形 ---")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Multiplication table (partial) / 九九乘法表（部分）
print("\n--- Multiplication Table (2-5) / 乘法表 ---")
for i in range(2, 6):
    for j in range(1, 10):
        print(f"{i}x{j}={i*j:2d}", end="  ")
    print()

# Diamond pattern / 菱形圖案
print("\n--- Diamond Pattern / 菱形圖案 ---")
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)
