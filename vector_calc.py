import tkinter as tk
from tkinter import messagebox
import math

# Create main window
root = tk.Tk()
root.title("Vector Calculator")
root.geometry("400x400")  # Adjust window size for better fit

# Define StringVar variables for storing results
dotproduct_val = tk.StringVar()
angle_val = tk.StringVar()
projection_val = tk.StringVar()
crossproduct_x_val = tk.StringVar()
crossproduct_y_val = tk.StringVar()
crossproduct_z_val = tk.StringVar()

# Function to extract values from entries
def ExtractVals():
    try:
        Ax, Ay, Az = float(Ax_entry.get()), float(Ay_entry.get()), float(Az_entry.get())
        Bx, By, Bz = float(Bx_entry.get()), float(By_entry.get()), float(Bz_entry.get())
        return (Ax, Ay, Az, Bx, By, Bz)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for vectors.")
        return None
# Function to compute Dot Product
def DotProduct(vals):
    Ax, Ay, Az, Bx, By, Bz = vals
    result = Ax * Bx + Ay * By + Az * Bz
    dotproduct_val.set(f"{result:.2f}")

# Function to compute Angle between vectors
def AngleBetweenVectors(vals):
    Ax, Ay, Az, Bx, By, Bz = vals
    mag_A = math.sqrt(Ax**2 + Ay**2 + Az**2)
    mag_B = math.sqrt(Bx**2 + By**2 + Bz**2)

    if mag_A == 0 or mag_B == 0:
        messagebox.showerror("Math Error", "Cannot calculate angle with zero vector.")
        return

    dot_product = Ax * Bx + Ay * By + Az * Bz
    angle_rad = math.acos(dot_product / (mag_A * mag_B))
    angle_deg = math.degrees(angle_rad)
    angle_val.set(f"{angle_deg:.2f}°")

# Function to compute Projection
def Projection(vals):
    Ax, Ay, Az, Bx, By, Bz = vals
    dot_product = Ax * Bx + Ay * By + Az * Bz
    mag_B_squared = Bx**2 + By**2 + Bz**2

    if mag_B_squared == 0:
        messagebox.showerror("Math Error", "Cannot project onto a zero vector.")
        return

    scalar_proj = dot_product / math.sqrt(mag_B_squared)
    projection_val.set(f"{scalar_proj:.2f}")

# Function to compute Cross Product
def CrossProduct(vals):
    Ax, Ay, Az, Bx, By, Bz = vals
    res_x = Ay * Bz - Az * By
    res_y = Az * Bx - Ax * Bz
    res_z = Ax * By - Ay * Bx

    # Update Tkinter variables
    crossproduct_x_val.set(f"{res_x:.2f}")
    crossproduct_y_val.set(f"{res_y:.2f}")
    crossproduct_z_val.set(f"{res_z:.2f}")

# Main function to handle calculations
def func_main():
    vals = ExtractVals()
    if vals:
        DotProduct(vals)
        AngleBetweenVectors(vals)
        Projection(vals)
        CrossProduct(vals)

# UI Components
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(anchor="w")  # Align entire frame to the left

# Vector A Inputs
tk.Label(frame, text="Vector A:", font=("Arial", 12, "bold")).grid(row=0, column=0, pady=5, sticky="w")
Ax_entry = tk.Entry(frame, width=5)
Ay_entry = tk.Entry(frame, width=5)
Az_entry = tk.Entry(frame, width=5)
Ax_entry.grid(row=0, column=1, padx=2)
Ay_entry.grid(row=0, column=2, padx=2)
Az_entry.grid(row=0, column=3, padx=2)

# Vector B Inputs
tk.Label(frame, text="Vector B:", font=("Arial", 12, "bold")).grid(row=1, column=0, pady=5, sticky="w")
Bx_entry = tk.Entry(frame, width=5)
By_entry = tk.Entry(frame, width=5)
Bz_entry = tk.Entry(frame, width=5)
Bx_entry.grid(row=1, column=1, padx=2)
By_entry.grid(row=1, column=2, padx=2)
Bz_entry.grid(row=1, column=3, padx=2)

# Calculate Button
tk.Button(frame, text="Calculate", font=("Arial", 12), command=func_main).grid(row=2, column=0, columnspan=4, pady=10, sticky="w")

# Results Section
results_frame = tk.Frame(root, padx=20, pady=10)
results_frame.pack(anchor="w")  # Align results to the left

tk.Label(results_frame, text="Results:", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3, sticky="w")

tk.Label(results_frame, text="Dot Product:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=5)
tk.Label(results_frame, textvariable=dotproduct_val, font=("Arial", 12)).grid(row=1, column=1, sticky="w")

tk.Label(results_frame, text="Angle (degrees):", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=5)
tk.Label(results_frame, textvariable=angle_val, font=("Arial", 12)).grid(row=2, column=1, sticky="w")

tk.Label(results_frame, text="Projection of A onto B:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=5)
tk.Label(results_frame, textvariable=projection_val, font=("Arial", 12)).grid(row=3, column=1, sticky="w")

# Cross Product Section
tk.Label(results_frame, text="Cross Product:", font=("Arial", 12, "bold")).grid(row=4, column=0, sticky="w", padx=5)

tk.Label(results_frame, text="X:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=5)  
tk.Label(results_frame, textvariable=crossproduct_x_val, font=("Arial", 12)).grid(row=5, column=1, sticky="w")

tk.Label(results_frame, text="Y:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=5)  
tk.Label(results_frame, textvariable=crossproduct_y_val, font=("Arial", 12)).grid(row=6, column=1, sticky="w")

tk.Label(results_frame, text="Z:", font=("Arial", 12)).grid(row=7, column=0, sticky="w", padx=5)  
tk.Label(results_frame, textvariable=crossproduct_z_val, font=("Arial", 12)).grid(row=7, column=1, sticky="w")

root.mainloop()
