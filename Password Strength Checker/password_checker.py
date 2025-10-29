# Simple Password Strength Checker

# Ask the user for a password
password = input("Enter a password to check: ")

score = 0       # Start score at 0
feedback = []   # Store suggestions

# Check password length
if len(password) >= 8:
    score += 1
else:
    feedback.append("Make it at least 8 characters long.")

# Check for uppercase letters
if any(a.isupper() for a in password):
    score += 1
else:
    feedback.append("Add at least one uppercase letter.")

# Check for lowercase letters
if any(a.islower() for a in password):
    score += 1
else:
    feedback.append("Add at least one lowercase letter.")

# Check for numbers
if any(a.isdigit() for a in password):
    score += 1
else:
    feedback.append("Add at least one number.")

# Check for special characters
special_characters = "!@#$%^&*()-_+=[]{}|;:'\",.<>?/`~"
if any(a in special_characters for a in password):
    score += 1
else:
    feedback.append("Add at least one special character (e.g., !, @, #).")

# Show the results
print(f"\nPassword Strength: {score}/5")
if score == 5:
    print("Excellent! Your password is strong.")
else:
    print("Suggestions to improve your password:")
    for tip in feedback:
        print("- " + tip)
