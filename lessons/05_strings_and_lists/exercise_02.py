"""
TQC Practice Exercise 02: List Statistics
TQC 練習題 02：串列統計

Category: Lists (第五類：串列操作)

題目說明：
Read n numbers from input (first line is n, then n numbers one per line).
Output the following statistics:
1. Count
2. Sum
3. Average (2 decimal places)
4. Maximum
5. Minimum
6. Sorted list (ascending)

請讀取 n 個數字並輸出以上六項統計資料。

Example Input / 輸入範例：
5
23
45
12
67
34
Expected Output / 預期輸出：
Count: 5
Sum: 181
Average: 36.20
Max: 67
Min: 12
Sorted: [12, 23, 34, 45, 67]
"""

# Write your code below / 請在下方撰寫程式碼
# ============================================

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

print(f"Count: {len(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers):.2f}")
print(f"Max: {max(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Sorted: {sorted(numbers)}")

# ============================================
