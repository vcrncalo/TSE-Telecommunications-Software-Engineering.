import numpy as np
import matplotlib.pyplot as plt

def qpsk_modulation(binary_data, carrier_freq, sample_rate, bit_duration):
    """!
    @brief Perform Quadrature Phase Shift Keying (QPSK) modulation.
    
    @param binary_data The binary data sequence to be modulated (e.g., [1, 0, 1, 0]).
    @param carrier_freq Carrier frequency (Hz).
    @param sample_rate Sampling rate for the signal (Hz).
    @param bit_duration Duration of each bit (seconds).
    
    @return A tuple containing:
        - time: Time vector for the entire signal duration.
        - modulating_signal: Complex representation of the constellation points over time.
        - carrier_signal_i: In-phase carrier signal.
        - carrier_signal_q: Quadrature carrier signal.
        - qpsk_signal: QPSK modulated signal.
    
    @code
    binary_data = [0, 1, 1, 0, 1, 1, 0, 0]
    carrier_freq = 5  # Hz
    sample_rate = 1000  # Hz
    bit_duration = 1    # second

    time, modulating_signal, carrier_signal_i, carrier_signal_q, qpsk_signal = qpsk_modulation(
        binary_data, carrier_freq, sample_rate, bit_duration)
    @endcode
    
    @details
    This function generates a time vector, the modulating signal (as complex constellation points),
    the in-phase and quadrature carrier signals, and the resulting QPSK modulated signal.
    The constellation points for QPSK are fixed to [1+0j, 0+1j, -1+0j, 0-1j].
    """
    constellation_points = [1+0j, 0+1j, -1+0j, 0-1j] # QPSK constellation
    bits_per_symbol = 2 # QPSK always has 2 bits per symbol

    if len(binary_data) % bits_per_symbol != 0:
        raise ValueError("Length of binary data must be a multiple of 2 for QPSK.")

    # Create a time vector for the entire signal duration.
    time = np.arange(0, len(binary_data) / bits_per_symbol * bit_duration, 1 / sample_rate)
    signal_length = len(time)

    # Create a time vector for the duration of one symbol.
    samples_per_symbol = int(sample_rate * bit_duration)
    symbol_time = np.linspace(0, bit_duration, samples_per_symbol, endpoint=False)

    # Initialize the modulating signal (constellation points) and the QPSK signal.
    modulating_signal = np.zeros(len(binary_data) // bits_per_symbol, dtype=complex)
    qpsk_signal = np.zeros(signal_length, dtype=complex)

    # Precompute continuous carrier signals for visualization.
    carrier_signal_i = np.cos(2 * np.pi * carrier_freq * time)
    carrier_signal_q = np.sin(2 * np.pi * carrier_freq * time)

    # Loop over each symbol in the binary data to create the QPSK modulated signal.
    for i in range(0, len(binary_data), bits_per_symbol):
        # Convert binary data to an integer index for the constellation point
        symbol_bits = binary_data[i:i + bits_per_symbol]
        symbol_index = 0
        for bit in symbol_bits:
            symbol_index = (symbol_index << 1) | bit
        
        modulating_signal[i // bits_per_symbol] = constellation_points[symbol_index]

        # Calculate the indices corresponding to this symbol's duration in the signal.
        start_idx = (i // bits_per_symbol) * samples_per_symbol
        end_idx = ((i // bits_per_symbol) + 1) * samples_per_symbol

        # Modulate this symbol using the corresponding constellation point.
        qpsk_signal[start_idx:end_idx] = constellation_points[symbol_index] * np.exp(1j * 2 * np.pi * carrier_freq * symbol_time)

    return time, modulating_signal, carrier_signal_i, carrier_signal_q, qpsk_signal

def plot_qpsk_signals(time, modulating_signal, carrier_signal_i, carrier_signal_q, qpsk_signal, carrier_freq):
    """!
    @brief Plot the modulating signal, carrier signals, and the QPSK modulated signal.
    
    @param time Time vector for the signals.
    @param modulating_signal Complex representation of the constellation points over time.
    @param carrier_signal_i In-phase carrier signal.
    @param carrier_signal_q Quadrature carrier signal.
    @param qpsk_signal QPSK modulated signal.
    @param carrier_freq Frequency of carrier signal (Hz).
    
    @code
    binary_data = [0, 1, 1, 0, 1, 1, 0, 0]
    carrier_freq = 5  # Hz
    sample_rate = 1000  # Hz
    bit_duration = 1    # second

    time, modulating_signal, carrier_signal_i, carrier_signal_q, qpsk_signal = qpsk_modulation(
        binary_data, carrier_freq, sample_rate, bit_duration)
    plot_qpsk_signals(time, modulating_signal, carrier_signal_i, carrier_signal_q, qpsk_signal, carrier_freq)
    @endcode
    """
    plt.figure(figsize=(12, 10))

    # Modulating signal (constellation points)
    plt.subplot(5, 1, 1)
    plt.step(time[::int(len(time)/len(modulating_signal))], np.real(modulating_signal), where='post', linewidth=1.5, color='blue', label='Real')
    plt.step(time[::int(len(time)/len(modulating_signal))], np.imag(modulating_signal), where='post', linewidth=1.5, color='red', label='Imaginary')
    plt.title('Modulating Signal (Constellation Points)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend()

    # In-phase carrier signal
    plt.subplot(5, 1, 2)
    plt.plot(time, carrier_signal_i, color='green')
    plt.title(f'In-phase Carrier Signal (Frequency = {carrier_freq} Hz)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    # Quadrature carrier signal
    plt.subplot(5, 1, 3)
    plt.plot(time, carrier_signal_q, color='purple')
    plt.title(f'Quadrature Carrier Signal (Frequency = {carrier_freq} Hz)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    # QPSK modulated signal (real part)
    plt.subplot(5, 1, 4)
    plt.plot(time, np.real(qpsk_signal), color='orange')
    plt.title('QPSK Modulated Signal (Real Part)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    # QPSK modulated signal (imaginary part)
    plt.subplot(5, 1, 5)
    plt.plot(time, np.imag(qpsk_signal), color='red')
    plt.title('QPSK Modulated Signal (Imaginary Part)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def main_qpsk():
    """!
    @brief Main function to perform QPSK modulation and plot the signals.
    
    @details
    Steps:
        1. Accept binary input from the user.
        2. Set QPSK modulation parameters.
        3. Perform QPSK modulation.
        4. Plot the resulting signals.
    """
    # Define QPSK modulation parameters.
    binary_data = [0, 1, 1, 0, 1, 1, 0, 0]
    carrier_freq = 5  # Carrier frequency (Hz).
    sample_rate = 1000  # Sampling rate (Hz).
    bit_duration = 1    # Duration of each bit (seconds).

    # Perform QPSK modulation.
    time, modulating_signal, carrier_signal_i, carrier_signal_q, qpsk_signal = qpsk_modulation(
        binary_data, carrier_freq, sample_rate, bit_duration)

    # Plot the modulated signals.
    plot_qpsk_signals(time, modulating_signal, carrier_signal_i, carrier_signal_q, qpsk_signal, carrier_freq)

if __name__ == "__main__":
    main_qpsk()
