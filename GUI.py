import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import joblib

# ============================================================
# LOAD TRAINED RANDOM FOREST MODEL
# ============================================================

model = joblib.load("random_forest_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")


# ============================================================
# PREDICTION FUNCTION
# ============================================================

def predict_price():

    try:
        # Get values from GUI
        data = {
            'Battery_power_mAh': float(battery_power.get()),
            'Bluetooh': int(float(bluetooth.get())),
            'Speed_of_microprocessor': float(clock_speed.get()),
            'Dual_sim': int(float(dual_sim.get())),
            'Front_camera': float(front_camera.get()),
            '4G': int(float(four_g.get())),
            'Internal_memeory_gb': float(internal_memory.get()),
            'Mobile_depth': float(mobile_depth.get()),
            'Mobile_weight': float(mobile_weight.get()),
            'Cores_of_processor': int(float(number_of_cores.get())),
            'Primary_camera': float(primary_camera.get()),
            'px_height': float(px_height.get()),
            'Pixel_width': float(pixel_width.get()),
            'Ram_mb': float(ram.get()),
            'Screen_height': float(screen_height.get()),
            'Screen_weight': float(screen_weight.get()),
            'talk_time': float(talk_time.get()),
            '3G': int(float(three_g.get())),
            'touch_screen': int(float(touch_screen.get())),
            'wifi': int(float(wifi.get()))
        }

        # Convert input into DataFrame
        input_data = pd.DataFrame([data])

        # Make prediction
        prediction = model.predict(input_data)

        # Convert encoded prediction back to original label
        result = label_encoder.inverse_transform(prediction)[0]

        # Display result
        result_label.config(
            text=f"Predicted Price Range: {result}"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numeric values in all fields."
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            f"Something went wrong:\n{e}"
        )


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title("Mobile Price Range Prediction System")
# Let Tkinter automatically size the window based on its contents
# root.geometry("650x850")
# root.resizable(False, False)


# ============================================================
# TITLE
# ============================================================

title = tk.Label(
    root,
    text="Mobile Price Range Prediction System",
    font=("Arial", 20, "bold")
)

title.pack(pady=15)


subtitle = tk.Label(
    root,
    text="Enter Mobile Specifications",
    font=("Arial", 12)
)

subtitle.pack(pady=5)


# ============================================================
# INPUT FRAME
# ============================================================

frame = tk.Frame(root)
frame.pack(pady=10)


# Variables
battery_power = tk.StringVar()
bluetooth = tk.StringVar(value="1")
clock_speed = tk.StringVar()
dual_sim = tk.StringVar(value="1")
front_camera = tk.StringVar()
internal_memory = tk.StringVar()
mobile_depth = tk.StringVar()
mobile_weight = tk.StringVar()
number_of_cores = tk.StringVar()
primary_camera = tk.StringVar()
px_height = tk.StringVar()
pixel_width = tk.StringVar()
ram = tk.StringVar()
screen_height = tk.StringVar()
screen_weight = tk.StringVar()
talk_time = tk.StringVar()
three_g = tk.StringVar(value="1")
four_g = tk.StringVar(value="1")
touch_screen = tk.StringVar(value="1")
wifi = tk.StringVar(value="1")


# ============================================================
# INPUT FIELDS
# ============================================================

fields = [
    ("Battery Power (mAh)", battery_power),
    ("Bluetooth (1=Yes, 0=No)", bluetooth),
    ("Clock Speed", clock_speed),
    ("Dual SIM (1=Yes, 0=No)", dual_sim),
    ("Front Camera (pixels)", front_camera),
    ("Internal Memory (GB)", internal_memory),
    ("Mobile Depth (cm)", mobile_depth),
    ("Mobile Weight (g)", mobile_weight),
    ("Number of Cores", number_of_cores),
    ("Primary Camera (pixels)", primary_camera),
    ("Pixel Height", px_height),
    ("Pixel Width", pixel_width),
    ("RAM (MB)", ram),
    ("Screen Height", screen_height),
    ("Screen Weight", screen_weight),
    ("Talk Time", talk_time),
    ("3G (1=Yes, 0=No)", three_g),
    ("4G (1=Yes, 0=No)", four_g),
    ("Touch Screen (1=Yes, 0=No)", touch_screen),
    ("WiFi (1=Yes, 0=No)", wifi)
]


for i, (label_text, variable) in enumerate(fields):
    
    # Calculate row and column to split the 20 fields into two columns of 10
    row_idx = i % 10
    col_idx = (i // 10) * 2

    label = tk.Label(
        frame,
        text=label_text,
        font=("Arial", 10),
        anchor="w",
        width=25
    )

    label.grid(
        row=row_idx,
        column=col_idx,
        padx=10,
        pady=4,
        sticky="w"
    )

    entry = tk.Entry(
        frame,
        textvariable=variable,
        width=20
    )

    entry.grid(
        row=row_idx,
        column=col_idx + 1,
        padx=10,
        pady=4
    )


# ============================================================
# PREDICT BUTTON
# ============================================================

predict_button = tk.Button(
    root,
    text="PREDICT PRICE RANGE",
    command=predict_price,
    font=("Arial", 12, "bold"),
    padx=20,
    pady=10,
    background="blue"
)

predict_button.pack(pady=15)


# ============================================================
# RESULT
# ============================================================

result_label = tk.Label(
    root,
    text="Predicted Price Range: ---",
    font=("Arial", 16, "bold")
)

result_label.pack(pady=15)


# ============================================================
# RUN APPLICATION
# ============================================================

root.mainloop()