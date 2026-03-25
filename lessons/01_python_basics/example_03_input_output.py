"""
Lesson 01 - Example 03: Input and Output
第一課 - 範例三：輸入與輸出

Learn how to interact with users using input() and print().
學習如何使用 input() 和 print() 與使用者互動。
"""

# Simple greeting program / 簡單的打招呼程式
print("=" * 40)
print("  Welcome to the Greeting Program!")
print("  歡迎來到打招呼程式！")
print("=" * 40)

# Get user's name / 取得使用者姓名
name = input("What is your name? / 你的名字是？ ")

# Get user's age (convert string to integer)
# 取得使用者年齡（將字串轉為整數）
age_str = input("How old are you? / 你幾歲？ ")
age = int(age_str)

# Calculate birth year / 計算出生年
birth_year = 2025 - age

# Display results using f-string / 使用 f-string 顯示結果
print("\n--- Your Information / 你的資訊 ---")
print(f"Name / 姓名: {name}")
print(f"Age / 年齡: {age}")
print(f"Approximate birth year / 大約出生年: {birth_year}")
print(f"Hello {name}! You were born around {birth_year}.")
print(f"你好 {name}！你大約出生於 {birth_year} 年。")
