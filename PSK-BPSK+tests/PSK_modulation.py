import numpy as np
import matplotlib.pyplot as plt

def psk_modulation(binary_data, carrier_freq, sample_rate, bit_duration):
    """!
    @brief Perform Phase-Shift Keying (PSK) modulation.
    
    @param binary_data The binary data sequence to be modulated (e.g., [1, 0, 1]).
    @param carrier_freq Carrier frequency (Hz).
    @param sample_rate Sampling rate for the signal (Hz).
    @param bit_duration Duration of each bit (seconds).
    
    @return A tuple containing:
        - time: Time vector for the entire signal duration.
        - modulating_signal: Binary sitgnal expanded over time.
        - carrier_signal: Continuous carrier signal.
        - psk_signal: PSK modulated signal.
    
    @code
    binary_data = [1, 0, 1, 0]
    carrier_freq = 5  # Hz
    sample_rate = 1000  # Hz
    bit_duration = 1    # second

    time, modulating_signal, carrier_signal, psk_signal = psk_modulation(
        binary_data, carrier_freq, sample_rate, bit_duration)
    @endcode
    
    @details
    This function generates a time vector, the modulating binary signal, the continuous carrier signal,
    and the resulting PSK modulated signal, all based on the input parameters.
    """
    # Create a time vector for the entire signal duration.
    time = np.arange(0, len(binary_data) * bit_duration, 1 / sample_rate)
    signal_length = len(time)

    # Create a time vector for the duration of one bit.
    bit_time = np.linspace(0, bit_duration, int(sample_rate * bit_duration), endpoint=False)

    # Initialize the modulating signal (binary sequence spread over time) and the PSK signal.
    modulating_signal = np.zeros(signal_length)
    psk_signal = np.zeros(signal_length)

    # Precompute continuous carrier signal for visualization.
    carrier_signal = np.sin(2 * np.pi * carrier_freq * time)

    # Loop over each bit in the binary data to create the PSK modulated signal.
    for i, bit in enumerate(binary_data):
        # Calculate the indices corresponding to this bit's duration in the signal.
        start_idx = int(i * bit_duration * sample_rate)
        end_idx = int((i + 1) * bit_duration * sample_rate)

        # Assign the bit value to the modulating signal.
        modulating_signal[start_idx:end_idx] = bit

        # Modulate this bit using the corresponding phase shift.
        if bit == 0:
            psk_signal[start_idx:end_idx] = np.sin(2 * np.pi * carrier_freq * bit_time)
        elif bit == 1:
            psk_signal[start_idx:end_idx] = np.sin(2 * np.pi * carrier_freq * bit_time + np.pi)
        else:
            # Raise an error if the input contains values other than 0 or 1.
            raise ValueError("Input data must be binary (0s and 1s only).")

    return time, modulating_signal, carrier_signal, psk_signal

def plot_psk_signals(time, modulating_signal, carrier_signal, psk_signal, carrier_freq):
    """!
    @brief Plot the modulating signal, carrier signal, and the PSK modulated signal.
    
    @param time Time vector for the signals.
    @param modulating_signal Binary modulating signal over time.
    @param carrier_signal Carrier signal.
    @param psk_signal PSK modulated signal.
    @param carrier_freq Frequency of carrier signal (Hz).
    
    @code
    time, modulating_signal, carrier_signal, psk_signal = psk_modulation(
        [1, 0, 1, 0], 5, 1000, 1)
    plot_psk_signals(time, modulating_signal, carrier_signal, psk_signal, 5)
    @endcode
    """
    plt.figure(figsize=(12, 8))

    # Modulating signal (binary data)
    plt.subplot(3, 1, 1)
    plt.step(time, modulating_signal, where='post', linewidth=1.5, color='blue')
    plt.title('Modulating Signal (Binary Data)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.ylim(-0.5, 1.5)
    plt.grid(True)

    # Carrier signal
    plt.subplot(3, 1, 2)
    plt.plot(time, carrier_signal, color='green')
    plt.title(f'Carrier Signal (Frequency = {carrier_freq} Hz)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    # PSK modulated signal
    plt.subplot(3, 1, 3)
    plt.plot(time, psk_signal, color='orange')
    plt.title('PSK Modulated Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def main_psk():
    """!
    @brief Main function to perform PSK modulation and plot the signals.
    
    @details
    Steps:
        1. Accept binary input from the user.
        2. Set PSK modulation parameters.
        3. Perform PSK modulation.
        4. Plot the resulting signals.
    """
    # Input binary sequence as comma-separated values (e.g., 1,0,1,0).
    binary_data = input("Enter binary sequence (e.g., 1, 0, 1, 0): ")
    binary_data = list(map(int, binary_data.strip().split(',')))

    # Define PSK modulation parameters.
    carrier_freq = 5  # Carrier frequency (Hz).
    sample_rate = 1000  # Sampling rate (Hz).
    bit_duration = 1    # Duration of each bit (seconds).

    # Perform PSK modulation.
    time, modulating_signal, carrier_signal, psk_signal = psk_modulation(
        binary_data, carrier_freq, sample_rate, bit_duration)

    # Plot the modulated signals.
    plot_psk_signals(time, modulating_signal, carrier_signal, psk_signal, carrier_freq)

# --------------------
if __name__ == "__main__":
    main_psk()
