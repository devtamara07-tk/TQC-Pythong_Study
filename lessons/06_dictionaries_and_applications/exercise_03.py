"""
TQC Practice Exercise 03: Integrated Application - Day Calculator
TQC 練習題 03：綜合應用 - 星期計算器

Category: Integrated Application (第十類：綜合應用)

Based on the computational thinking example from Python1.pdf:
基於 Python1.pdf 中的運算思維範例：

"Today is Saturday. What day will it be after 100 days?"
「今天是星期六，100 天後是星期幾？」

Formula from PDF: (w + n) % 7 => day of week
PDF中的公式：(w + n) % 7 => 星期幾

題目說明：
Read the current day of the week (0=Sunday, 1=Monday, ..., 6=Saturday)
and a number of days n.
Output what day of the week it will be after n days.

Example Input / 輸入範例：
6
100
Expected Output / 預期輸出：
Today is Saturday.
After 100 days, it will be Monday.

Example Input / 輸入範例：
6
10100
Expected Output / 預期輸出：
Today is Saturday.
After 10100 days, it will be Monday.
"""

# Write your code below / 請在下方撰寫程式碼
# ============================================

days_of_week = [
    "Sunday", "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday"
]

w = int(input())     # Current day (0-6)
n = int(input())     # Number of days forward

today = days_of_week[w]
future_day = days_of_week[(w + n) % 7]

print(f"Today is {today}.")
print(f"After {n} days, it will be {future_day}.")

# ============================================
# This uses the pattern recognition concept from the PDF!
# 這使用了PDF中的模式識別概念！
# Formula: (current_day + days_forward) % 7 = future_day
