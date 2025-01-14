import numpy as np
import matplotlib.pyplot as plt
import traceback

# --------------------
def fsk_modulation(binary_data, carrier_freq_0, carrier_freq_1, sample_rate, bit_duration):
    """
    Perform FSK modulation with two carrier frequencies, a sampling rate, bit duration, and binary data.
    """
    if not all(bit in [0, 1] for bit in binary_data):
        raise ValueError("Invalid binary data. Only 0s and 1s are allowed.")
    
    time = np.arange(0, len(binary_data) * bit_duration, 1 / sample_rate)  # Time vector for the signal duration.
    signal_length = len(time)

    # Create a time vector for one bit duration.
    bit_time = np.linspace(0, bit_duration, int(sample_rate * bit_duration), endpoint=False)

    # Initialize signals
    modulating_signal = np.zeros(signal_length)
    carrier_signal_0 = np.sin(2 * np.pi * carrier_freq_0 * time)
    carrier_signal_1 = np.sin(2 * np.pi * carrier_freq_1 * time)
    fsk_signal = np.zeros(signal_length)

    # Construct the FSK signal and modulating signal
    for i, bit in enumerate(binary_data):
        start_idx = int(i * bit_duration * sample_rate)
        end_idx = int((i + 1) * bit_duration * sample_rate)
        modulating_signal[start_idx:end_idx] = bit
        if bit == 0:
            fsk_signal[start_idx:end_idx] = np.sin(2 * np.pi * carrier_freq_0 * bit_time)
        else:
            fsk_signal[start_idx:end_idx] = np.sin(2 * np.pi * carrier_freq_1 * bit_time)

    return time, modulating_signal, carrier_signal_0, carrier_signal_1, fsk_signal
# --------------------
def plot_fsk_signals(time, modulating_signal, carrier_signal_0, carrier_signal_1, fsk_signal, carrier_freq_0, carrier_freq_1):
    """
    Plot the modulating signal, carrier signals, and the FSK modulated signal.
    """
    plt.figure(figsize=(12, 8))  # Define figure size.

    # Modulating signal (binary data).
    plt.subplot(4, 1, 1)
    plt.step(time, modulating_signal, where='post', linewidth=1.5, color='blue')
    plt.title('Modulating Signal (Binary Data)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.ylim(-0.5, 1.5)
    plt.grid(True)

    # Carrier signal for binary 0.
    plt.subplot(4, 1, 2)
    plt.plot(time, carrier_signal_0, color='green')
    plt.title(f'Carrier Signal for Binary 0 (Frequency = {carrier_freq_0} Hz)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    # Carrier signal for binary 1.
    plt.subplot(4, 1, 3)
    plt.plot(time, carrier_signal_1, color='purple')
    plt.title(f'Carrier Signal for Binary 1 (Frequency = {carrier_freq_1} Hz)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    # FSK modulated signal.
    plt.subplot(4, 1, 4)
    plt.plot(time, fsk_signal, color='orange')
    plt.title('FSK Modulated Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    plt.tight_layout()
    plt.show()
# --------------------
def main_fsk():
    """
    Main function for user input and FSK modulation visualization.
    """
    # User input for binary data sequence.
    binary_data = input("Enter binary sequence (e.g., 1, 0, 1, 0): ")
    binary_data = list(map(int, binary_data.strip().split(',')))

    # Set parameters for FSK modulation.
    carrier_freq_0 = 5  # Frequency for binary 0 (Hz).
    carrier_freq_1 = 10  # Frequency for binary 1 (Hz).
    sample_rate = 1000  # Sampling rate (Hz).
    bit_duration = 1  # Duration of each bit (seconds).

    # Perform FSK modulation.
    time, modulating_signal, carrier_signal_0, carrier_signal_1, fsk_signal = fsk_modulation(
        binary_data, carrier_freq_0, carrier_freq_1, sample_rate, bit_duration)

    # Plot the signals.
    plot_fsk_signals(time, modulating_signal, carrier_signal_0, carrier_signal_1, fsk_signal, carrier_freq_0, carrier_freq_1)

# --------------------
def test_sad_empty_binary_data():
    """Test with empty binary data."""
    binary_data = []
    carrier_freq_0 = 5
    carrier_freq_1 = 10
    sample_rate = 1000
    bit_duration = 1
    try:
        # Check if binary_data is empty before passing it to the modulation function
        if not binary_data:
            raise ValueError("Binary data is empty. Cannot perform modulation.")
        
        # If not empty, perform modulation (this line will not be reached for empty data)
        fsk_modulation(binary_data, carrier_freq_0, carrier_freq_1, sample_rate, bit_duration)
        
    except ValueError as e:
        print(f"Sad Path Test Failed: {str(e)}")  # Print error message to terminal
        print("Detailed traceback:")
        print(traceback.format_exc())  # Print detailed traceback

        assert "Binary data is empty" in str(e), "Error message is not as expected!"

def test_sad_invalid_binary_data():
    """Test for invalid binary data."""
    binary_data = [1, 2, 0, -1]  # Invalid binary data
    carrier_freq_0 = 5
    carrier_freq_1 = 10
    sample_rate = 1000
    bit_duration = 1
    try:
        fsk_modulation(binary_data, carrier_freq_0, carrier_freq_1, sample_rate, bit_duration)
        print("Sad Path Test Failed: Expected ValueError due to invalid binary data, but no exception was raised.")
    except ValueError as e:
        print(f"Sad Path Test Passed: {str(e)}")
        print("Detailed traceback:")
        print(traceback.format_exc())  # Print detailed traceback

        assert "Invalid binary data" in str(e), "Error message is not as expected!"

