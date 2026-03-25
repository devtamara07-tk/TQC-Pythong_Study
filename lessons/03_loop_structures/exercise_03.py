"""
TQC Practice Exercise 03: Prime Number Check
TQC 練習題 03：質數判斷

Category: Loop Structure (第三類：迴圈結構)

題目說明：
Read an integer n, find and print all prime numbers from 2 to n.
Also print the count of prime numbers found.
請讀取整數 n，找出並印出 2 到 n 之間的所有質數。
同時印出質數的個數。

Example Input / 輸入範例：20
Expected Output / 預期輸出：
2 3 5 7 11 13 17 19
Total primes: 8
"""

# Write your code below / 請在下方撰寫程式碼
# ============================================

n = int(input())
count = 0

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
        count += 1

print(f"\nTotal primes: {count}")

# ============================================
# Think: Why do we only check up to sqrt(n)?
# 思考：為什麼我們只需要檢查到 sqrt(n)？
