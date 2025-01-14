import os
import importlib
import os
import importlib
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class ModulationGUI:
    """!
    @brief A graphical user interface for simulating various digital and analog modulation techniques.
    """
    
    def __init__(self, root):
        """!
        @brief Initializes the ModulationGUI with the main Tkinter window.

        @param root (tk.Tk): The root Tkinter window.
        """
        

        self.root = root
        self.root.title("Modulation Simulator")

        # Load modulation modules
        self.modulation_modules = self.load_modulation_modules()
        self.modulation_names = ["AM_modulation", "ASK_modulation", "FM_modulation", "FSK_modulation", "PSK_modulation", "BPSK_modulation", "QAM_modulation", "QPSK_modulation"]
        self.selected_modulation = tk.StringVar()

        # Parameter frames
        self.parameter_frames = {}
        self.parameter_vars = {}

        # Styling
        style = ttk.Style()
        style.theme_use('clam')  # Use a modern theme
        style.configure('TButton', padding=6, font=('Arial', 10))
        style.configure('TLabel', font=('Arial', 10))
        style.configure('TCombobox', font=('Arial', 10))
        style.configure('TEntry', font=('Arial', 10))
        
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Modulation selection
        ttk.Label(main_frame, text="Select Modulation:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.modulation_combo = ttk.Combobox(main_frame, textvariable=self.selected_modulation, values=self.modulation_names, state="readonly")
        self.modulation_combo.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)
        # Matplotlib figure
        self.fig, self.ax = plt.subplots(figsize=(8, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10)
        self.fig.set_tight_layout(True)

        if self.modulation_names:
            self.modulation_combo.current(0)
            self.show_parameters(None)
        self.modulation_combo.bind("<<ComboboxSelected>>", self.show_parameters)

        # AM parameters
        # AM parameters
        am_frame = ttk.LabelFrame(main_frame, text="AM Parameters")
        am_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        am_frame.grid_remove()
        self.parameter_frames['AM_modulation'] = am_frame

        ttk.Label(am_frame, text="Carrier Frequency (Hz):").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.parameter_vars['am_carrier_freq'] = tk.DoubleVar(value=10.0)
        ttk.Entry(am_frame, textvariable=self.parameter_vars['am_carrier_freq'], validate="focusout", validatecommand=(self.root.register(self.validate_am_carrier_freq), '%P')).grid(row=0, column=1, sticky=(tk.W, tk.E), pady=2)
        self.am_carrier_freq_label = ttk.Label(am_frame, text="")
        self.am_carrier_freq_label.grid(row=0, column=2, sticky=tk.W, pady=2)
        ttk.Label(am_frame, text="(1-100)").grid(row=0, column=3, sticky=tk.W, pady=2)

        ttk.Label(am_frame, text="Initial Phase (rad):").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.parameter_vars['am_initial_phase'] = tk.DoubleVar(value=0.0)
        ttk.Entry(am_frame, textvariable=self.parameter_vars['am_initial_phase']).grid(row=1, column=1, sticky=(tk.W, tk.E), pady=2)
        self.am_initial_phase_label = ttk.Label(am_frame, text=f"{self.parameter_vars['am_initial_phase'].get():.1f}")
        self.am_initial_phase_label.grid(row=1, column=2, sticky=tk.W, pady=2)
        ttk.Label(am_frame, text="(-π to π)").grid(row=1, column=3, sticky=tk.W, pady=2)

        ttk.Label(am_frame, text="Amplitude:").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.parameter_vars['am_amplitude'] = tk.DoubleVar(value=1.0)
        ttk.Entry(am_frame, textvariable=self.parameter_vars['am_amplitude']).grid(row=2, column=1, sticky=(tk.W, tk.E), pady=2)
        self.am_amplitude_label = ttk.Label(am_frame, text=f"{self.parameter_vars['am_amplitude'].get():.1f}")
        self.am_amplitude_label.grid(row=2, column=2, sticky=tk.W, pady=2)
        ttk.Label(am_frame, text="(0-5)").grid(row=2, column=3, sticky=tk.W, pady=2)

        ttk.Label(am_frame, text="Duration (s):").grid(row=3, column=0, sticky=tk.W, pady=2)
        self.parameter_vars['am_duration'] = tk.DoubleVar(value=2.0)
        ttk.Entry(am_frame, textvariable=self.parameter_vars['am_duration']).grid(row=3, column=1, sticky=(tk.W, tk.E), pady=2)
        self.am_duration_label = ttk.Label(am_frame, text="")
        self.am_duration_label.grid(row=3, column=2, sticky=tk.W, pady=2)
        ttk.Label(am_frame, text="(0-10)").grid(row=3, column=3, sticky=tk.W, pady=2)
        self.update_am_labels()

        # FSK parameters
        fsk_frame = ttk.LabelFrame(main_frame, text="FSK Parameters")
        fsk_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        fsk_frame.grid_remove()
        self.parameter_frames['FSK_modulation'] = fsk_frame

        ttk.Label(fsk_frame, text="Carrier Frequency 0 (Hz):").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.parameter_vars['fsk_carrier_freq_0'] = tk.DoubleVar(value=5.0)
        ttk.Entry(fsk_frame, textvariable=self.parameter_vars['fsk_carrier_freq_0']).grid(row=0, column=1, sticky=(tk.W, tk.E), pady=2)
        self.fsk_carrier_freq_0_label = ttk.Label(fsk_frame, text="1.0")
        self.fsk_carrier_freq_0_label.grid(row=0, column=2, sticky=tk.W, pady=2)
        ttk.Label(fsk_frame, text="(1-100)").grid(row=0, column=3, sticky=tk.W, pady=2)

        ttk.Label(fsk_frame, text="Carrier Frequency 1 (Hz):").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.parameter_vars['fsk_carrier_freq_1'] = tk.DoubleVar(value=10.0)
        ttk.Entry(fsk_frame, textvariable=self.parameter_vars['fsk_carrier_freq_1']).grid(row=1, column=1, sticky=(tk.W, tk.E), pady=2)
        self.fsk_carrier_freq_1_label = ttk.Label(fsk_frame, text="1.0")
        self.fsk_carrier_freq_1_label.grid(row=1, column=2, sticky=tk.W, pady=2)
        ttk.Label(fsk_frame, text="(1-100)").grid(row=1, column=3, sticky=tk.W, pady=2)

        ttk.Label(fsk_frame, text="Bit Duration (s):").grid(row=2, column=0, sticky=tk.W, pady=2)
        ttk.Label(fsk_frame, text="Bit Duration (s):").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.parameter_vars['fsk_bit_duration'] = tk.DoubleVar(value=1.0)
        ttk.Entry(fsk_frame, textvariable=self.parameter_vars['fsk_bit_duration']).grid(row=2, column=1, sticky=(tk.W, tk.E), pady=2)
        self.fsk_bit_duration_label = ttk.Label(fsk_frame, text="0.1")
        self.fsk_bit_duration_label.grid(row=2, column=2, sticky=tk.W, pady=2)
        ttk.Label(fsk_frame, text="(0.1-10)").grid(row=2, column=3, sticky=tk.W, pady=2)


        # BPSK parameters
        bpsk_frame = ttk.LabelFrame(main_frame, text="BPSK Parameters")
        bpsk_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        bpsk_frame.grid_remove()
        self.parameter_frames['BPSK_modulation'] = bpsk_frame

        ttk.Label(bpsk_frame, text="Carrier Frequency (Hz):").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.parameter_vars['bpsk_carrier_freq'] = tk.DoubleVar(value=5.0)
        ttk.Entry(bpsk_frame, textvariable=self.parameter_vars['bpsk_carrier_freq']).grid(row=0, column=1, sticky=(tk.W, tk.E), pady=2)
        self.bpsk_carrier_freq_label = ttk.Label(bpsk_frame, text="1.0")
        self.bpsk_carrier_freq_label.grid(row=0, column=2, sticky=tk.W, pady=2)
        ttk.Label(bpsk_frame, text="(1-100)").grid(row=0, column=3, sticky=tk.W, pady=2)

        ttk.Label(bpsk_frame, text="Bit Duration (s):").grid(row=1, column=0, sticky=tk.W, pady=2)
        ttk.Label(bpsk_frame, text="Bit Duration (s):").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.parameter_vars['bpsk_bit_duration'] = tk.DoubleVar(value=1.0)
        ttk.Entry(bpsk_frame, textvariable=self.parameter_vars['bpsk_bit_duration']).grid(row=1, column=1, sticky=(tk.W, tk.E), pady=2)
        self.bpsk_bit_duration_label = ttk.Label(bpsk_frame, text="0.1")
        self.bpsk_bit_duration_label.grid(row=1, column=2, sticky=tk.W, pady=2)
        ttk.Label(bpsk_frame, text="(0.1-10)").grid(row=1, column=3, sticky=tk.W, pady=2)


        # PSK parameters
        psk_frame = ttk.LabelFrame(main_frame, text="PSK Parameters")
        psk_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        psk_frame.grid_remove()
        self.parameter_frames['PSK_modulation'] = psk_frame

        ttk.Label(psk_frame, text="Carrier Frequency (Hz):").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.parameter_vars['psk_carrier_freq'] = tk.DoubleVar(value=5.0)
        ttk.Entry(psk_frame, textvariable=self.parameter_vars['psk_carrier_freq']).grid(row=0, column=1, sticky=(tk.W, tk.E), pady=2)
        self.psk_carrier_freq_label = ttk.Label(psk_frame, text="1.0")
        self.psk_carrier_freq_label.grid(row=0, column=2, sticky=tk.W, pady=2)
        ttk.Label(psk_frame, text="(1-100)").grid(row=0, column=3, sticky=tk.W, pady=2)

        ttk.Label(psk_frame, text="Bit Duration (s):").grid(row=1, column=0, sticky=tk.W, pady=2)
        ttk.Label(psk_frame, text="Bit Duration (s):").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.parameter_vars['psk_bit_duration'] = tk.DoubleVar(value=1.0)
        ttk.Entry(psk_frame, textvariable=self.parameter_vars['psk_bit_duration']).grid(row=1, column=1, sticky=(tk.W, tk.E), pady=2)
        self.psk_bit_duration_label = ttk.Label(psk_frame, text="0.1")
        self.psk_bit_duration_label.grid(row=1, column=2, sticky=tk.W, pady=2)
        ttk.Label(psk_frame, text="(0.1-10)").grid(row=1, column=3, sticky=tk.W, pady=2)


        # QAM parameters
        qam_frame = ttk.LabelFrame(main_frame, text="QAM Parameters")
        qam_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        qam_frame.grid_remove()
        self.parameter_frames['QAM_modulation'] = qam_frame

        ttk.Label(qam_frame, text="Carrier Frequency (Hz):").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.parameter_vars['qam_carrier_freq'] = tk.DoubleVar(value=5.0)
        ttk.Entry(qam_frame, textvariable=self.parameter_vars['qam_carrier_freq']).grid(row=0, column=1, sticky=(tk.W, tk.E), pady=2)
        self.qam_carrier_freq_label = ttk.Label(qam_frame, text="1.0")
        self.qam_carrier_freq_label.grid(row=0, column=2, sticky=tk.W, pady=2)
        ttk.Label(qam_frame, text="(1-100)").grid(row=0, column=3, sticky=tk.W, pady=2)

        ttk.Label(qam_frame, text="Bit Duration (s):").grid(row=1, column=0, sticky=tk.W, pady=2)
        ttk.Label(qam_frame, text="Bit Duration (s):").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.parameter_vars['qam_bit_duration'] = tk.DoubleVar(value=1.0)
        ttk.Entry(qam_frame, textvariable=self.parameter_vars['qam_bit_duration']).grid(row=1, column=1, sticky=(tk.W, tk.E), pady=2)
        self.qam_bit_duration_label = ttk.Label(qam_frame, text="0.1")
        self.qam_bit_duration_label.grid(row=1, column=2, sticky=tk.W, pady=2)
        ttk.Label(qam_frame, text="(0.1-10)").grid(row=1, column=3, sticky=tk.W, pady=2)

        ttk.Label(qam_frame, text="Constellation Points (e.g., 1+1j, 1-1j, -1+1j, -1-1j):").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.parameter_vars['qam_constellation_points'] = tk.StringVar(value="1+1j, 1-1j, -1+1j, -1-1j")
        ttk.Entry(qam_frame, textvariable=self.parameter_vars['qam_constellation_points']).grid(row=2, column=1, sticky=(tk.W, tk.E), pady=2)
        ttk.Label(qam_frame, text="(Complex)").grid(row=2, column=2, sticky=tk.W, pady=2)


        # FM parameters
        # FM parameters
        fm_frame = ttk.LabelFrame(main_frame, text="FM Parameters")
        fm_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        fm_frame.grid_remove()
        self.parameter_frames['FM_modulation'] = fm_frame

        ttk.Label(fm_frame, text="Carrier Frequency (Hz):").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.parameter_vars['fm_carrier_freq'] = tk.DoubleVar(value=10.0)
        ttk.Entry(fm_frame, textvariable=self.parameter_vars['fm_carrier_freq']).grid(row=0, column=1, sticky=(tk.W, tk.E), pady=2)
        self.fm_carrier_freq_label = ttk.Label(fm_frame, text="1.0")
        self.fm_carrier_freq_label.grid(row=0, column=2, sticky=tk.W, pady=2)
        ttk.Label(fm_frame, text="(1-100)").grid(row=0, column=3, sticky=tk.W, pady=2)

        ttk.Label(fm_frame, text="Duration (s):").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.parameter_vars['fm_duration'] = tk.DoubleVar(value=2.0)
        ttk.Entry(fm_frame, textvariable=self.parameter_vars['fm_duration']).grid(row=1, column=1, sticky=(tk.W, tk.E), pady=2)
        self.fm_duration_label = ttk.Label(fm_frame, text="0.1")
        self.fm_duration_label.grid(row=1, column=2, sticky=tk.W, pady=2)
        ttk.Label(fm_frame, text="(0.1-10)").grid(row=1, column=3, sticky=tk.W, pady=2)

        ttk.Label(fm_frame, text="Frequency Deviation (Hz):").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.parameter_vars['fm_freq_deviation'] = tk.DoubleVar(value=5.0)
        ttk.Entry(fm_frame, textvariable=self.parameter_vars['fm_freq_deviation']).grid(row=2, column=1, sticky=(tk.W, tk.E), pady=2)
        self.fm_freq_deviation_label = ttk.Label(fm_frame, text=f"{self.parameter_vars['fm_freq_deviation'].get():.1f}")
        self.fm_freq_deviation_label.grid(row=2, column=2, sticky=tk.W, pady=2)


        # ASK parameters
        ask_frame = ttk.LabelFrame(main_frame, text="ASK Parameters")
        ask_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        ask_frame.grid_remove()
        self.parameter_frames['ASK_modulation'] = ask_frame

        ttk.Label(ask_frame, text="Binary Sequence (e.g., 1, 0, 1, 0):").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.parameter_vars['ask_binary_sequence'] = tk.StringVar(value="1, 0, 1, 0")
        ttk.Entry(ask_frame, textvariable=self.parameter_vars['ask_binary_sequence']).grid(row=0, column=1, sticky=(tk.W, tk.E), pady=2)
        ttk.Label(ask_frame, text="(Binary)").grid(row=0, column=2, sticky=tk.W, pady=2)

        ttk.Label(ask_frame, text="Carrier Frequency (Hz):").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.parameter_vars['ask_carrier_freq'] = tk.DoubleVar(value=10.0)
        ttk.Entry(ask_frame, textvariable=self.parameter_vars['ask_carrier_freq'], validate="focusout", validatecommand=(self.root.register(self.validate_ask_carrier_freq), '%P')).grid(row=1, column=1, sticky=(tk.W, tk.E), pady=2)
        self.ask_carrier_freq_label = ttk.Label(ask_frame, text=f"{self.parameter_vars['ask_carrier_freq'].get():.1f}")
        self.ask_carrier_freq_label.grid(row=1, column=2, sticky=tk.W, pady=2)
        ttk.Label(ask_frame, text="(1-100)").grid(row=1, column=3, sticky=tk.W, pady=2)

        ttk.Label(ask_frame, text="Amplitude:").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.parameter_vars['ask_amplitude'] = tk.DoubleVar(value=1.0)
        ttk.Entry(ask_frame, textvariable=self.parameter_vars['ask_amplitude']).grid(row=2, column=1, sticky=(tk.W, tk.E), pady=2)
        self.ask_amplitude_label = ttk.Label(ask_frame, text=f"{self.parameter_vars['ask_amplitude'].get():.1f}")
        self.ask_amplitude_label.grid(row=2, column=2, sticky=tk.W, pady=2)
        ttk.Label(ask_frame, text="(0-5)").grid(row=2, column=3, sticky=tk.W, pady=2)

        ttk.Label(ask_frame, text="Bit Duration (s):").grid(row=3, column=0, sticky=tk.W, pady=2)
        self.parameter_vars['ask_bit_duration'] = tk.DoubleVar(value=1.0)
        ttk.Entry(ask_frame, textvariable=self.parameter_vars['ask_bit_duration']).grid(row=3, column=1, sticky=(tk.W, tk.E), pady=2)
        self.ask_bit_duration_label = ttk.Label(ask_frame, text=f"{self.parameter_vars['ask_bit_duration'].get():.1f}")
        self.ask_bit_duration_label.grid(row=3, column=2, sticky=tk.W, pady=2)
        ttk.Label(ask_frame, text="(0.1-10)").grid(row=3, column=3, sticky=tk.W, pady=2)
        self.update_ask_labels()

        # QPSK parameters
        qpsk_frame = ttk.LabelFrame(main_frame, text="QPSK Parameters")
        qpsk_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        qpsk_frame.grid_remove()
        self.parameter_frames['QPSK_modulation'] = qpsk_frame

        ttk.Label(qpsk_frame, text="Carrier Frequency (Hz):").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.parameter_vars['qpsk_carrier_freq'] = tk.DoubleVar(value=5.0)
        ttk.Entry(qpsk_frame, textvariable=self.parameter_vars['qpsk_carrier_freq']).grid(row=0, column=1, sticky=(tk.W, tk.E), pady=2)
        self.qpsk_carrier_freq_label = ttk.Label(qpsk_frame, text=f"{self.parameter_vars['qpsk_carrier_freq'].get():.1f}")
        self.qpsk_carrier_freq_label.grid(row=0, column=2, sticky=tk.W, pady=2)
        ttk.Label(qpsk_frame, text="(1-100)").grid(row=0, column=3, sticky=tk.W, pady=2)

        ttk.Label(qpsk_frame, text="Bit Duration (s):").grid(row=1, column=0, sticky=tk.W, pady=2)
        ttk.Label(qpsk_frame, text="Bit Duration (s):").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.parameter_vars['qpsk_bit_duration'] = tk.DoubleVar(value=1.0)
        ttk.Entry(qpsk_frame, textvariable=self.parameter_vars['qpsk_bit_duration']).grid(row=1, column=1, sticky=(tk.W, tk.E), pady=2)
        self.qpsk_bit_duration_label = ttk.Label(qpsk_frame, text="0.1")
        self.qpsk_bit_duration_label.grid(row=1, column=2, sticky=tk.W, pady=2)
        ttk.Label(qpsk_frame, text="(0.1-10)").grid(row=1, column=3, sticky=tk.W, pady=2)


        # Run button
        run_button = ttk.Button(main_frame, text="Run Simulation", command=self.run_simulation)
        run_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Help button
        help_button = ttk.Button(main_frame, text="Help", command=self.show_help)
        help_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Matplotlib figure
        self.fig, self.ax = plt.subplots(figsize=(8, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10)
        self.fig.set_tight_layout(True)

        # Configure grid weights
        self.root.columnconfigure(0, weight=1)

        self.root.columnconfigure(1, weight=2)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

    def show_help(self):
        """!
        @brief Displays a help message box with information about the program.
        """
        help_text = """
        This program simulates various digital and analog modulation techniques.
        
        To use the program:
        1. Select a modulation type from the dropdown menu.
        2. Adjust the parameters for the selected modulation type.
        3. Click the 'Run Simulation' button to generate and display the modulated signal.
        
        The plots will show the message signal, carrier signal, and the modulated signal.
        
        For digital modulations, a binary sequence is used as input.
        For analog modulations, a sinusoidal signal is used as input.
        
        Use the sliders and entry fields to adjust the parameters.
        """
        messagebox.showinfo("Help", help_text)

    def get_parameters(self, param_names):
        """!
        @brief Extracts parameters from the parameter_vars dictionary.

        @param param_names (list): A list of parameter names to extract.

        @return dict: A dictionary containing the extracted parameters.
        """
        params = {}
        for name in param_names:
            if name in self.parameter_vars:
                var = self.parameter_vars[name]
                try:
                    if isinstance(var, tk.DoubleVar):
                        params[name] = float(var.get())
                    elif isinstance(var, tk.StringVar):
                        params[name] = var.get()
                    else:
                        params[name] = var.get()
                except ValueError as e:
                     messagebox.showerror("Error", f"Invalid input for {name}. Please enter a valid number.")
                     return None
            else:
                messagebox.showerror("Error", f"Parameter {name} not found.")
                return None
        return params

    def validate_range(self, value, min_val, max_val, var_name):
        """!
        @brief Validates if the input value is within the specified range.

        @param value (str): The input value to validate.
        @param min_val (float): The minimum allowed value.
        @param max_val (float): The maximum allowed value.
        @param var_name (str): The name of the variable being validated.

        @return bool: True if the value is valid, False otherwise.
        """
        try:
            value = float(value)
            if value < min_val or value > max_val:
                messagebox.showerror("Error", f"Value for {var_name} must be between {min_val} and {max_val}.")
                return False
            return True
        except ValueError:
            messagebox.showerror("Error", f"Invalid input for {var_name}. Please enter a number.")
            return False


    """!
    @brief Shows the parameter frame for the selected modulation and hides the others.
    """

    def show_parameters(self, event):
        selected_modulation = self.selected_modulation.get()
        for name, frame in self.parameter_frames.items():
            if name == selected_modulation:
                frame.grid()
                if name == 'AM_modulation':
                    self.update_am_labels()
            else:
                frame.grid_remove()

    def load_modulation_modules(self):
        """!
        @brief Loads modulation modules from the 'Modulation_files' directory.

        @return dict: A dictionary where keys are module names and values are the modulation functions.
        """
        gui_dir = os.path.dirname(os.path.abspath(__file__))
        modulation_dir = os.path.join(gui_dir, '..', 'Modulation_files')
        modulation_modules = {}
        print("Contents of modulation directory:", os.listdir(modulation_dir))
        for root, _, files in os.walk(modulation_dir):
            for item in files:
                if item.endswith('.py') and not item.startswith('__'):
                    module_name = item[:-3]
                    module_path = os.path.join(root, item)
                    spec = importlib.util.spec_from_file_location(module_name, module_path)
                    module = importlib.util.module_from_spec(spec)
                    try:
                        spec.loader.exec_module(module)
                        print(f"Imported module: {module_name} from {root}")
                        print(f"Module attributes: {dir(module)}")
                    except Exception as e:
                        print(f"Error executing module {module_name}: {e}")
                        continue

                    # Find the modulation function within the module
                    modulation_func = None
                    for name in dir(module):
                        if name.endswith('_modulation') and callable(getattr(module, name)):
                            modulation_func = getattr(module, name)
                            break
                    if modulation_func:
                        modulation_modules[module_name] = modulation_func
        print("Loaded modules:", list(modulation_modules.keys()))
        return modulation_modules

    """!
    @brief Executes the selected modulation function and plots the result.
    """
    
    def run_simulation(self):
        self.show_parameters(None)
        
        selected_module = self.selected_modulation.get()

        if not selected_module:
            messagebox.showerror("Error", "Please select a modulation type.")
            return

        module = self.modulation_modules.get(selected_module)
        if module is None:
            messagebox.showerror("Error", "Selected modulation module not found.")
            return
        self.fig.clf()
        try:
            if selected_module == 'AM_modulation':
                params = self.get_parameters(['am_carrier_freq', 'am_initial_phase', 'am_amplitude', 'am_duration'])
                if params is None:
                    return
                time, message_signal, carrier_signal, am_signal = module(
                    carrier_freq=params['am_carrier_freq'], sample_rate=1000, duration=params['am_duration'])
                am_signal = params['am_amplitude'] * message_signal * np.cos(2 * np.pi * params['am_carrier_freq'] * time + params['am_initial_phase'])
                self.plot_am_signals(time, message_signal, carrier_signal, am_signal, carrier_freq=params['am_carrier_freq'])
                self.update_am_labels()

            elif selected_module == 'FSK_modulation':
                params = self.get_parameters(['fsk_carrier_freq_0', 'fsk_carrier_freq_1', 'fsk_bit_duration'])
                if params is None:
                    return
                binary_data = [1, 0, 1, 0]  # Fixed binary data for now
                time, modulating_signal, carrier_signal_0, carrier_signal_1, fsk_signal = module(
                    binary_data=binary_data, carrier_freq_0=params['fsk_carrier_freq_0'], carrier_freq_1=params['fsk_carrier_freq_1'], sample_rate=1000, bit_duration=params['fsk_bit_duration'])
                self.plot_fsk_signals(time, modulating_signal, carrier_signal_0, carrier_signal_1, fsk_signal, carrier_freq_0=params['fsk_carrier_freq_0'], carrier_freq_1=params['fsk_carrier_freq_1'])

            elif selected_module == 'BPSK_modulation':
                params = self.get_parameters(['bpsk_carrier_freq', 'bpsk_bit_duration'])
                if params is None:
                    return
                binary_data = [1, 0, 1, 0]  # Fixed binary data for now
                time, modulating_signal, carrier_signal, bpsk_signal = module(
                    binary_data=binary_data, carrier_freq=params['bpsk_carrier_freq'], sample_rate=1000, bit_duration=params['bpsk_bit_duration'])
                self.plot_bpsk_signals(time, modulating_signal, carrier_signal, bpsk_signal, carrier_freq=params['bpsk_carrier_freq'])

            elif selected_module == 'PSK_modulation':
                params = self.get_parameters(['psk_carrier_freq', 'psk_bit_duration'])
                if params is None:
                    return
                binary_data = [1, 0, 1, 0]  # Fixed binary data for now
                time, modulating_signal, carrier_signal, psk_signal = module(
                    binary_data=binary_data, carrier_freq=params['psk_carrier_freq'], sample_rate=1000, bit_duration=params['psk_bit_duration'])
                self.plot_psk_signals(time, modulating_signal, carrier_signal, psk_signal, carrier_freq=params['psk_carrier_freq'])

            elif selected_module == 'QAM_modulation':
                params = self.get_parameters(['qam_carrier_freq', 'qam_bit_duration', 'qam_constellation_points'])
                if params is None:
                    return
                try:
                    constellation_points = [complex(x.strip()) for x in params['qam_constellation_points'].split(',')]
                except ValueError:
                    messagebox.showerror("Error", "Invalid constellation points format.")
                    return
                binary_data = [0, 1, 1, 0, 1, 1, 0, 0]  # Fixed binary data for now
                time, modulating_signal, carrier_signal_i, carrier_signal_q, qam_signal = module(
                    binary_data=binary_data, carrier_freq=params['qam_carrier_freq'], sample_rate=1000, bit_duration=params['qam_bit_duration'], constellation_points=constellation_points)
                self.plot_qam_signals(time, modulating_signal, carrier_signal_i, carrier_signal_q, qam_signal, carrier_freq=params['qam_carrier_freq'], constellation_points=constellation_points)

            elif selected_module == 'FM_modulation':
                params = self.get_parameters(['fm_carrier_freq', 'fm_duration', 'fm_freq_deviation'])
                if params is None:
                    return
                time, message_signal, carrier_signal, fm_signal = module(
                    carrier_freq=params['fm_carrier_freq'], sample_rate=1000, duration=params['fm_duration'], freq_deviation=params['fm_freq_deviation'])
                self.plot_fm_signals(time, message_signal, carrier_signal, fm_signal, carrier_freq=params['fm_carrier_freq'], freq_deviation=params['fm_freq_deviation'])

            elif selected_module == 'ASK_modulation':
                params = self.get_parameters(['ask_binary_sequence', 'ask_carrier_freq', 'ask_amplitude', 'ask_bit_duration'])
                if params is None:
                    return
                try:
                    binary_sequence = list(map(int, params['ask_binary_sequence'].split(',')))
                except ValueError:
                    messagebox.showerror("Error", "Invalid binary sequence format.")
                    return
                time, bw, sint, st = module(
                    binary_sequence=binary_sequence, carrier_freq=params['ask_carrier_freq'], amplitude=params['ask_amplitude'], bit_duration=params['ask_bit_duration']
                )
                self.plot_ask_signals(time, bw, sint, st)
                self.update_ask_labels()
            elif selected_module == 'QPSK_modulation':
                params = self.get_parameters(['qpsk_carrier_freq', 'qpsk_bit_duration'])
                if params is None:
                    return
                binary_data = [0, 1, 1, 0, 1, 1, 0, 0]  # Fixed binary data for now
                time, modulating_signal, carrier_signal_i, carrier_signal_q, qpsk_signal = module(
                    binary_data=binary_data, carrier_freq=params['qpsk_carrier_freq'], sample_rate=1000, bit_duration=params['qpsk_bit_duration'])
                self.plot_qpsk_signals(time, modulating_signal, carrier_signal_i, carrier_signal_q, qpsk_signal, carrier_freq=params['qpsk_carrier_freq'])
            else:
                messagebox.showerror("Error", "Unsupported modulation function.")
                return
            self.canvas.draw()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during modulation: {e}")

    def validate_am_carrier_freq(self, value):
        if self.validate_range(value, 1, 100, "AM Carrier Frequency"):
            self.am_carrier_freq_label.config(text=f"{float(value):.1f}")
            return True
        return False

    def validate_ask_carrier_freq(self, value):
        return self.validate_range(value, 1, 100, "ASK Carrier Frequency")

    def update_am_labels(self):
        """!
        @brief Updates the labels for AM parameters with the current values.
        """
        self.am_carrier_freq_label.config(text=f"{self.parameter_vars['am_carrier_freq'].get():.1f}")
        self.am_initial_phase_label.config(text=f"{self.parameter_vars['am_initial_phase'].get():.1f}")
        self.am_amplitude_label.config(text=f"{self.parameter_vars['am_amplitude'].get():.1f}")
        self.am_duration_label.config(text=f"{self.parameter_vars['am_duration'].get():.1f}")

    def update_ask_labels(self):
        """!
        @brief Updates the labels for ASK parameters with the current values.
        """
        self.ask_carrier_freq_label.config(text=f"{self.parameter_vars['ask_carrier_freq'].get():.1f}")
        self.ask_amplitude_label.config(text=f"{self.parameter_vars['ask_amplitude'].get():.1f}")
        self.ask_bit_duration_label.config(text=f"{self.parameter_vars['ask_bit_duration'].get():.1f}")

    def plot_am_signals(self, time, message_signal, carrier_signal, am_signal, carrier_freq):
        """!
        @brief Plot the message signal, carrier signal, and AM modulated signal.

        @param time (np.array): Time vector for the signals.
        @param message_signal (np.array): The base message signal.
        @param carrier_signal (np.array): The carrier signal.
        @param am_signal (np.array): The AM modulated signal.
        @param carrier_freq (float): Frequency of the carrier signal in Hz.
        """
        
        self.ax.clear()
        
        
        ax1 = self.fig.add_subplot(3, 1, 1)
        ax1.plot(time, message_signal, label='Message Signal')
        ax1.set_title('Message Signal')
        ax1.set_xlabel('Time (s)')
        ax1.set_ylabel('Amplitude')
        ax1.legend()
        ax1.grid(True)

        ax2 = self.fig.add_subplot(3, 1, 2, sharex=ax1)
        ax2.plot(time, carrier_signal, label=f'Carrier Signal (Fc={carrier_freq} Hz)', color='orange')
        ax2.set_title('Carrier Signal')
        ax2.set_xlabel('Time (s)')
        ax2.set_ylabel('Amplitude')
        ax2.legend()
        ax2.grid(True)

        ax3 = self.fig.add_subplot(3, 1, 3, sharex=ax1)
        ax3.plot(time, am_signal, label='AM Signal', color='green')
        ax3.set_title('AM Signal')
        ax3.set_xlabel('Time (s)')
        ax3.set_ylabel('Amplitude')
        ax3.legend()
        ax3.grid(True)
        self.fig.tight_layout()

    def plot_fsk_signals(self, time, modulating_signal, carrier_signal_0, carrier_signal_1, fsk_signal, carrier_freq_0,
                         carrier_freq_1):
        """!
        @brief Plot the modulating signal, carrier signals, and the FSK modulated signal.

        @param time (np.array): Time vector for the signals.
        @param modulating_signal (np.array): Binary modulating signal over time.
        @param carrier_signal_0 (np.array): Carrier signal for binary 0.
        @param carrier_signal_1 (np.array): Carrier signal for binary 1.
        @param fsk_signal (np.array): FSK modulated signal.
        @param carrier_freq_0 (float): Frequency of carrier signal for binary 0 (Hz).
        @param carrier_freq_1 (float): Frequency of carrier signal for binary 1 (Hz).
        """
        
        self.ax.clear()
        
        
        ax1 = self.fig.add_subplot(4, 1, 1)
        ax1.step(time, modulating_signal, where='post', label='Modulating Signal')
        ax1.set_title('Modulating Signal')
        ax1.set_xlabel('Time (s)')
        ax1.set_ylabel('Amplitude')
        ax1.legend()
        ax1.grid(True)

        ax2 = self.fig.add_subplot(4, 1, 2, sharex=ax1)
        ax2.plot(time, carrier_signal_0, label=f'Carrier 0 (Fc={carrier_freq_0} Hz)', color='orange')
        ax2.set_title(f'Carrier Signal 0 (Fc={carrier_freq_0} Hz)')
        ax2.set_xlabel('Time (s)')
        ax2.set_ylabel('Amplitude')
        ax2.legend()
        ax2.grid(True)

        ax3 = self.fig.add_subplot(4, 1, 3, sharex=ax1)
        ax3.plot(time, carrier_signal_1, label=f'Carrier 1 (Fc={carrier_freq_1} Hz)', color='green')
        ax3.set_title(f'Carrier Signal 1 (Fc={carrier_freq_1} Hz)')
        ax3.set_xlabel('Time (s)')
        ax3.set_ylabel('Amplitude')
        ax3.legend()
        ax3.grid(True)

        ax4 = self.fig.add_subplot(4, 1, 4, sharex=ax1)
        ax4.plot(time, fsk_signal, label='FSK Signal', color='red')
        ax4.set_title('FSK Signal')
        ax4.set_xlabel('Time (s)')
        ax4.set_ylabel('Amplitude')
        ax4.legend()
        ax4.grid(True)
        self.fig.tight_layout()

    def plot_bpsk_signals(self, time, modulating_signal, carrier_signal, bpsk_signal, carrier_freq):
        """!
        @brief Plot the modulating signal, carrier signal, and the BPSK modulated signal.

        @param time (np.array): Time vector for the signals.
        @param modulating_signal (np.array): Binary modulating signal over time.
        @param carrier_signal (np.array): Carrier signal.
        @param bpsk_signal (np.array): BPSK modulated signal.
        @param carrier_freq (float): Frequency of carrier signal (Hz).
        """
        
        self.ax.clear()
        
        
        ax1 = self.fig.add_subplot(3, 1, 1)
        ax1.step(time, modulating_signal, where='post', label='Modulating Signal')
        ax1.set_title('Modulating Signal')
        ax1.set_xlabel('Time (s)')
        ax1.set_ylabel('Amplitude')
        ax1.legend()
        ax1.grid(True)

        ax2 = self.fig.add_subplot(3, 1, 2, sharex=ax1)
        ax2.plot(time, carrier_signal, label=f'Carrier (Fc={carrier_freq} Hz)', color='orange')
        ax2.set_title(f'Carrier Signal (Fc={carrier_freq} Hz)')
        ax2.set_xlabel('Time (s)')
        ax2.set_ylabel('Amplitude')
        ax2.legend()
        ax2.grid(True)

        ax3 = self.fig.add_subplot(3, 1, 3, sharex=ax1)
        ax3.plot(time, bpsk_signal, label='BPSK Signal', color='green')
        ax3.set_title('BPSK Signal')
        ax3.set_xlabel('Time (s)')
        ax3.set_ylabel('Amplitude')
        ax3.legend()
        ax3.grid(True)
        self.fig.tight_layout()

    def plot_psk_signals(self, time, modulating_signal, carrier_signal, psk_signal, carrier_freq):
        """!
        @brief Plot the modulating signal, carrier signal, and the PSK modulated signal.

        @param time (np.array): Time vector for the signals.
        @param modulating_signal (np.array): Binary modulating signal over time.
        @param carrier_signal (np.array): Carrier signal.
        @param psk_signal (np.array): PSK modulated signal.
        @param carrier_freq (float): Frequency of carrier signal (Hz).
        """
        
        self.ax.clear()
        
        
        ax1 = self.fig.add_subplot(3, 1, 1)
        ax1.step(time, modulating_signal, where='post', label='Modulating Signal')
        ax1.set_title('Modulating Signal')
        ax1.set_xlabel('Time (s)')
        ax1.set_ylabel('Amplitude')
        ax1.legend()
        ax1.grid(True)

        ax2 = self.fig.add_subplot(3, 1, 2, sharex=ax1)
        ax2.plot(time, carrier_signal, label=f'Carrier (Fc={carrier_freq} Hz)', color='orange')
        ax2.set_title(f'Carrier Signal (Fc={carrier_freq} Hz)')
        ax2.set_xlabel('Time (s)')
        ax2.set_ylabel('Amplitude')
        ax2.legend()
        ax2.grid(True)

        ax3 = self.fig.add_subplot(3, 1, 3, sharex=ax1)
        ax3.plot(time, psk_signal, label='PSK Signal', color='green')
        ax3.set_title('PSK Signal')
        ax3.set_xlabel('Time (s)')
        ax3.set_ylabel('Amplitude')
        ax3.legend()
        ax3.grid(True)
        self.fig.tight_layout()

    def plot_qam_signals(self, time, modulating_signal, carrier_signal_i, carrier_signal_q, qam_signal, carrier_freq, constellation_points):
        """!
        @brief Plot the modulating signal, carrier signals, and the QAM modulated signal.

        @param time (np.array): Time vector for the signals.
        @param modulating_signal (np.array): Integer representation of the constellation points over time.
        @param carrier_signal_i (np.array): In-phase carrier signal.
        @param carrier_signal_q (np.array): Quadrature carrier signal.
        @param qam_signal (np.array): QAM modulated signal.
        @param carrier_freq (float): Frequency of carrier signal (Hz).
        @param constellation_points (list): A list of complex numbers representing the constellation points.
        """
        
        self.ax.clear()
        
        
        ax1 = self.fig.add_subplot(5, 1, 1)
        ax1.step(time[::int(len(time)/len(modulating_signal))], modulating_signal, where='post', label='Modulating Signal')
        ax1.set_title('Modulating Signal')
        ax1.set_xlabel('Time (s)')
        ax1.set_ylabel('Amplitude')
        ax1.legend()
        ax1.grid(True)

        ax2 = self.fig.add_subplot(5, 1, 2, sharex=ax1)
        ax2.plot(time, carrier_signal_i, label=f'Carrier I (Fc={carrier_freq} Hz)', color='orange')
        ax2.set_title(f'Carrier I (Fc={carrier_freq} Hz)')
        ax2.set_xlabel('Time (s)')
        ax2.set_ylabel('Amplitude')
        ax2.legend()
        ax2.grid(True)

        ax3 = self.fig.add_subplot(5, 1, 3, sharex=ax1)
        ax3.plot(time, carrier_signal_q, label=f'Carrier Q (Fc={carrier_freq} Hz)', color='green')
        ax3.set_title(f'Carrier Q (Fc={carrier_freq} Hz)')
        ax3.set_xlabel('Time (s)')
        ax3.set_ylabel('Amplitude')
        ax3.legend()
        ax3.grid(True)

        ax4 = self.fig.add_subplot(5, 1, 4, sharex=ax1)
        ax4.plot(time, np.real(qam_signal), label='QAM Signal (Real)', color='red')
        ax4.set_title('QAM Signal (Real)')
        ax4.set_xlabel('Time (s)')
        ax4.set_ylabel('Amplitude')
        ax4.legend()
        ax4.grid(True)

        ax5 = self.fig.add_subplot(5, 1, 5, sharex=ax1)
        ax5.plot(time, np.imag(qam_signal), label='QAM Signal (Imag)', color='purple')
        ax5.set_title('QAM Signal (Imag)')
        ax5.set_xlabel('Time (s)')
        ax5.set_ylabel('Amplitude')
        ax5.legend()
        ax5.grid(True)
        self.fig.tight_layout()

    def plot_fm_signals(self, time, message_signal, carrier_signal, fm_signal, carrier_freq, freq_deviation):
        """!
        @brief Plot the message signal, carrier signal, and FM modulated signal.

        @param time (np.array): Time vector for the signals.
        @param message_signal (np.array): The base message signal.
        @param carrier_signal (np.array): The carrier signal.
        @param fm_signal (np.array): The FM modulated signal.
        @param carrier_freq (float): Frequency of the carrier signal in Hz.
        @param freq_deviation (float): Frequency deviation in Hz.
        """
        
        self.ax.clear()
        
        
        ax1 = self.fig.add_subplot(3, 1, 1)
        ax1.plot(time, message_signal, label='Message Signal')
        ax1.set_title('Message Signal')
        ax1.set_xlabel('Time (s)')
        ax1.set_ylabel('Amplitude')
        ax1.legend()
        ax1.grid(True)

        ax2 = self.fig.add_subplot(3, 1, 2, sharex=ax1)
        ax2.plot(time, carrier_signal, label=f'Carrier (Fc={carrier_freq} Hz)', color='orange')
        ax2.set_title(f'Carrier Signal (Fc={carrier_freq} Hz)')
        ax2.set_xlabel('Time (s)')
        ax2.set_ylabel('Amplitude')
        ax2.legend()
        ax2.grid(True)

        ax3 = self.fig.add_subplot(3, 1, 3, sharex=ax1)
        ax3.plot(time, fm_signal, label=f'FM Signal (\\Delta f={freq_deviation} Hz)', color='green')
        ax3.set_title(f'FM Signal (\\Delta f={freq_deviation} Hz)')
        ax3.set_xlabel('Time (s)')
        ax3.set_ylabel('Amplitude')
        ax3.legend()
        ax3.grid(True)
        self.fig.tight_layout()

    def plot_ask_signals(self, time, bw, sint, st):
        """!
        @brief Plot the digital signal, carrier signal, and ASK modulated signal.

        @param time (np.array): Time vector for the signal.
        @param bw (np.array): Repeated binary sequence.
        @param sint (np.array): Carrier sinusoidal signal.
        @param st (np.array): ASK modulated signal.
        """
        self.ax.clear()
        
        ax1 = self.fig.add_subplot(3, 1, 1)
        ax1.step(time, bw, label='Digital Signal', where='post')
        ax1.set_title('Digital Signal')
        ax1.set_xlabel('Time (s)')
        ax1.set_ylabel('Amplitude')
        ax1.legend()
        ax1.grid(True)

        ax2 = self.fig.add_subplot(3, 1, 2, sharex=ax1)
        ax2.plot(time, sint, label='Carrier Signal', color='orange')
        ax2.set_title('Carrier Signal')
        ax2.set_xlabel('Time (s)')
        ax2.set_ylabel('Amplitude')
        ax2.legend()
        ax2.grid(True)

        ax3 = self.fig.add_subplot(3, 1, 3, sharex=ax1)
        ax3.plot(time, st, label='ASK Signal', color='green')
        ax3.set_title('ASK Signal')
        ax3.set_xlabel('Time (s)')
        ax3.set_ylabel('Amplitude')
        ax3.legend()
        ax3.grid(True)
        self.fig.tight_layout()

    def plot_qpsk_signals(self, time, modulating_signal, carrier_signal_i, carrier_signal_q, qpsk_signal, carrier_freq):
        """!
        @brief Plot the modulating signal, carrier signals, and the QPSK modulated signal.

        @param time (np.array): Time vector for the signals.
        @param modulating_signal (np.array): Complex representation of the constellation points over time.
        @param carrier_signal_i (np.array): In-phase carrier signal.
        @param carrier_signal_q (np.array): Quadrature carrier signal.
        @param qpsk_signal (np.array): QPSK modulated signal.
        @param carrier_freq (float): Frequency of carrier signal (Hz).
        """
        
        self.ax.clear()
        
        
        ax1 = self.fig.add_subplot(5, 1, 1)
        ax1.step(time[::int(len(time)/len(modulating_signal))], np.real(modulating_signal), where='post', linewidth=1.5, color='blue', label='Real')
        
        ax1.step(time[::int(len(time)/len(modulating_signal))], np.imag(modulating_signal), where='post', linewidth=1.5, color='red', label='Imaginary')
        ax1.set_title('Modulating Signal (Constellation Points)')
        ax1.set_xlabel('Time (s)')
        ax1.set_ylabel('Amplitude')
        ax1.legend()
        ax1.grid(True)

        ax2 = self.fig.add_subplot(5, 1, 2, sharex=ax1)
        ax2.plot(time, carrier_signal_i, label=f'Carrier I (Fc={carrier_freq} Hz)', color='orange')
        ax2.set_title(f'Carrier I (Fc={carrier_freq} Hz)')
        ax2.set_xlabel('Time (s)')
        ax2.set_ylabel('Amplitude')
        ax2.legend()
        ax2.grid(True)

        ax3 = self.fig.add_subplot(5, 1, 3, sharex=ax1)
        ax3.plot(time, carrier_signal_q, label=f'Carrier Q (Fc={carrier_freq} Hz)', color='green')
        ax3.set_title(f'Carrier Q (Fc={carrier_freq} Hz)')
        ax3.set_xlabel('Time (s)')
        ax3.set_ylabel('Amplitude')
        ax3.legend()
        ax3.grid(True)

        ax4 = self.fig.add_subplot(5, 1, 4, sharex=ax1)
        ax4.plot(time, np.real(qpsk_signal), label='QPSK Signal (Real)', color='red')
        ax4.set_title('QPSK Signal (Real)')
        ax4.set_xlabel('Time (s)')
        ax4.set_ylabel('Amplitude')
        ax4.legend()
        ax4.grid(True)

        ax5 = self.fig.add_subplot(5, 1, 5, sharex=ax1)
        ax5.plot(time, np.imag(qpsk_signal), label='QPSK Signal (Imag)', color='purple')
        ax5.set_title('QPSK Signal (Imag)')
        ax5.set_xlabel('Time (s)')
        ax5.set_ylabel('Amplitude')
        ax5.legend()
        ax5.grid(True)
        self.fig.tight_layout()

if __name__ == "__main__":
    root = tk.Tk()
    gui = ModulationGUI(root)
    root.mainloop()
