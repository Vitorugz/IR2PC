import tkinter as tk
from tkinter import ttk

class Interface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("IR2PC")
        self.window.geometry("350x250")
        self.window.resizable(False, False)

        self.window.wm_attributes("-topmost", 1)

        self.var_title        = tk.StringVar(value="IR2PC")
        self.var_mode         = tk.StringVar(value="Current Mode: Mouse")
        self.var_last_command = tk.StringVar(value="Last Command: ---")
        self.var_last_action  = tk.StringVar(value="Last Action: ---")

        label_title        = ttk.Label(self.window, textvariable=self.var_title,         font=("Arial", 16, "bold"))
        label_mode         = ttk.Label(self.window, textvariable=self.var_mode,          font=("Arial", 12, "bold"))
        label_last_command = ttk.Label(self.window, textvariable=self.var_last_command,  font=("Arial", 10))
        label_last_action  = ttk.Label(self.window, textvariable=self.var_last_action,   font=("Arial", 10))

        label_title.pack(pady=10)
        label_mode.pack(pady=10)
        label_last_command.pack(pady=5)
        label_last_action.pack(pady=5)

        button_quit = ttk.Button(self.window, text="Quit", command=self.window.quit)
        button_quit.pack(pady=10)

    def run(self):
        self.window.mainloop()

    def close(self):
        self.window.destroy()
