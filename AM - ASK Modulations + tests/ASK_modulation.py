# Code for ASK Modulation
# --------------------
import numpy as np  # Provides mathematical functions like pi (np.pi) and sine (np.sin).
import matplotlib.pyplot as plt  # Enables plotting of graphs.


# --------------------
def ask_modulation(binary_sequence):
    """
    Generates ASK (Amplitude Shift Keying) modulation components for a given binary sequence.

    Parameters:
        binary_sequence (list): A binary sequence (e.g., [1, 0, 1, 0]).

    Returns:
        tuple: Contains the following:
            - t (numpy array): Time vector for the signal.
            - bw (numpy array): Repeated binary sequence to match the signal duration.
            - sint (numpy array): Carrier sinusoidal signal.
            - st (numpy array): ASK modulated signal.
    """
    n = len(binary_sequence)  # Length of the binary sequence.
    bw = np.repeat(binary_sequence, 100)  # Each bit is repeated 100 times.
    t = np.linspace(0, n, len(bw))  # Time vector from 0 to n with len(bw) points.
    sint = np.sin(2 * np.pi * t)  # Carrier sinusoidal signal.
    st = bw * sint  # ASK modulated signal is the product of the binary signal and the sinusoidal signal.
    return t, bw, sint, st  # Return the components.


# --------------------
def plot_ask_signals(t, bw, sint, st):
    """
    Plots the digital signal, carrier signal, and ASK modulated signal.

    Parameters:
        t (numpy array): Time vector for the signal.
        bw (numpy array): Repeated binary sequence.
        sint (numpy array): Carrier sinusoidal signal.
        st (numpy array): ASK modulated signal.
    """
    plt.figure(figsize=(10, 5))  # Set the figure size.

    # Plot the digital signal.
    plt.subplot(3, 1, 1)  # 3 rows, 1 column, first plot.
    plt.plot(t, bw, linewidth=1.5)  # Plot the digital signal.
    plt.grid(True)  # Enable grid.
    plt.axis([0, max(t), -2, 2])  # Set x and y axis limits.
    plt.title('Digital Signal')  # Title of the plot.
    plt.xlabel('Time')  # Label for the x-axis.
    plt.ylabel('Amplitude')  # Label for the y-axis.

    # Plot the carrier signal.
    plt.subplot(3, 1, 2)
    plt.plot(t, sint, linewidth=1.5)
    plt.grid(True)
    plt.axis([0, max(t), -2, 2])
    plt.title('Carrier Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')

    # Plot the ASK modulated signal.
    plt.subplot(3, 1, 3)
    plt.plot(t, st, linewidth=1.5)
    plt.grid(True)
    plt.axis([0, max(t), -2, 2])
    plt.title('ASK Modulated Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')

    plt.tight_layout()  # Adjust layout to prevent overlapping.
    plt.show()  # Display the plot.


# --------------------
if __name__ == "__main__":
    """
    Main execution block. Prompts the user for a binary sequence, performs ASK modulation, 
    and plots the results.
    """
    binary_sequence = input(
        "Enter a binary sequence in the format [1, 0, 1, 0] with brackets, commas, and spaces: ")
    # Convert user input into a list of integers.
    binary_sequence = list(map(int, binary_sequence.strip('[]').split(",")))

    # Perform ASK modulation and obtain the components.
    t, bw, sint, st = ask_modulation(binary_sequence)

    # Plot the ASK signals.
    plot_ask_signals(t, bw, sint, st)
