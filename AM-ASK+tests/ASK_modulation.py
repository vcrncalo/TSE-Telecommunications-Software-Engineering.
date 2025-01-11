import numpy as np  # Provides mathematical functions like pi (np.pi) and sine (np.sin).
import matplotlib.pyplot as plt  # Enables plotting of graphs.

def ask_modulation(binary_sequence):
    """!
    @brief Generates ASK (Amplitude Shift Keying) modulation components for a given binary sequence.

    @param binary_sequence A binary sequence (e.g., [1, 0, 1, 0]).
    
    @return A tuple containing:
        - t (numpy array): Time vector for the signal.
        - bw (numpy array): Repeated binary sequence to match the signal duration.
        - sint (numpy array): Carrier sinusoidal signal.
        - st (numpy array): ASK modulated signal.

    @code
    binary_sequence = [1, 0, 1, 0]
    t, bw, sint, st = ask_modulation(binary_sequence)
    print(len(t), len(bw))  # Outputs: 400 400
    @endcode
    """
    n = len(binary_sequence)  # Length of the binary sequence.
    bw = np.repeat(binary_sequence, 100)  # Each bit is repeated 100 times.
    t = np.linspace(0, n, len(bw))  # Time vector from 0 to n with len(bw) points.
    sint = np.sin(2 * np.pi * t)  # Carrier sinusoidal signal.
    st = bw * sint  # ASK modulated signal is the product of the binary signal and the sinusoidal signal.
    return t, bw, sint, st  # Return the components.

def plot_ask_signals(t, bw, sint, st):
    """!
    @brief Plots the digital signal, carrier signal, and ASK modulated signal.

    @param t Time vector for the signal.
    @param bw Repeated binary sequence.
    @param sint Carrier sinusoidal signal.
    @param st ASK modulated signal.

    @code
    binary_sequence = [1, 0, 1, 0]
    t, bw, sint, st = ask_modulation(binary_sequence)
    plot_ask_signals(t, bw, sint, st)
    @endcode
    """
    plt.figure(figsize=(10, 5))

    # Plot the digital signal.
    plt.subplot(3, 1, 1)
    plt.plot(t, bw, linewidth=1.5)
    plt.grid(True)
    plt.axis([0, max(t), -2, 2])
    plt.title('Digital Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')

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
    plt.show()

if __name__ == "__main__":
    """!
    @brief Main execution block. Prompts the user for a binary sequence, performs ASK modulation, 
    and plots the results.

    @code
    Enter a binary sequence when prompted (e.g., [1, 0, 1, 0]).
    The program will display the plots for the digital signal, carrier signal, and modulated signal.
    @endcode
    """
    binary_sequence = input(
        "Enter a binary sequence in the format [1, 0, 1, 0] with brackets, commas, and spaces: ")
    binary_sequence = list(map(int, binary_sequence.strip('[]').split(",")))

    # Perform ASK modulation and obtain the components.
    t, bw, sint, st = ask_modulation(binary_sequence)

    # Plot the ASK signals.
    plot_ask_signals(t, bw, sint, st)
