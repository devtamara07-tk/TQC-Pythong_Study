"""
Lesson 01 - Example 02: Variables and Data Types
第一課 - 範例二：變數與資料型態

Variables are like containers that store data.
變數就像容器，可以儲存資料。
"""

# Integer variables / 整數變數
age = 25
year = 2025
print(f"Age: {age}, Year: {year}")
print(f"Type of age: {type(age)}")

# Float variables / 浮點數變數
height = 175.5
weight = 68.3
print(f"Height: {height} cm, Weight: {weight} kg")
print(f"Type of height: {type(height)}")

# String variables / 字串變數
name = "Alice"
greeting = '你好'
print(f"Name: {name}, Greeting: {greeting}")
print(f"Type of name: {type(name)}")

# Boolean variables / 布林變數
is_student = True
is_graduated = False
print(f"Is student: {is_student}, Is graduated: {is_graduated}")
print(f"Type of is_student: {type(is_student)}")

# Variable operations / 變數運算
print("\n--- Arithmetic Operations / 算術運算 ---")
a = 10
b = 3
print(f"{a} + {b} = {a + b}")       # Addition / 加法
print(f"{a} - {b} = {a - b}")       # Subtraction / 減法
print(f"{a} * {b} = {a * b}")       # Multiplication / 乘法
print(f"{a} / {b} = {a / b:.2f}")   # Division / 除法
print(f"{a} // {b} = {a // b}")     # Floor division / 整數除法
print(f"{a} % {b} = {a % b}")       # Modulus / 取餘數
print(f"{a} ** {b} = {a ** b}")     # Power / 次方

# Type conversion / 型態轉換
print("\n--- Type Conversion / 型態轉換 ---")
x = "100"
y = int(x)           # String to integer
z = float(x)         # String to float
print(f"String '{x}' -> int {y} -> float {z}")
