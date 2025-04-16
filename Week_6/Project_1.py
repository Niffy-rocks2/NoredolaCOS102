import tkinter as tk
from tkinter import messagebox

def calculate_charge():
    try:
        # Get user inputs
        location = location_var.get()
        weight = float(weight_entry.get())
        
        # Initialize base charge
        charge = 0
        
        # Determine charge based on location and weight
        if location.lower() == "ibeju-lekki":
            if weight >= 10:
                charge = 5000
            else:
                charge = 3500
        elif location.lower() == "epe":
            if weight >= 10:
                charge = 10000
            else:
                charge = 5000
        else:
            messagebox.showerror("Error", "Please enter either 'Ibeju-Lekki' or 'Epe' as the location.")
            return
        
        # Display the result
        result_label.config(text=f"Delivery Charge: N{charge:,}")
    
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid weight (numeric value).")

# Create the main window
window = tk.Tk()
window.title("Simi Services Delivery Calculator")
window.geometry("800x600")

# Location selection
location_label = tk.Label(window, text="Select Location:")
location_label.pack(pady=5)

location_var = tk.StringVar(value="Ibeju-Lekki")
tk.Radiobutton(window, text="Ibeju-Lekki", variable=location_var, value="Ibeju-Lekki").pack()
tk.Radiobutton(window, text="Epe", variable=location_var, value="Epe").pack()

# Weight input
weight_label = tk.Label(window, text="Enter Package Weight (kg):")
weight_label.pack(pady=5)

weight_entry = tk.Entry(window)
weight_entry.pack()

# Calculate button
calc_button = tk.Button(window, text="Calculate Charge", command=calculate_charge)
calc_button.pack(pady=10)

# Result label
result_label = tk.Label(window, text="Delivery Charge: N0")
result_label.pack(pady=10)

# Start the application
window.mainloop()