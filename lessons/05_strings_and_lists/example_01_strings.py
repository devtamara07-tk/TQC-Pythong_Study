"""
Lesson 05 - Example 01: String Operations
第五課 - 範例一：字串操作

Strings are sequences of characters with many built-in methods.
字串是字元序列，有許多內建方法。
"""

# String creation / 字串建立
s1 = "Hello, World!"
s2 = 'Python Programming'
s3 = """This is a
multi-line string."""

print(f"s1: {s1}")
print(f"s2: {s2}")
print(f"s3: {s3}")

# String indexing and slicing / 字串索引和切片
print("\n--- Indexing & Slicing / 索引和切片 ---")
text = "Python"
print(f"text[0] = '{text[0]}'")       # First character
print(f"text[-1] = '{text[-1]}'")     # Last character
print(f"text[0:3] = '{text[0:3]}'")   # Slice: Pyt
print(f"text[::2] = '{text[::2]}'")   # Every 2nd char: Pto
print(f"text[::-1] = '{text[::-1]}'") # Reversed: nohtyP

# String methods / 字串方法
print("\n--- String Methods / 字串方法 ---")
message = "  Hello, Python World!  "
print(f"upper(): '{message.upper()}'")
print(f"lower(): '{message.lower()}'")
print(f"strip(): '{message.strip()}'")
print(f"replace(): '{message.replace('Python', 'TQC')}'")
print(f"split(): {message.split()}")
print(f"find('Python'): {message.find('Python')}")
print(f"count('l'): {message.count('l')}")
print(f"startswith('  He'): {message.startswith('  He')}")
print(f"isdigit(): {'12345'.isdigit()}")
print(f"isalpha(): {'Hello'.isalpha()}")

# String formatting / 字串格式化
print("\n--- String Formatting / 字串格式化 ---")
name = "Alice"
score = 95.678
print(f"f-string: {name} scored {score:.1f}")
print("format(): {} scored {:.1f}".format(name, score))
print("%%-format: %s scored %.1f" % (name, score))

# Join / 連接
words = ["I", "love", "Python"]
sentence = " ".join(words)
print(f"\njoin: {sentence}")
