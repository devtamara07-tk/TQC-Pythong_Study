"""
TQC Practice Exercise 03: BMI Calculator
TQC 練習題 03：BMI 計算器

Category: Selection Structure (第二類：選擇結構)

題目說明：
Write a program that calculates BMI and determines the category.
請撰寫程式，計算 BMI 並判斷體重分類。

BMI = weight(kg) / height(m)^2

Categories / 分類：
  BMI < 18.5       -> Underweight / 過輕
  18.5 <= BMI < 24  -> Normal / 正常
  24 <= BMI < 27    -> Overweight / 過重
  BMI >= 27         -> Obese / 肥胖

Example Input / 輸入範例：
70
1.75
Expected Output / 預期輸出：
BMI = 22.86
Category: Normal
"""

# Write your code below / 請在下方撰寫程式碼
# ============================================

weight = float(input())
height = float(input())

bmi = weight / (height ** 2)

print(f"BMI = {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 24:
    print("Category: Normal")
elif bmi < 27:
    print("Category: Overweight")
else:
    print("Category: Obese")

# ============================================
