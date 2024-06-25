
import tkinter as tk
from tkinter import ttk

def create_form():
    root = tk.Tk()
    root.title("Testform")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Label(frame, text="Name").grid(row=0, column=0, sticky=tk.W, pady=2)
    name_entry = ttk.Entry(frame)
    name_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=2)

    ttk.Label(frame, text="Password").grid(row=1, column=0, sticky=tk.W, pady=2)
    password_entry = ttk.Entry(frame, show="*")
    password_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=2)

    ttk.Label(frame, text="Gender").grid(row=2, column=0, sticky=tk.W, pady=2)
    gender_frame = ttk.Frame(frame)
    gender_frame.grid(row=2, column=1, sticky=(tk.W, tk.E))
    gender_var = tk.StringVar()
    ttk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").grid(row=0, column=0, sticky=tk.W)
    ttk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").grid(row=0, column=1, sticky=tk.W)

    ttk.Label(frame, text="Continent").grid(row=3, column=0, sticky=tk.W, pady=2)
    continent_combo = ttk.Combobox(frame, values=["Please select...", "Africa", "Asia", "Europe", "North America", "South America", "Australia", "Antarctica"])
    continent_combo.current(0)
    continent_combo.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=2)

    ttk.Label(frame, text="Meals").grid(row=4, column=0, sticky=tk.W, pady=2)
    meals_frame = ttk.Frame(frame)
    meals_frame.grid(row=4, column=1, sticky=(tk.W, tk.E))
    breakfast_var = tk.BooleanVar()
    lunch_var = tk.BooleanVar()
    dinner_var = tk.BooleanVar()
    ttk.Checkbutton(meals_frame, text="breakfast", variable=breakfast_var).grid(row=0, column=0, sticky=tk.W)
    ttk.Checkbutton(meals_frame, text="lunch", variable=lunch_var).grid(row=0, column=1, sticky=tk.W)
    ttk.Checkbutton(meals_frame, text="dinner", variable=dinner_var).grid(row=0, column=2, sticky=tk.W)

    ttk.Label(frame, text="Remark").grid(row=5, column=0, sticky=tk.W, pady=2)
    remark_text = tk.Text(frame, height=5, width=40)
    remark_text.grid(row=5, column=1, sticky=(tk.W, tk.E), pady=2)

    button_frame = ttk.Frame(frame)
    button_frame.grid(row=6, column=1, sticky=(tk.E, tk.W))
    ttk.Button(button_frame, text="Send").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
    ttk.Button(button_frame, text="Cancel").grid(row=0, column=1, padx=5, pady=5, sticky=tk.E)

    root.mainloop()

create_form()