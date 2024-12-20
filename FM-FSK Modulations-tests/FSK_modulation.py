import numpy as np
import matplotlib.pyplot as plt


# --------------------
def fsk_modulation(binary_data, carrier_freq_0, carrier_freq_1, sample_rate, bit_duration):
    """
    Perform Frequency-Shift Keying (FSK) modulation.

    Parameters:
        binary_data (list of int): The binary data sequence to be modulated (e.g., [1, 0, 1]).
        carrier_freq_0 (float): Carrier frequency corresponding to binary 0 (Hz).
        carrier_freq_1 (float): Carrier frequency corresponding to binary 1 (Hz).
        sample_rate (float): Sampling rate for the signal (Hz).
        bit_duration (float): Duration of each bit (seconds).

    Returns:
        tuple: A tuple containing the following:
            - time (numpy.ndarray): Time vector for the entire signal duration.
            - modulating_signal (numpy.ndarray): Binary signal expanded over time.
            - carrier_signal_0 (numpy.ndarray): Continuous carrier signal for binary 0.
            - carrier_signal_1 (numpy.ndarray): Continuous carrier signal for binary 1.
            - fsk_signal (numpy.ndarray): FSK modulated signal.
    """
    # Time vector for the entire signal duration.
    time = np.arange(0, len(binary_data) * bit_duration, 1 / sample_rate)
    signal_length = len(time)

    # Create a time vector for one bit duration.
    bit_time = np.linspace(0, bit_duration, int(sample_rate * bit_duration), endpoint=False)

    # Initialize the modulating signal and the FSK signal.
    modulating_signal = np.zeros(signal_length)
    fsk_signal = np.zeros(signal_length)

    # Carrier signals (continuous for visualization purposes).
    carrier_signal_0 = np.sin(2 * np.pi * carrier_freq_0 * time)
    carrier_signal_1 = np.sin(2 * np.pi * carrier_freq_1 * time)

    # Generate the FSK signal by mapping each bit to its corresponding carrier frequency.
    for i, bit in enumerate(binary_data):
        # Determine the start and end indices for this bit in the signal.
        start_idx = int(i * bit_duration * sample_rate)
        end_idx = int((i + 1) * bit_duration * sample_rate)

        # Assign the binary bit to the modulating signal.
        modulating_signal[start_idx:end_idx] = bit

        # Generate the corresponding carrier for this bit and add it to the FSK signal.
        if bit == 0:
            fsk_signal[start_idx:end_idx] = np.sin(2 * np.pi * carrier_freq_0 * bit_time)
        elif bit ==1:
            fsk_signal[start_idx:end_idx] = np.sin(2 * np.pi * carrier_freq_1 * bit_time)
        else :
            raise ValueError("Input data must be binary (0s and 1s only).")

    return time, modulating_signal, carrier_signal_0, carrier_signal_1, fsk_signal


# --------------------
def plot_fsk_signals(time, modulating_signal, carrier_signal_0, carrier_signal_1, fsk_signal, carrier_freq_0,
                     carrier_freq_1):
    """
    Plot the modulating signal, carrier signals, and the FSK modulated signal.

    Parameters:
        time (numpy.ndarray): Time vector for the signals.
        modulating_signal (numpy.ndarray): Binary modulating signal over time.
        carrier_signal_0 (numpy.ndarray): Carrier signal for binary 0.
        carrier_signal_1 (numpy.ndarray): Carrier signal for binary 1.
        fsk_signal (numpy.ndarray): FSK modulated signal.
        carrier_freq_0 (float): Frequency of carrier signal for binary 0 (Hz).
        carrier_freq_1 (float): Frequency of carrier signal for binary 1 (Hz).
    """
    plt.figure(figsize=(12, 8))  # Define the figure size for better visibility.

    # Plot the modulating signal (binary data).
    plt.subplot(4, 1, 1)
    plt.step(time, modulating_signal, where='post', linewidth=1.5, color='blue')
    plt.title('Modulating Signal (Binary Data)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.ylim(-0.5, 1.5)  # Limit y-axis for binary signal.
    plt.grid(True)

    # Plot the carrier signal for binary 0.
    plt.subplot(4, 1, 2)
    plt.plot(time, carrier_signal_0, color='green')
    plt.title(f'Carrier Signal for Binary 0 (Frequency = {carrier_freq_0} Hz)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    # Plot the carrier signal for binary 1.
    plt.subplot(4, 1, 3)
    plt.plot(time, carrier_signal_1, color='purple')
    plt.title(f'Carrier Signal for Binary 1 (Frequency = {carrier_freq_1} Hz)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    # Plot the FSK modulated signal.
    plt.subplot(4, 1, 4)
    plt.plot(time, fsk_signal, color='orange')
    plt.title('FSK Modulated Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    plt.tight_layout()  # Adjust subplot spacing for clarity.
    plt.show()


# --------------------
def main_fsk():
    """
    Main function to perform FSK modulation and plot the signals.

    Steps:
        1. Accept binary input from the user.
        2. Set FSK modulation parameters.
        3. Perform FSK modulation.
        4. Plot the resulting signals.
    """
    # Prompt the user to input a binary sequence (comma-separated).
    binary_data = input("Enter binary sequence (e.g., 1, 0, 1, 0): ")
    binary_data = list(map(int, binary_data.strip().split(',')))

    # Define modulation parameters.
    carrier_freq_0 = 5  # Frequency for binary 0 (Hz).
    carrier_freq_1 = 10  # Frequency for binary 1 (Hz).
    sample_rate = 1000  # Sampling rate (Hz).
    bit_duration = 1  # Duration of each bit (seconds).

    # Perform FSK modulation.
    time, modulating_signal, carrier_signal_0, carrier_signal_1, fsk_signal = fsk_modulation(
        binary_data, carrier_freq_0, carrier_freq_1, sample_rate, bit_duration)

    # Plot the resulting signals.
    plot_fsk_signals(time, modulating_signal, carrier_signal_0, carrier_signal_1, fsk_signal, carrier_freq_0,
                     carrier_freq_1)


# --------------------
if __name__ == "__main__":
    main_fsk()  # Call the main function.



