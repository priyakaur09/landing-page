# Simple Password Complexity Checker for Portfolio Practice
def check_password(password):
 # Check length
  if len(password) < 8:
    return "Weak: Must be at least 8 characters long."
 # Check for numbers
  if not any(char.isdigit() for char in password):
  return "Medium: Add numbers to make it stronger."
  return "Strong: Password meets portfolio criteria!"
  # Test the function
  user_input = "Sec12345"
  print("Testing password status:")
  print(check_password(user_input))
