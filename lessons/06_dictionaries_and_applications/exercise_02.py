"""
TQC Practice Exercise 02: Word Frequency Counter
TQC 練習題 02：文字頻率統計

Category: Dictionaries / Strings (第六類：字典與字串)

題目說明：
Read a line of text and count the frequency of each word.
Output the words sorted by frequency (highest first).
If two words have the same frequency, sort alphabetically.

請讀取一行文字，計算每個單字的頻率，按頻率由高到低排序輸出。

Example Input / 輸入範例：
the cat sat on the mat the cat
Expected Output / 預期輸出：
the: 3
cat: 2
mat: 1
on: 1
sat: 1
"""

# Write your code below / 請在下方撰寫程式碼
# ============================================

text = input()
words = text.lower().split()

# Count frequency
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

# Sort by frequency (desc), then alphabetically (asc)
sorted_words = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

for word, count in sorted_words:
    print(f"{word}: {count}")

# ============================================
