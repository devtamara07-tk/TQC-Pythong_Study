"""
Lesson 02 - Example 01: Basic if/else
第二課 - 範例一：基本 if/else

Selection structures let your program make decisions.
選擇結構讓你的程式能做出決定。
"""

# Simple if/else example / 簡單的 if/else 範例
number = int(input("Enter a number / 請輸入一個數字: "))

if number > 0:
    print(f"{number} is positive / 是正數")
elif number < 0:
    print(f"{number} is negative / 是負數")
else:
    print(f"{number} is zero / 是零")

# Comparison operators / 比較運算子
print("\n--- Comparison Operators / 比較運算子 ---")
a = 10
b = 20
print(f"{a} == {b} : {a == b}")    # Equal / 等於
print(f"{a} != {b} : {a != b}")    # Not equal / 不等於
print(f"{a} > {b}  : {a > b}")     # Greater than / 大於
print(f"{a} < {b}  : {a < b}")     # Less than / 小於
print(f"{a} >= {b} : {a >= b}")    # Greater or equal / 大於等於
print(f"{a} <= {b} : {a <= b}")    # Less or equal / 小於等於

# Even or odd check / 奇偶數判斷
num = int(input("\nEnter another number / 再輸入一個數字: "))
if num % 2 == 0:
    print(f"{num} is even / 是偶數")
else:
    print(f"{num} is odd / 是奇數")
