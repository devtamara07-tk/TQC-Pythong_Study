"""
TQC Practice Exercise 01: Math Functions
TQC 練習題 01：數學函式

Category: Functions (第四類：函式)

題目說明：
Write the following functions:
1. circle_area(radius) - returns the area of a circle
2. circle_perimeter(radius) - returns the perimeter of a circle
3. rectangle_area(width, height) - returns the area of a rectangle

Read radius, width, height from input and print results rounded to 2 decimals.
請撰寫上述函式，讀取輸入並印出結果（四捨五入到小數點後兩位）。

Example Input / 輸入範例：
5
3
4
Expected Output / 預期輸出：
Circle area: 78.54
Circle perimeter: 31.42
Rectangle area: 12
"""

import math

# Write your code below / 請在下方撰寫程式碼
# ============================================


def circle_area(radius):
    return math.pi * radius ** 2


def circle_perimeter(radius):
    return 2 * math.pi * radius


def rectangle_area(width, height):
    return width * height


radius = float(input())
width = float(input())
height = float(input())

print(f"Circle area: {circle_area(radius):.2f}")
print(f"Circle perimeter: {circle_perimeter(radius):.2f}")
print(f"Rectangle area: {rectangle_area(width, height):.0f}")

# ============================================
