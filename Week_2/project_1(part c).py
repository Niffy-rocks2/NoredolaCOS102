def swap_ages():
    name1 = input("Enter first person's name: ")
    age1 = int(input(f"Enter {name1}'s age: "))
    
    name2 = input("Enter second person's name: ")
    age2 = int(input(f"Enter {name2}'s age: "))
    
    age1, age2 = age2, age1  # Swapping
    
    print(f"{name1} is now {age1} years old")
    print(f"{name2} is now {age2} years old")

swap_ages()
