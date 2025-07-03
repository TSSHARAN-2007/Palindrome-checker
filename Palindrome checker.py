# Palindrome checker
w = input("Enter the value: ").strip()
n = w.lower()
u = n[::-1]
if n==u:
    print("The given value is a palindrome.")
else:
    print("The given value is not a palindrome.")    