from tkinter import *
from tkinter import ttk

# ---------------- CONSTANTS ---------------- #
DECIMAL = {
    "Byte": 1,
    "KB": 1000,
    "MB": 1000**2,
    "GB": 1000**3,
    "TB": 1000**4
}

BINARY = {
    "Byte": 1,
    "KB": 1024,
    "MB": 1024**2,
    "GB": 1024**3,
    "TB": 1024**4
}

MILE = 1.609344

# ---------------- CONVERT ---------------- #
def convert():
    text = input_entry.get().strip()
    if not text:
        output_label.config(text="0")
        return
    try:
        value = float(text)
    except:
        output_label.config(text="Invalid")
        return

    cat = category_var.get()
    mode = mode_var.get()
    f = from_var.get()
    t = to_var.get()

    # -------- DISTANCE -------- #
    if cat == "Distance":
        if f == "Miles" and t == "Km":
            result = value * MILE
        elif f == "Km" and t == "Miles":
            result = value / MILE
        else:
            result = value

    # -------- STORAGE -------- #
    elif cat == "Storage":
        bytes_val = value * DECIMAL.get(f, 1)
        if mode == "Math (Windows)":
            result = bytes_val / BINARY.get(t, 1)

        else:  
            math_val = bytes_val / BINARY.get(t, 1)
            result = math_val * 0.97   # approx system loss

    # -------- TEMPERATURE -------- #
    elif cat == "Temperature":
        if f == "Celsius" and t == "Fahrenheit":
            result = (value * 9/5) + 32

        elif f == "Fahrenheit" and t == "Celsius":
            result = (value - 32) * 5/9

        else:
            result = value

    # -------- WEIGHT -------- #
    elif cat == "Weight":
        if f == "Kg" and t == "Pound":
            result = value * 2.20462

        elif f == "Pound" and t == "Kg":
            result = value / 2.20462

        else:
            result = value

    # -------- SPEED -------- #
    elif cat == "Speed":
        if f == "Km/h" and t == "Mph":
            result = value / 1.609344

        elif f == "Mph" and t == "Km/h":
            result = value * 1.609344

        else:
            result = value

    else:
        result = 0

    output_label.config(text=f"{result:,.3f}")

# ---------------- UPDATE UNITS ---------------- #
def update_units(event=None):
    cat = category_var.get()
    if cat == "Distance":
        units = ["Miles", "Km"]

    elif cat == "Storage":
        units = ["Byte", "KB", "MB", "GB", "TB"]

    elif cat == "Temperature":
        units = ["Celsius", "Fahrenheit"]

    elif cat == "Weight":
        units = ["Kg", "Pound"]

    elif cat == "Speed":
        units = ["Km/h", "Mph"]

    else:
        units = []

    from_box["values"] = units
    to_box["values"] = units

    if units:
        from_var.set(units[0])
        to_var.set(units[-1])

# ---------------- UI ---------------- #
root = Tk()
root.title("Clear Windows Converter")
root.geometry("460x450")
root.resizable(False, False)
root.config(padx=20, pady=20)

Label(root, text="UNIT CONVERTER", font=("Arial", 18, "bold")).pack(pady=6)
Label(root, text="Math vs Real PC Display", font=("Arial", 10)).pack()

# -------- MODE -------- #
mode_var = StringVar()
mode_box = ttk.Combobox(
    root,
    textvariable=mode_var,
    state="readonly",
    width=25,
    values=[
        "Math (Windows)",
        "PC Display (Estimated)"
    ]
)

mode_box.current(0)
mode_box.pack(pady=6)

# -------- CATEGORY -------- #
category_var = StringVar()
category_box = ttk.Combobox(
    root,
    textvariable=category_var,
    state="readonly",
    width=25,
    values=[
        "Distance",
        "Storage",
        "Temperature",
        "Weight",
        "Speed"
    ]
)

category_box.current(1)
category_box.pack(pady=6)
category_box.bind("<<ComboboxSelected>>", update_units)

# -------- INPUT -------- #
input_entry = Entry(
    root,
    font=("Arial", 14),
    justify="center",
    width=22
)

input_entry.pack(pady=10)
input_entry.focus()

# -------- FROM / TO -------- #
frame = Frame(root)
frame.pack(pady=5)

from_var = StringVar()
to_var = StringVar()

from_box = ttk.Combobox(frame, textvariable=from_var, state="readonly", width=12)
to_box = ttk.Combobox(frame, textvariable=to_var, state="readonly", width=12)

from_box.grid(row=0, column=0, padx=6)
Label(frame, text="→", font=("Arial", 12, "bold")).grid(row=0, column=1)
to_box.grid(row=0, column=2, padx=6)

# -------- BUTTONS -------- #
btn = Frame(root)
btn.pack(pady=15)
Button(btn, text="Convert", width=12, bg="green", fg="white",
       command=convert).grid(row=0, column=0, padx=8)

Button(btn, text="Clear", width=12, bg="red", fg="white",
       command=lambda: output_label.config(text="0")).grid(row=0, column=1, padx=8)

# -------- OUTPUT -------- #
output_label = Label(
    root,
    text="0",
    font=("Arial", 16, "bold"),
    bg="#f0f0f0",
    width=26,
    height=2,
    relief="ridge",
    bd=2,
    anchor="e",
    padx=10
)

output_label.pack(pady=15)
update_units()
root.mainloop()