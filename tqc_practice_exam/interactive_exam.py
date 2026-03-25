"""
TQC Python Practice Exam - Interactive Test
TQC Python 練習考試 - 互動測驗

This is an interactive version where YOU write the code!
這是互動版本，由你來寫程式！

Each question gives you a problem to solve.
每一題給你一個要解決的問題。
"""


def run_test(question_num, description, test_func, expected):
    """Run a single test case"""
    print(f"\nQ{question_num}: {description}")
    try:
        result = test_func()
        if result == expected:
            print(f"  ✅ CORRECT! Output: {result}")
            return 1
        else:
            print(f"  ❌ WRONG. Got: {result}, Expected: {expected}")
            return 0
    except Exception as e:
        print(f"  ❌ ERROR: {e}")
        return 0


print("=" * 60)
print("  TQC Interactive Practice Exam")
print("  TQC 互動練習考試")
print("=" * 60)
print()
print("Complete each function below to pass the exam!")
print("完成以下每個函式來通過考試！")
print()

score = 0

# ═══════════════════════════════════════════════════════════
# EDIT THESE FUNCTIONS TO MAKE THE TESTS PASS!
# 修改這些函式來讓測試通過！
# ═══════════════════════════════════════════════════════════


# Q1: Return the sum of all numbers from 1 to n
# 回傳 1 到 n 的總和
def sum_to_n(n):
    # TODO: Write your code here / 在此撰寫程式碼
    pass


# Q2: Return True if n is even, False if odd
# n 是偶數回傳 True，奇數回傳 False
def is_even(n):
    # TODO: Write your code here
    pass


# Q3: Return the factorial of n (n!)
# 回傳 n 的階乘
def my_factorial(n):
    # TODO: Write your code here
    pass


# Q4: Return a list of all even numbers from 1 to n
# 回傳 1 到 n 之間的所有偶數串列
def even_numbers(n):
    # TODO: Write your code here
    pass


# Q5: Return the string reversed
# 回傳反轉的字串
def reverse_string(s):
    # TODO: Write your code here
    pass


# Q6: Return the number of vowels in a string
# 回傳字串中母音字母的數量
def count_vowels(s):
    # TODO: Write your code here
    pass


# Q7: Return the max value in a list without using max()
# 不使用 max()，回傳串列中的最大值
def find_max(lst):
    # TODO: Write your code here
    pass


# Q8: Return True if the string is a palindrome
# 若字串是回文，回傳 True
def is_palindrome(s):
    # TODO: Write your code here
    pass


# ═══════════════════════════════════════════════════════════
# TESTS - DO NOT MODIFY BELOW THIS LINE
# 測試 - 請勿修改以下內容
# ═══════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("  Running Tests... / 執行測試中...")
print("=" * 60)

score += run_test(1, "Sum of 1 to 100", lambda: sum_to_n(100), 5050)
score += run_test(2, "Is 42 even?", lambda: is_even(42), True)
score += run_test(3, "5! = ?", lambda: my_factorial(5), 120)
score += run_test(4, "Even numbers 1-10", lambda: even_numbers(10), [2, 4, 6, 8, 10])
score += run_test(5, "Reverse 'Hello'", lambda: reverse_string("Hello"), "olleH")
score += run_test(6, "Vowels in 'Hello World'", lambda: count_vowels("Hello World"), 3)
score += run_test(7, "Max of [3,7,1,9,4]", lambda: find_max([3, 7, 1, 9, 4]), 9)
score += run_test(8, "Is 'racecar' palindrome?", lambda: is_palindrome("racecar"), True)

total = 8
print("\n" + "=" * 60)
print(f"  Score: {score}/{total} ({score/total*100:.0f}%)")
print("=" * 60)

if score == total:
    print("  🎉 All tests passed! You're ready for the TQC exam!")
elif score == 0:
    print("  📝 Fill in the TODO functions and run again!")
    print("  📝 填寫 TODO 函式後再次執行！")
else:
    print(f"  📚 {score} correct! Keep working on the rest!")
