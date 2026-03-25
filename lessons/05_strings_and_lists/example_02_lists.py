"""
Lesson 05 - Example 02: List Operations
第五課 - 範例二：串列操作

Lists are ordered, mutable collections.
串列是有序的、可修改的集合。
"""

# Creating lists / 建立串列
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []

print(f"fruits: {fruits}")
print(f"numbers: {numbers}")
print(f"mixed: {mixed}")

# Accessing elements / 存取元素
print("\n--- Accessing Elements / 存取元素 ---")
print(f"fruits[0]: {fruits[0]}")
print(f"fruits[-1]: {fruits[-1]}")
print(f"numbers[1:3]: {numbers[1:3]}")

# Modifying lists / 修改串列
print("\n--- Modifying Lists / 修改串列 ---")
fruits.append("date")          # Add to end
print(f"After append: {fruits}")

fruits.insert(1, "blueberry")  # Insert at index
print(f"After insert: {fruits}")

fruits.remove("banana")        # Remove by value
print(f"After remove: {fruits}")

popped = fruits.pop()          # Remove last
print(f"After pop: {fruits}, popped: {popped}")

# List operations / 串列運算
print("\n--- List Operations / 串列運算 ---")
a = [1, 2, 3]
b = [4, 5, 6]
print(f"Concatenation: {a + b}")
print(f"Repetition: {a * 3}")
print(f"Length: {len(a)}")
print(f"Sum: {sum(a)}")
print(f"Min: {min(a)}, Max: {max(a)}")
print(f"3 in a: {3 in a}")

# Sorting / 排序
print("\n--- Sorting / 排序 ---")
scores = [85, 92, 78, 95, 60, 88]
print(f"Original: {scores}")
print(f"sorted(): {sorted(scores)}")
print(f"sorted(reverse): {sorted(scores, reverse=True)}")

scores.sort()
print(f"After .sort(): {scores}")

scores.reverse()
print(f"After .reverse(): {scores}")
