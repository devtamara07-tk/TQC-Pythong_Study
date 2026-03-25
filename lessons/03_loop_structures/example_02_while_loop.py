"""
Lesson 03 - Example 02: While Loops
第三課 - 範例二：While 迴圈

While loops repeat as long as a condition is True.
While 迴圈在條件為 True 時重複執行。
"""

# Basic while loop / 基本 while 迴圈
print("--- Countdown / 倒數 ---")
count = 5
while count > 0:
    print(count, end=" ")
    count -= 1
print("Go! 🚀")

# Accumulator pattern / 累加器模式
print("\n--- Sum until user enters 0 ---")
print("Enter numbers to add (0 to stop):")
total = 0
num = int(input("Number: "))
while num != 0:
    total += num
    num = int(input("Number: "))
print(f"Total sum: {total}")

# Break and continue / break 和 continue
print("\n--- break example ---")
for i in range(1, 11):
    if i == 6:
        print(f"\nFound {i}, breaking!")
        break
    print(i, end=" ")

print("\n--- continue example ---")
print("Odd numbers from 1-10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i, end=" ")
print()

# Guessing game / 猜數字遊戲
print("\n--- Number Guessing Game / 猜數字遊戲 ---")
import random
secret = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess a number (1-10) / 猜一個數字: "))
    attempts += 1
    if guess == secret:
        print(f"Correct! You got it in {attempts} attempts! / 答對了！")
        break
    elif guess < secret:
        print("Too low! / 太小了！")
    else:
        print("Too high! / 太大了！")
