"""
Lesson 05 - Example 03: Comprehensions and Tuples
第五課 - 範例三：推導式與元組

Powerful Pythonic ways to create sequences.
強大的 Python 風格序列建立方式。
"""

# List comprehension / 串列推導式
print("--- List Comprehensions / 串列推導式 ---")

# Basic / 基本
squares = [x ** 2 for x in range(1, 6)]
print(f"Squares: {squares}")

# With condition / 帶條件
evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Evens: {evens}")

# With transformation / 帶轉換
words = ["hello", "world", "python"]
upper_words = [w.upper() for w in words]
print(f"Uppercased: {upper_words}")

# Nested comprehension (2D list) / 巢狀推導式
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"Matrix: {matrix}")

# Tuples (immutable lists) / 元組（不可修改的串列）
print("\n--- Tuples / 元組 ---")
point = (3, 4)
colors = ("red", "green", "blue")

print(f"Point: {point}")
print(f"x={point[0]}, y={point[1]}")

# Tuple unpacking / 元組解構
x, y = point
print(f"Unpacked: x={x}, y={y}")

# Tuple as function return / 元組作為函式回傳值
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

data = [10, 20, 30, 40, 50]
minimum, maximum, average = get_stats(data)
print(f"\nStats of {data}:")
print(f"  Min: {minimum}, Max: {maximum}, Avg: {average}")

# Converting between list and tuple / 串列和元組互轉
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
back_to_list = list(my_tuple)
print(f"\nList: {my_list} -> Tuple: {my_tuple} -> List: {back_to_list}")
