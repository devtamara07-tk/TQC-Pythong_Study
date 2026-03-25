"""
Lesson 04 - Example 02: Parameters and Returns
第四課 - 範例二：參數與回傳值

Different ways to use parameters and return values.
參數和回傳值的不同使用方式。
"""


# Multiple return values / 多個回傳值
def min_max(numbers):
    """Return the min and max of a list / 回傳列表的最小值和最大值"""
    return min(numbers), max(numbers)


data = [3, 7, 1, 9, 4, 6]
smallest, largest = min_max(data)
print(f"Data: {data}")
print(f"Min: {smallest}, Max: {largest}")

print("-" * 40)


# *args - variable number of arguments / *args - 可變數量的參數
def calculate_average(*args):
    """Calculate average of any number of values / 計算任意數量值的平均"""
    if len(args) == 0:
        return 0
    return sum(args) / len(args)


print(f"Average(1,2,3): {calculate_average(1, 2, 3):.2f}")
print(f"Average(10,20,30,40,50): {calculate_average(10, 20, 30, 40, 50):.2f}")

print("-" * 40)


# Keyword arguments / 關鍵字參數
def create_profile(name, age, city="Unknown"):
    """Create a formatted profile string / 建立格式化的個人資料"""
    return f"Name: {name}, Age: {age}, City: {city}"


print(create_profile("Alice", 25, "Taipei"))
print(create_profile("Bob", 30))               # Uses default city
print(create_profile(age=28, name="Charlie"))   # Named arguments

print("-" * 40)


# Lambda functions (anonymous functions) / Lambda 函式（匿名函式）
square = lambda x: x ** 2
add = lambda a, b: a + b

print(f"Square of 5: {square(5)}")
print(f"3 + 4 = {add(3, 4)}")

# Using lambda with sorting / 搭配排序使用 lambda
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
students_sorted = sorted(students, key=lambda s: s[1], reverse=True)
print(f"\nStudents sorted by score: {students_sorted}")
