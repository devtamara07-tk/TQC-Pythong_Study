"""
Lesson 04 - Example 01: Basic Functions
第四課 - 範例一：基本函式

Functions are reusable blocks of code.
函式是可重複使用的程式碼區塊。
"""


# Defining a simple function / 定義一個簡單的函式
def greet():
    """A simple greeting function / 簡單的打招呼函式"""
    print("Hello! Welcome to Python functions!")
    print("你好！歡迎來到 Python 函式的世界！")


# Calling the function / 呼叫函式
greet()

print("-" * 40)


# Function with a parameter / 帶參數的函式
def greet_person(name):
    """Greet a specific person / 向特定的人打招呼"""
    print(f"Hello, {name}! Nice to meet you!")
    print(f"你好，{name}！很高興認識你！")


greet_person("Alice")
greet_person("Bob")

print("-" * 40)


# Function with return value / 帶回傳值的函式
def add(a, b):
    """Return the sum of two numbers / 回傳兩數之和"""
    return a + b


result = add(3, 5)
print(f"3 + 5 = {result}")
print(f"10 + 20 = {add(10, 20)}")

print("-" * 40)


# Function with default parameter / 帶預設參數的函式
def power(base, exponent=2):
    """Calculate base raised to exponent / 計算次方"""
    return base ** exponent


print(f"3^2 = {power(3)}")        # Uses default exponent=2
print(f"2^10 = {power(2, 10)}")   # Overrides default
