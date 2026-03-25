"""
TQC Practice Exercise 03: Self-Introduction Program
TQC 練習題 03：自我介紹程式

Category: Basic I/O (第一類：基本輸入輸出)

題目說明 (from Python1.pdf homework):
Write a self-introduction program that:
1. Greets the user with a welcome message
2. Asks for the user's name, hobby, and favorite animal
3. Displays a formatted self-introduction

請撰寫自我介紹程式：
1. 向使用者顯示歡迎訊息
2. 詢問使用者的姓名、興趣和最喜歡的動物
3. 顯示格式化的自我介紹

Expected Output / 預期輸出：
哈囉！請告訴我一些關於你的事情吧！
你的名字是？小明
你的一個興趣是？玩電動
你最喜歡的動物是？狗
太棒了！這是你的自我介紹：
我的名字是小明，我喜歡的興趣是玩電動，我最喜歡的動物是狗。
"""

# Write your code below / 請在下方撰寫程式碼
# ============================================

print("哈囉！請告訴我一些關於你的事情吧！")

name = input("你的名字是？")
hobby = input("你的一個興趣是？")
animal = input("你最喜歡的動物是？")

print("太棒了！這是你的自我介紹：")
print(f"我的名字是{name}，我喜歡的興趣是{hobby}，我最喜歡的動物是{animal}。")

# ============================================
# Bonus: Add more questions and make the introduction more detailed!
# 加分：加入更多問題，讓自我介紹更詳細！
