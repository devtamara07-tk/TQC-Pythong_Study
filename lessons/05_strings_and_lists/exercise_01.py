"""
TQC Practice Exercise 01: String Processing
TQC 練習題 01：字串處理

Category: Strings (第五類：字串操作)

題目說明：
Read a string from input and output:
1. The length of the string
2. The number of uppercase letters
3. The number of lowercase letters
4. The number of digits
5. The string reversed

請讀取一個字串並輸出以上五項資訊。

Example Input / 輸入範例：Hello World 123
Expected Output / 預期輸出：
Length: 15
Uppercase: 2
Lowercase: 8
Digits: 3
Reversed: 321 dlroW olleH
"""

# Write your code below / 請在下方撰寫程式碼
# ============================================

s = input()

print(f"Length: {len(s)}")
print(f"Uppercase: {sum(1 for c in s if c.isupper())}")
print(f"Lowercase: {sum(1 for c in s if c.islower())}")
print(f"Digits: {sum(1 for c in s if c.isdigit())}")
print(f"Reversed: {s[::-1]}")

# ============================================
