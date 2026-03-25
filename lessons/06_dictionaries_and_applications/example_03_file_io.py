"""
Lesson 06 - Example 03: File I/O
第六課 - 範例三：檔案讀寫

Reading from and writing to files.
讀取和寫入檔案。
"""

import os

# Get the directory of this script for file paths
script_dir = os.path.dirname(os.path.abspath(__file__))

# Writing to a file / 寫入檔案
print("--- Writing to file / 寫入檔案 ---")
filepath = os.path.join(script_dir, "sample_output.txt")
with open(filepath, "w", encoding="utf-8") as f:
    f.write("Hello, File I/O!\n")
    f.write("Python 檔案讀寫範例\n")
    for i in range(1, 6):
        f.write(f"Line {i}: This is line number {i}\n")
print(f"Written to {filepath}")

# Reading from a file / 讀取檔案
print("\n--- Reading from file / 讀取檔案 ---")
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()
print(content)

# Reading line by line / 逐行讀取
print("--- Reading line by line / 逐行讀取 ---")
with open(filepath, "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, 1):
        print(f"  [{line_num}] {line.strip()}")

# Appending to a file / 追加到檔案
print("\n--- Appending / 追加 ---")
with open(filepath, "a", encoding="utf-8") as f:
    f.write("This line was appended!\n")
    f.write("這一行是追加的！\n")
print("Appended successfully!")

# Reading into a list / 讀取成串列
with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()
print(f"\nTotal lines in file: {len(lines)}")

# Clean up / 清理
os.remove(filepath)
print(f"Cleaned up: removed {filepath}")
