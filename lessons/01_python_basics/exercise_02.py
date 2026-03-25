"""
TQC Practice Exercise 02: Variable Calculation
TQC 練習題 02：變數運算

Category: Basic I/O (第一類：基本輸入輸出)

題目說明：
Write a program that reads two integers from the user,
then outputs their sum, difference, product, and quotient.
請撰寫程式，讀取兩個整數，然後輸出它們的和、差、積、商。

Example Input / 輸入範例：
15
4

Expected Output / 預期輸出：
15 + 4 = 19
15 - 4 = 11
15 * 4 = 60
15 / 4 = 3.75

Hint / 提示：
- Use int() to convert input to integer
- Use f-string for formatted output
"""

# Write your code below / 請在下方撰寫程式碼
# ============================================

a = int(input())
b = int(input())

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")

# ============================================
# Try: Add floor division (//) and modulus (%) operations
# 試試：加上整數除法和取餘數的運算
