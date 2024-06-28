import re

def assess_password_strength(password):
    strength = 0
    feedback = ""

    # Check password length
    if len(password) < 8:
        feedback += "Password is too short. It should be at least 8 characters long.\n"
    else:
        strength += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback += "Password should contain at least one uppercase letter.\n"

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback += "Password should contain at least one lowercase letter.\n"

    # Check for numbers
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback += "Password should contain at least one number.\n"

    # Check for special characters
    if re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password):
        strength += 1
    else:
        feedback += "Password should contain at least one special character.\n"

    # Determine password strength based on the number of criteria met
    if strength == 5:
        feedback = "Strong password!"
    elif strength >= 3:
        feedback = "Medium password. Consider adding more complexity."
    else:
        feedback = "Weak password. Please try again."

    return feedback

# Test the function
password = input("Enter a password: ")
print(assess_password_strength(password))