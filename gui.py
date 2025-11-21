import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np
import os

# =========================
# Load the model
# =========================
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'titanic_knn_model.pkl')
model = joblib.load(model_path)

# =========================
# Prediction function
# =========================
def predict_survival():
    try:
        name = entry_name.get().strip()
        if not name:
            messagebox.showwarning("Input error", "Please enter a name.")
            return

        pclass = int(pclass_var.get())
        sex = sex_var.get()
        sex_val = 0 if sex == "Male" else 1
        age = float(entry_age.get())

        X_new = np.array([[pclass, sex_val, age]])
        prediction = model.predict(X_new)[0]
        proba = model.predict_proba(X_new)[0]

        result_text = f"{name} is predicted to {'Survive' if prediction == 1 else 'Not Survive'} " \
                      f"({max(proba)*100:.1f}% confidence)"
        result_label.config(text=result_text)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid age.")

# =========================
# GUI Setup
# =========================
root = tk.Tk()
root.title("Titanic Survival Classifier")
root.geometry("500x400")
root.config(bg="#2e2e3f")

# Title
tk.Label(root, text="Titanic Survival Classifier", font=("Arial", 20, "bold"),
         fg="white", bg="#2e2e3f").pack(pady=(20, 15))

# Input Frame
frame = tk.Frame(root, bg="#2e2e3f")
frame.pack(pady=10, padx=30, fill="x")

label_font = ("Arial", 12, "bold")
entry_font = ("Arial", 12)

# Name
tk.Label(frame, text="Name:", fg="white", bg="#2e2e3f", font=label_font)\
    .grid(row=0, column=0, sticky="w", pady=10)
entry_name = tk.Entry(frame, font=entry_font, justify="center")
entry_name.grid(row=0, column=1, pady=10, padx=10, sticky="ew")

# Passenger Class
tk.Label(frame, text="Passenger Class:", fg="white", bg="#2e2e3f", font=label_font)\
    .grid(row=1, column=0, sticky="w", pady=10)
pclass_var = tk.StringVar(value="1")
tk.OptionMenu(frame, pclass_var, "1", "2", "3")\
    .grid(row=1, column=1, pady=10, padx=10, sticky="ew")

# Sex
tk.Label(frame, text="Sex:", fg="white", bg="#2e2e3f", font=label_font)\
    .grid(row=2, column=0, sticky="w", pady=10)
sex_var = tk.StringVar(value="Male")
tk.OptionMenu(frame, sex_var, "Male", "Female")\
    .grid(row=2, column=1, pady=10, padx=10, sticky="ew")

# Age
tk.Label(frame, text="Age:", fg="white", bg="#2e2e3f", font=label_font)\
    .grid(row=3, column=0, sticky="w", pady=10)
entry_age = tk.Entry(frame, font=entry_font, justify="center")
entry_age.grid(row=3, column=1, pady=10, padx=10, sticky="ew")

# Expand columns evenly
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=2)

# Predict Button
tk.Button(root, text="Predict Survival", command=predict_survival,
          bg="#4CAF50", fg="white", font=("Arial", 14, "bold"))\
    .pack(pady=(25, 15))

# Result Label
result_label = tk.Label(root, text="", fg="white", bg="#2e2e3f", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
