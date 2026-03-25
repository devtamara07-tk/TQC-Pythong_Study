"""
TQC Practice Exercise 03: Password Validator
TQC 練習題 03：密碼驗證器

Category: Functions (第四類：函式)

題目說明：
Write a function validate_password(password) that checks if a password
meets the following criteria:
1. At least 8 characters long
2. Contains at least one uppercase letter
3. Contains at least one lowercase letter
4. Contains at least one digit

Return True if valid, False otherwise.
Also print which rules fail.

請撰寫函式驗證密碼是否符合以上四個規則。

Example Input / 輸入範例：MyPass1
Expected Output / 預期輸出：
Rule 1 (length >= 8): FAIL
Rule 2 (uppercase): PASS
Rule 3 (lowercase): PASS
Rule 4 (digit): PASS
Password is INVALID.
"""

# Write your code below / 請在下方撰寫程式碼
# ============================================


def validate_password(password):
    rules = {
        "Rule 1 (length >= 8)": len(password) >= 8,
        "Rule 2 (uppercase)": any(c.isupper() for c in password),
        "Rule 3 (lowercase)": any(c.islower() for c in password),
        "Rule 4 (digit)": any(c.isdigit() for c in password),
    }

    all_pass = True
    for rule, passed in rules.items():
        status = "PASS" if passed else "FAIL"
        print(f"{rule}: {status}")
        if not passed:
            all_pass = False

    return all_pass


password = input()
if validate_password(password):
    print("Password is VALID.")
else:
    print("Password is INVALID.")

# ============================================
