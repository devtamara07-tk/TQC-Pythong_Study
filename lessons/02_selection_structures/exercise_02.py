"""
TQC Practice Exercise 02: Leap Year
TQC 練習題 02：閏年判斷

Category: Selection Structure (第二類：選擇結構)

題目說明：
Write a program that reads a year and determines if it is a leap year.
請撰寫程式，讀取年份並判斷是否為閏年。

Leap year rules / 閏年規則：
  1. Divisible by 4 / 可被4整除
  2. BUT not divisible by 100 / 但不可被100整除
  3. UNLESS also divisible by 400 / 除非也可被400整除

Example Input / 輸入範例：2024
Expected Output / 預期輸出：2024 is a leap year.

Example Input / 輸入範例：1900
Expected Output / 預期輸出：1900 is not a leap year.
"""

# Write your code below / 請在下方撰寫程式碼
# ============================================

year = int(input())

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# ============================================
# Try: Test with years 2000, 1900, 2024, 2023
# 試試：用 2000、1900、2024、2023 測試
