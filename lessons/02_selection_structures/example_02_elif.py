"""
Lesson 02 - Example 02: Multiple Conditions with elif
第二課 - 範例二：使用 elif 的多重條件

Use elif when you have more than two possible outcomes.
當有超過兩種結果時使用 elif。
"""

# Score to grade conversion / 分數轉等級
score = int(input("Enter your score (0-100) / 請輸入你的分數: "))

if score >= 90:
    grade = "A (優秀/Excellent)"
elif score >= 80:
    grade = "B (良好/Good)"
elif score >= 70:
    grade = "C (中等/Average)"
elif score >= 60:
    grade = "D (及格/Pass)"
else:
    grade = "F (不及格/Fail)"

print(f"Score: {score} -> Grade: {grade}")
print(f"分數: {score} -> 等級: {grade}")

# Season checker / 季節判斷
print("\n--- Season Checker / 季節判斷 ---")
month = int(input("Enter month (1-12) / 請輸入月份: "))

if month in [3, 4, 5]:
    season = "Spring / 春天 🌸"
elif month in [6, 7, 8]:
    season = "Summer / 夏天 ☀️"
elif month in [9, 10, 11]:
    season = "Autumn / 秋天 🍂"
elif month in [12, 1, 2]:
    season = "Winter / 冬天 ❄️"
else:
    season = "Invalid month / 無效的月份"

print(f"Month {month} is in {season}")
