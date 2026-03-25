"""
TQC Practice Exercise 01: Sum of Series
TQC 練習題 01：級數求和

Category: Loop Structure (第三類：迴圈結構)

題目說明：
Read an integer n, calculate and output:
1. Sum = 1 + 2 + 3 + ... + n
2. Sum of squares = 1² + 2² + 3² + ... + n²
3. Sum of odd numbers from 1 to n

請讀取整數 n，計算並輸出以上三個值。

Example Input / 輸入範例：10
Expected Output / 預期輸出：
Sum of 1 to 10 = 55
Sum of squares = 385
Sum of odd numbers = 25
"""

# Write your code below / 請在下方撰寫程式碼
# ============================================

n = int(input())

# 1. Sum of 1 to n
total = 0
for i in range(1, n + 1):
    total += i
print(f"Sum of 1 to {n} = {total}")

# 2. Sum of squares
sq_sum = 0
for i in range(1, n + 1):
    sq_sum += i ** 2
print(f"Sum of squares = {sq_sum}")

# 3. Sum of odd numbers
odd_sum = 0
for i in range(1, n + 1, 2):
    odd_sum += i
print(f"Sum of odd numbers = {odd_sum}")

# ============================================
# Challenge: Can you solve these using formulas instead of loops?
# 挑戰：你能用公式而不是迴圈來解決嗎？
# Sum = n*(n+1)/2
# Sum of squares = n*(n+1)*(2n+1)/6
