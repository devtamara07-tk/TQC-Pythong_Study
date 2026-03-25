"""
Lesson 04 - Example 03: Advanced Function Concepts
第四課 - 範例三：進階函式概念

Scope, recursion, and higher-order functions.
範圍、遞迴和高階函式。
"""


# Variable scope / 變數範圍
print("--- Variable Scope / 變數範圍 ---")
x = 10  # Global variable / 全域變數


def show_scope():
    x = 20  # Local variable / 區域變數
    print(f"  Inside function: x = {x}")


show_scope()
print(f"  Outside function: x = {x}")

print("-" * 40)


# Recursion / 遞迴
print("--- Recursion / 遞迴 ---")


def factorial(n):
    """Calculate n! using recursion / 使用遞迴計算 n!"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


for i in range(1, 8):
    print(f"  {i}! = {factorial(i)}")

print("-" * 40)


# Fibonacci sequence / 費波那契數列
def fibonacci(n):
    """Return nth Fibonacci number / 回傳第n個費波那契數"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print("--- Fibonacci Sequence / 費波那契數列 ---")
for i in range(10):
    print(fibonacci(i), end=" ")
print()

print("-" * 40)


# Higher-order functions / 高階函式
print("--- map, filter, reduce ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map: apply function to each element / 對每個元素套用函式
squares = list(map(lambda x: x ** 2, numbers))
print(f"Squares: {squares}")

# filter: keep elements that satisfy condition / 保留滿足條件的元素
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens: {evens}")

# List comprehension (Pythonic alternative) / 串列推導式
squares_lc = [x ** 2 for x in numbers]
evens_lc = [x for x in numbers if x % 2 == 0]
print(f"Squares (comprehension): {squares_lc}")
print(f"Evens (comprehension): {evens_lc}")
