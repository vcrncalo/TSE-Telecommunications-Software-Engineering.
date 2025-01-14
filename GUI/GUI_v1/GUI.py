import tkinter as tk
from tkinter import ttk, messagebox
import os
import importlib
import traceback

class ModulationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Modulation Test Loader")
        self.root.attributes('-fullscreen', True)  # Set the GUI to fullscreen

        # Set dark theme colors
        self.bg_color = "#1a1a1a"  # Dark background color
        self.fg_color = "#e6e6e6"  # Light text color
        self.accent_color = "#004d99"  # Dark blue accent color

        self.root.configure(bg=self.bg_color)

        # Modulation selection variable
        self.modulation_var = tk.StringVar()
        self.path_var = tk.StringVar()
        self.test_var = tk.StringVar()

        # Create and configure the style for UI elements
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Helvetica", 14), background=self.bg_color, foreground=self.fg_color)
        self.style.configure("TButton", font=("Helvetica", 14, "bold"), padding=12, width=20)
        self.style.map("TButton", background=[("active", self.accent_color)])
        self.style.configure("TCombobox", font=("Helvetica", 14), padding=6, width=25)

        # Header label
        self.header_label = tk.Label(
            root, text="Select Modulation and Test Path", font=("Helvetica", 18, "bold"),
            bg=self.bg_color, fg=self.accent_color
        )
        self.header_label.pack(pady=20)

        # Dropdown for selecting modulation
        ttk.Label(root, text="Select Modulation:").pack(pady=10)
        self.modulation_menu = ttk.Combobox(root, textvariable=self.modulation_var, state="readonly")
        self.modulation_menu['values'] = ['PSK', 'BPSK', 'QAM', 'AM', 'ASK', 'FM', 'FSK']
        self.modulation_menu.pack(pady=10)
        self.modulation_menu.bind("<<ComboboxSelected>>", self.load_modulation)

        # Dropdown for selecting test path
        ttk.Label(root, text="Select Test Path:").pack(pady=10)
        self.path_menu = ttk.Combobox(root, textvariable=self.path_var, state="readonly")
        self.path_menu.pack(pady=10)
        self.path_menu.bind("<<ComboboxSelected>>", self.update_test_menu)

        # Dropdown for selecting test
        ttk.Label(root, text="Select Test:").pack(pady=10)
        self.test_menu = ttk.Combobox(root, textvariable=self.test_var, state="readonly")
        self.test_menu.pack(pady=10)

        # Run Test button
        self.run_button = ttk.Button(root, text="Run Test", command=self.run_test)
        self.run_button.pack(pady=30)

        # Exit button
        self.exit_button = ttk.Button(root, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=10)

        # Initialize variables
        self.current_module = None

    def load_modulation(self, event):
        """Load the selected modulation and update the dropdowns."""
        modulation = self.modulation_var.get()
        module_name = f"{modulation}.py"

        if not os.path.exists(module_name):
            self.current_module = None
            self.path_menu['values'] = []
            self.test_menu['values'] = []
            self.path_var.set('')
            self.test_var.set('')
            messagebox.showerror("Error", f"Modulation file '{module_name}' not found!")
            return

        try:
            self.current_module = importlib.import_module(modulation)
            importlib.reload(self.current_module)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load module '{module_name}': {e}")
            self.current_module = None
            return

        self.path_menu['values'] = ['Happy Path', 'Sad Path']
        self.path_var.set('')
        self.test_menu['values'] = []
        self.test_var.set('')

    def update_test_menu(self, event):
        """Update the test menu based on the selected path."""
        if not self.current_module:
            return

        selected_path = self.path_var.get()
        tests = [
            attr for attr in dir(self.current_module)
            if callable(getattr(self.current_module, attr)) and attr.startswith("test_")
        ]

        if selected_path == 'Happy Path':
            filtered_tests = [test for test in tests if 'happy' in test]
        elif selected_path == 'Sad Path':
            filtered_tests = [test for test in tests if 'sad' in test or 'invalid' in test]
        else:
            filtered_tests = []

        self.test_menu['values'] = filtered_tests
        self.test_var.set('')

    def run_test(self):
        """Run the selected test."""
        if not self.current_module:
            messagebox.showerror("Error", "No modulation module is loaded!")
            return

        selected_test = self.test_var.get()
        if not selected_test:
            messagebox.showerror("Error", "Please select a test to run.")
            return

        try:
            test_func = getattr(self.current_module, selected_test)
            test_func()
            messagebox.showinfo("Success", f"Test '{selected_test}' ran successfully.")
        except Exception as e:
            if 'sad' in selected_test or 'invalid' in selected_test:
                messagebox.showerror(
                    "Test Error",
                    f"Sad path test '{selected_test}' failed. Check terminal for details."
                )
                print(f"Error while running '{selected_test}':\n{traceback.format_exc()}")
            else:
                messagebox.showerror(
                    "Test Error",
                    f"An error occurred while running the test:\n\n{e}"
                )

if __name__ == "__main__":
    root = tk.Tk()
    app = ModulationGUI(root)
    root.mainloop()
