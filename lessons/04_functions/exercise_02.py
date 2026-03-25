"""
TQC Practice Exercise 02: Recursive Function
TQC 練習題 02：遞迴函式

Category: Functions (第四類：函式)

題目說明：
Write a recursive function power(base, exp) that calculates base^exp
without using the ** operator or pow() function.
請撰寫遞迴函式 power(base, exp)，不使用 ** 運算子或 pow() 函式。

Example Input / 輸入範例：
2
10
Expected Output / 預期輸出：
2 ^ 10 = 1024
"""

# Write your code below / 請在下方撰寫程式碼
# ============================================


def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


base = int(input())
exp = int(input())

print(f"{base} ^ {exp} = {power(base, exp)}")

# ============================================
# Challenge: Can you make it work with negative exponents?
# 挑戰：你能讓它支援負指數嗎？
