# Financial Calculations Program

def simple_interest(P, R, T):
    """Calculate Simple Interest"""
    A = P * (1 + (R / 100) * T)
    return A

def compound_interest(P, R, n, t):
    """Calculate Compound Interest"""
    A = P * (1 + (R / n))**(n * t)
    return A

def annuity_plan(PMT, R, n, t):
    """Calculate Annuity Plan"""
    r_n = R / n
    A = PMT * (((1 + r_n) ** (n * t) - 1) / r_n)
    return A

# User input
print("Choose calculation type:")
print("1. Simple Interest")
print("2. Compound Interest")
print("3. Annuity Plan")

choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    P = float(input("Enter Principal (P): "))
    R = float(input("Enter Rate of Interest (R in %): "))
    T = float(input("Enter Time Period (T in years): "))
    result = simple_interest(P, R, T)
    print(f"Simple Interest Amount: {result:.2f}")

elif choice == 2:
    P = float(input("Enter Principal (P): "))
    R = float(input("Enter Rate of Interest (R in %): ")) / 100
    n = int(input("Enter Compounding Frequency per year (n): "))
    t = float(input("Enter Time Period (T in years): "))
    result = compound_interest(P, R, n, t)
    print(f"Compound Interest Amount: {result:.2f}")

elif choice == 3:
    PMT = float(input("Enter Payment Amount (PMT): "))
    R = float(input("Enter Rate of Interest (R in %): ")) / 100
    n = int(input("Enter Compounding Frequency per year (n): "))
    t = float(input("Enter Time Period (T in years): "))
    result = annuity_plan(PMT, R, n, t)
    print(f"Annuity Plan Amount: {result:.2f}")

else:
    print("Invalid choice. Please enter 1, 2, or 3.")
