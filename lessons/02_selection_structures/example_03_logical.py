"""
Lesson 02 - Example 03: Logical Operators
第二課 - 範例三：邏輯運算子

Combine conditions using and, or, not.
使用 and、or、not 組合條件。
"""

# Logical operators / 邏輯運算子
print("--- Logical Operators / 邏輯運算子 ---")
x = True
y = False
print(f"True and False = {x and y}")     # Both must be True
print(f"True or False  = {x or y}")      # At least one True
print(f"not True       = {not x}")       # Opposite

# Practical example: Admission check / 實用範例：入場檢查
print("\n--- Admission Check / 入場檢查 ---")
age = int(input("Enter your age / 請輸入年齡: "))
has_ticket = input("Do you have a ticket? (yes/no) / 有票嗎？ ").lower()

if age >= 18 and has_ticket == "yes":
    print("Welcome! You may enter. / 歡迎入場！")
elif age < 18 and has_ticket == "yes":
    print("Sorry, you need to be 18+. / 抱歉，你需要年滿18歲。")
elif age >= 18 and has_ticket != "yes":
    print("You need a ticket to enter. / 你需要票才能入場。")
else:
    print("You need to be 18+ AND have a ticket. / 你需要年滿18歲且有票。")

# Number range check / 數字範圍檢查
print("\n--- Range Check / 範圍檢查 ---")
num = int(input("Enter a number (1-100) / 請輸入數字: "))
if 1 <= num <= 100:
    print(f"{num} is in range [1, 100] / 在範圍內")
else:
    print(f"{num} is out of range / 不在範圍內")
