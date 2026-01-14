import re

def check_password_strength(password):
    score = 0
    feedback  = []
    
    if len(password) >= 8:
        score += 2
    else:
        feedback.append("Use at least 8 characters")
        
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add an uppercase letter")
    
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add a lowercase letter")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add a number")
        
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add a special character")
        
    if score <= 3:
        strength = "Weak"
    elif score <= 5:
        strength = "Medium"
    else:
        strength = "Strong"
        
    return strength, score, feedback

password = input("Enter password to check: ")
strength, score, feedback = check_password_strength(password)

print("\nPassword Strength: ", strength)
print("Score:",score,"/6")

if feedback:
    print("\nSuggestions:")
    for f in feedback:
        print("->", f)