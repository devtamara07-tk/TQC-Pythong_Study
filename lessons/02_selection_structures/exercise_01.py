"""
TQC Practice Exercise 01: Grade Checker
TQC 練習題 01：成績判定

Category: Selection Structure (第二類：選擇結構)

題目說明：
Write a program that reads a score (0-100) and outputs the grade.
If the score is invalid (< 0 or > 100), output "Invalid score".
請撰寫程式，讀取分數(0-100)並輸出等級。
若分數無效，輸出 "Invalid score"。

Grading rules / 評分規則：
  90-100 -> A
  80-89  -> B
  70-79  -> C
  60-69  -> D
  0-59   -> F

Example Input / 輸入範例：85
Expected Output / 預期輸出：B
"""

# Write your code below / 請在下方撰寫程式碼
# ============================================

score = int(input())

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# ============================================
