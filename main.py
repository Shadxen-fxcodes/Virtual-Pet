import tkinter as tk

class Pet:
    def __init__(self, name="Fluffy"):
        self.name = name

pet = Pet()

window = tk.Tk()
window.title("Virtual Pet")
window.geometry("500x600")

name_label = tk.Label(window, text=pet.name, font=("Arial", 24))
name_label.pack(pady=10)

