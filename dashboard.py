import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Embedded dataset (list of dictionaries)
data = [
    {"item": "Apples", "quantity": 120, "sales": 300},
    {"item": "Bananas", "quantity": 80, "sales": 200},
    {"item": "Cherries", "quantity": 50, "sales": 150},
    {"item": "Dates", "quantity": 60, "sales": 180},
    {"item": "Eggplants", "quantity": 40, "sales": 100},
]

# Function to plot sales data
def plot_sales():
    items = [d["item"] for d in data]
    sales = [d["sales"] for d in data]

    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.bar(items, sales, color="skyblue")
    ax.set_title("Item Sales")
    ax.set_xlabel("Items")
    ax.set_ylabel("Sales ($)")

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=0, columnspan=2)

# Function to plot quantity data
def plot_quantity():
    items = [d["item"] for d in data]
    quantities = [d["quantity"] for d in data]

    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.pie(quantities, labels=items, autopct="%1.1f%%", startangle=140, colors=["gold", "lightcoral", "lightskyblue", "lightgreen", "violet"])
    ax.set_title("Item Quantity Distribution")

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=0, columnspan=2)

# Main window setup
window = tk.Tk()
window.title("Super Mart Grocery Sales Dashboard")

# Buttons to switch between views
sales_button = ttk.Button(window, text="Show Sales Data", command=plot_sales)
sales_button.grid(row=0, column=0, padx=10, pady=10)

quantity_button = ttk.Button(window, text="Show Quantity Data", command=plot_quantity)
quantity_button.grid(row=0, column=1, padx=10, pady=10)

# Start with the sales plot
plot_sales()

# Run the GUI loop
window.mainloop()
