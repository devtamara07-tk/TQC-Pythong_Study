"""
Lesson 06 - Example 02: Set Operations
第六課 - 範例二：集合操作

Sets are unordered collections of unique elements.
集合是無序的、元素唯一的集合。
"""

# Creating sets / 建立集合
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}

print("--- Set Basics / 集合基礎 ---")
print(f"fruits: {fruits}")
print(f"numbers: {numbers}")

# Duplicate removal / 去除重複
data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique = set(data)
print(f"\nOriginal list: {data}")
print(f"Unique set: {unique}")

# Set operations / 集合運算
print("\n--- Set Operations / 集合運算 ---")
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(f"A = {a}")
print(f"B = {b}")
print(f"Union (A | B): {a | b}")             # 聯集
print(f"Intersection (A & B): {a & b}")       # 交集
print(f"Difference (A - B): {a - b}")         # 差集
print(f"Symmetric diff (A ^ B): {a ^ b}")     # 對稱差集

# Set methods / 集合方法
print("\n--- Set Methods / 集合方法 ---")
s = {1, 2, 3}
s.add(4)
print(f"After add(4): {s}")
s.discard(2)
print(f"After discard(2): {s}")
print(f"3 in s: {3 in s}")

# Practical example: finding common students / 實用範例：找共同學生
print("\n--- Practical Example / 實用範例 ---")
math_class = {"Alice", "Bob", "Charlie", "Diana"}
english_class = {"Bob", "Diana", "Eve", "Frank"}
print(f"Math: {math_class}")
print(f"English: {english_class}")
print(f"Both classes: {math_class & english_class}")
print(f"Math only: {math_class - english_class}")
print(f"Either class: {math_class | english_class}")
