"""
Lesson 03 - Example 01: For Loops
第三課 - 範例一：For 迴圈

For loops iterate over a sequence of values.
For 迴圈用來遍歷一系列的值。
"""

# Basic for loop with range / 基本 for 迴圈搭配 range
print("--- Counting 1 to 5 / 從1數到5 ---")
for i in range(1, 6):
    print(i, end=" ")
print()  # New line

# range(start, stop, step) examples
# range(起始, 結束, 步長) 範例
print("\n--- range() examples ---")
print("range(5):", list(range(5)))           # 0,1,2,3,4
print("range(1,6):", list(range(1, 6)))      # 1,2,3,4,5
print("range(0,10,2):", list(range(0, 10, 2)))  # 0,2,4,6,8
print("range(10,0,-1):", list(range(10, 0, -1)))  # 10,9,...,1

# Sum of 1 to 100 (Gauss problem from PDF!)
# 1到100的總和（PDF中提到的高斯問題！）
print("\n--- Sum 1 to 100 (Algorithm 1 from PDF) ---")
total = 0
for i in range(1, 101):
    total += i
print(f"1 + 2 + 3 + ... + 100 = {total}")

# Using Gauss formula (Algorithm 2 from PDF)
# 使用高斯公式（PDF中的演算法二）
n = 100
gauss_sum = n * (n + 1) // 2
print(f"Using Gauss formula: n*(n+1)/2 = {gauss_sum}")

# Iterating over strings / 遍歷字串
print("\n--- Iterating over a string ---")
word = "Python"
for char in word:
    print(char, end=" ")
print()

# Using enumerate / 使用 enumerate
print("\n--- enumerate() ---")
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")
