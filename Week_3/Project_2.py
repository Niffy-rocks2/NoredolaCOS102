# Program to calculate Annual Tax Revenue (ATR) based on experience and age

def calculate_atr(experience, age):
    if experience > 25 and age >= 55:
        return 5600000  # ATR for staff with >25 years experience and age >= 55
    elif experience > 20 and age >= 45:
        return 4480000  # ATR for staff with >20 years experience and age >= 45
    elif experience > 10 and age >= 35:
        return 1500000  # ATR for staff with >10 years experience and age >= 35
    else:
        return 550000  # ATR for staff with <10 years experience and age < 35

# Taking user input
experience = int(input("Enter years of experience: "))
age = int(input("Enter age: "))

# Calculate ATR
atr = calculate_atr(experience, age)

# Display result
print(f"Annual Tax Revenue (ATR) for the staff: N{atr:,}")
