"""
Lesson 06 - Example 01: Dictionary Operations
第六課 - 範例一：字典操作

Dictionaries store key-value pairs.
字典儲存鍵值對。
"""

# Creating dictionaries / 建立字典
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "scores": [85, 92, 78]
}

print("--- Dictionary Basics / 字典基礎 ---")
print(f"Student: {student}")
print(f"Name: {student['name']}")
print(f"Age: {student.get('age')}")
print(f"Email: {student.get('email', 'N/A')}")  # Default value

# Modifying dictionaries / 修改字典
print("\n--- Modifying / 修改 ---")
student["email"] = "alice@example.com"  # Add new key
student["age"] = 21                      # Update existing
print(f"Updated: {student}")

del student["email"]                     # Delete key
print(f"After del: {student}")

# Dictionary methods / 字典方法
print("\n--- Dictionary Methods / 字典方法 ---")
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")
print(f"'name' in student: {'name' in student}")

# Iterating over dictionaries / 遍歷字典
print("\n--- Iterating / 遍歷 ---")
scores = {"Math": 90, "English": 85, "Science": 92, "History": 78}
for subject, score in scores.items():
    status = "Pass ✓" if score >= 60 else "Fail ✗"
    print(f"  {subject}: {score} ({status})")

# Dictionary comprehension / 字典推導式
print("\n--- Dictionary Comprehension / 字典推導式 ---")
squares = {x: x ** 2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Filter to only passing scores
passing = {k: v for k, v in scores.items() if v >= 85}
print(f"High scores (>=85): {passing}")
