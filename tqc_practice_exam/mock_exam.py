"""
TQC Python Practice Exam - Mock Test
TQC Python 練習考試 - 模擬測驗

This simulates a TQC-style Python certification exam.
這模擬了 TQC 風格的 Python 認證考試。

The exam has 10 questions across different categories.
考試有 10 題，涵蓋不同類別。

Run this file and answer each question.
執行此檔案並回答每一題。
"""

import sys

score = 0
total = 10


def check(question_num, expected, actual, description):
    global score
    if expected == actual:
        print(f"  ✅ Q{question_num}: CORRECT - {description}")
        score += 1
    else:
        print(f"  ❌ Q{question_num}: WRONG - {description}")
        print(f"     Expected: {expected}")
        print(f"     Got: {actual}")


print("=" * 60)
print("  TQC Python Practice Exam / TQC Python 模擬考試")
print("  10 Questions / 10 題")
print("=" * 60)
print()

# ─── Category 1: Basic I/O ───────────────────────────────
print("📝 Category 1: Basic I/O / 第一類：基本輸入輸出")
print("-" * 50)

# Q1: String multiplication
print("Q1: What is the output of print('*' * 5)?")
q1 = "*" * 5
check(1, "*****", q1, "String multiplication")

# Q2: f-string
name = "Python"
version = 3
q2 = f"{name} {version}"
check(2, "Python 3", q2, "f-string formatting")

print()

# ─── Category 2: Selection Structure ─────────────────────
print("📝 Category 2: Selection Structure / 第二類：選擇結構")
print("-" * 50)

# Q3: Absolute value without abs()
def my_abs(x):
    if x < 0:
        return -x
    return x

check(3, 5, my_abs(-5), "Absolute value of -5")

# Q4: Leap year
def is_leap(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

check(4, True, is_leap(2024), "2024 is a leap year")
check(5, False, is_leap(1900), "1900 is not a leap year")

print()

# ─── Category 3: Loop Structure ──────────────────────────
print("📝 Category 3: Loop Structure / 第三類：迴圈結構")
print("-" * 50)

# Q6: Sum 1 to 100
total_sum = sum(range(1, 101))
check(6, 5050, total_sum, "Sum of 1 to 100 (Gauss)")

# Q7: Count primes under 20
def count_primes(n):
    count = 0
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count

check(7, 8, count_primes(20), "Number of primes <= 20")

print()

# ─── Category 4: Functions ───────────────────────────────
print("📝 Category 4: Functions / 第四類：函式")
print("-" * 50)

# Q8: Fibonacci
def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

check(8, 55, fib(10), "10th Fibonacci number")

print()

# ─── Category 5: Strings & Lists ────────────────────────
print("📝 Category 5: Strings & Lists / 第五類：字串與串列")
print("-" * 50)

# Q9: Reverse a string
def reverse_str(s):
    return s[::-1]

check(9, "nohtyP", reverse_str("Python"), "Reverse 'Python'")

# Q10: List comprehension - sum of even squares
result = sum(x**2 for x in range(1, 11) if x % 2 == 0)
check(10, 220, result, "Sum of squares of even numbers 1-10")

# ─── Results ─────────────────────────────────────────────
print()
print("=" * 60)
print(f"  Final Score: {score}/{total} ({score/total*100:.0f}%)")
print("=" * 60)

if score == total:
    print("  🎉 Perfect score! Excellent work!")
    print("  🎉 滿分！太棒了！")
elif score >= 7:
    print("  👍 Great job! Keep practicing!")
    print("  👍 做得好！繼續練習！")
elif score >= 5:
    print("  📚 Good effort! Review the lessons.")
    print("  📚 不錯的努力！複習一下課程。")
else:
    print("  💪 Keep studying! You'll get there!")
    print("  💪 繼續加油！你會進步的！")
