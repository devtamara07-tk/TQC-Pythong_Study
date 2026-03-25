"""
TQC Practice Exercise 01: Student Score System
TQC 練習題 01：學生成績系統

Category: Dictionaries (第六類：字典操作)

題目說明：
Read n student records (name and score), store in a dictionary.
Then output:
1. All student scores
2. The student with the highest score
3. The student with the lowest score
4. The class average

請讀取 n 位學生的姓名和分數，存入字典，然後輸出以上四項。

Example Input / 輸入範例：
3
Alice 92
Bob 78
Charlie 85
Expected Output / 預期輸出：
All scores:
  Alice: 92
  Bob: 78
  Charlie: 85
Highest: Alice (92)
Lowest: Bob (78)
Average: 85.00
"""

# Write your code below / 請在下方撰寫程式碼
# ============================================

n = int(input())
students = {}

for _ in range(n):
    parts = input().split()
    name = parts[0]
    score = int(parts[1])
    students[name] = score

# Display all scores
print("All scores:")
for name, score in students.items():
    print(f"  {name}: {score}")

# Highest and lowest
best = max(students, key=students.get)
worst = min(students, key=students.get)
print(f"Highest: {best} ({students[best]})")
print(f"Lowest: {worst} ({students[worst]})")

# Average
avg = sum(students.values()) / len(students)
print(f"Average: {avg:.2f}")

# ============================================
