"""
Lesson 01 - Example 01: Hello World
第一課 - 範例一：Hello World

This is your first Python program!
這是你的第一個 Python 程式！
"""

import sys

# Use print() to display text on the screen
# 使用 print() 在螢幕上顯示文字
print("Hello, World!")
print("歡迎來到 Python 的世界！")
print("Welcome to the world of Python!")

# Print a separator line using string multiplication
# 使用字串乘法印出分隔線
print("-" * 40)

# Display Python version info
# 顯示 Python 版本資訊
print(f"Python version: {sys.version}")
print(f"Python path: {sys.executable}")

# Multiple print examples
# 多種 print 用法
print("Name:", "Python", "Version:", 3)       # Multiple arguments
print("A", "B", "C", sep=" -> ")              # Custom separator
print("Line 1", end=" | ")                    # Custom end character
print("Line 2")
