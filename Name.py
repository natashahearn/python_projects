# Prompt the user for their name
name = input("What is your name? ")
print(f"What is your name? {name}")  # Display question and answer

# Prompt the user for their age
age = int(input("How old are you? "))
print(f"How old are you? {age}")  # Display question and answer

# Calculate birth year
current_year = 2025
birth_year = current_year - age

# Display the final greeting message
print(f"Hello {name}! You were born in {birth_year}.")
