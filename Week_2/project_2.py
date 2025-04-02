import sympy as sp

def quadratic_solver():
    print("\nQuadratic Equation: Ax² + Bx + C = 0")
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))
    
    x = sp.symbols('x')
    eq = a*x**2 + b*x + c
    roots = sp.solve(eq, x)
    
    print(f"Roots of the quadratic equation: {roots}")

def cubic_solver():
    print("\nCubic Equation: Ax³ + Bx² + Cx + D = 0")
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))
    d = float(input("Enter D: "))
    
    x = sp.symbols('x')
    eq = a*x**3 + b*x**2 + c*x + d
    roots = sp.solve(eq, x)
    
    print(f"Roots of the cubic equation: {roots}")

def quartic_solver():
    print("\nQuartic Equation: Ax⁴ + Bx³ + Cx² + Dx + E = 0")
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))
    d = float(input("Enter D: "))
    e = float(input("Enter E: "))
    
    x = sp.symbols('x')
    eq = a*x**4 + b*x**3 + c*x**2 + d*x + e
    roots = sp.solve(eq, x)
    
    print(f"Roots of the quartic equation: {roots}")

# Main program loop
while True:
    print("\nChoose the type of equation to solve:")
    print("1. Quadratic (Ax² + Bx + C = 0)")
    print("2. Cubic (Ax³ + Bx² + Cx + D = 0)")
    print("3. Quartic (Ax⁴ + Bx³ + Cx² + Dx + E = 0)")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        quadratic_solver()
    elif choice == "2":
        cubic_solver()
    elif choice == "3":
        quartic_solver()
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
