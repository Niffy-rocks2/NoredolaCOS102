# student data Representation in a Tabular Format

# Defining the data
girls = [
    ("Evelyn", 17, 5.5, 80),
    ("Jessica", 16, 6.0, 85),
    ("Somto", 17, 5.4, 70),
    ("Edith", 18, 5.9, 60),
    ("Liza", 16, 5.5, 76),
    ("Madonna", 18, 6.1, 66),
    ("Waje", 17, 5.0, 87),
    ("Tola", 20, 5.7, 95),
    ("Aisha", 19, 5.5, 50),
    ("Latifa", 17, 6.3, 49)
]

boys = [
    ("Chinedu", 19, 5.7, 74),
    ("Liam", 16, 5.9, 87),
    ("Wale", 18, 5.8, 75),
    ("Gbenga", 17, 6.1, 68),
    ("Abiola", 20, 5.5, 66),
    ("Kola", 19, 6.0, 78),
    ("Kunle", 16, 5.4, 87),
    ("George", 18, 5.8, 98),
    ("Thomas", 17, 5.7, 54),
    ("Wesley", 19, 6.1, 60)
]

# Function to display data in a formatted table
def display_table(title, data):
    print(f"\n{title}")
    print("-" * 40)
    print(f"{'Name':<10}{'Age':<5}{'Height':<7}{'Score'}")
    print("-" * 40)
    for student in data:
        name, age, height, score = student
        print(f"{name:<10}{age:<5}{height:<7}{score}")
    print("-" * 40)

# Displaying the data
display_table("Girls Data", girls)
display_table("Boys Data", boys)
