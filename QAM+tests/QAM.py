import numpy as np
import matplotlib.pyplot as plt

def qam_modulation(binary_data, carrier_freq, sample_rate, bit_duration, constellation_points):
    """!
    @brief Perform Quadrature Amplitude Modulation (QAM).
    
    @param binary_data The binary data sequence to be modulated (e.g., [1, 0, 1, 0]).
    @param carrier_freq Carrier frequency (Hz).
    @param sample_rate Sampling rate for the signal (Hz).
    @param bit_duration Duration of each bit (seconds).
    @param constellation_points A list of complex numbers representing the constellation points.
    
    @return A tuple containing:
        - time: Time vector for the entire signal duration.
        - modulating_signal: Integer representation of the constellation points over time.
        - carrier_signal_i: In-phase carrier signal.
        - carrier_signal_q: Quadrature carrier signal.
        - qam_signal: QAM modulated signal.
    
    @code
    binary_data = [0, 1, 1, 0, 1, 1, 0, 0]
    carrier_freq = 5  # Hz
    sample_rate = 1000  # Hz
    bit_duration = 1    # second
    constellation_points = [1+1j, 1-1j, -1+1j, -1-1j] # 4-QAM

    time, modulating_signal, carrier_signal_i, carrier_signal_q, qam_signal = qam_modulation(
        binary_data, carrier_freq, sample_rate, bit_duration, constellation_points)
    @endcode
    
    @details
    This function generates a time vector, the modulating signal (as constellation point indices),
    the in-phase and quadrature carrier signals, and the resulting QAM modulated signal.
    """
    # Validate constellation points
    if not isinstance(constellation_points, list) or not all(isinstance(point, complex) for point in constellation_points):
        raise ValueError("Constellation points must be a list of complex numbers.")
    
    bits_per_symbol = int(np.log2(len(constellation_points)))
    if 2**bits_per_symbol != len(constellation_points):
        raise ValueError("Number of constellation points must be a power of 2.")

    if len(binary_data) % bits_per_symbol != 0:
        raise ValueError("Length of binary data must be a multiple of bits per symbol.")

    # Create a time vector for the entire signal duration.
    time = np.arange(0, len(binary_data) / bits_per_symbol * bit_duration, 1 / sample_rate)
    signal_length = len(time)

    # Create a time vector for the duration of one symbol.
    samples_per_symbol = int(sample_rate * bit_duration)
    symbol_time = np.linspace(0, bit_duration, samples_per_symbol, endpoint=False)

    # Initialize the modulating signal (constellation point indices) and the QAM signal.
    modulating_signal = np.zeros(len(binary_data) // bits_per_symbol, dtype=int)
    qam_signal = np.zeros(signal_length, dtype=complex)

    # Precompute continuous carrier signals for visualization.
    carrier_signal_i = np.cos(2 * np.pi * carrier_freq * time)
    carrier_signal_q = np.sin(2 * np.pi * carrier_freq * time)

    # Loop over each symbol in the binary data to create the QAM modulated signal.
    for i in range(0, len(binary_data), bits_per_symbol):
        # Convert binary data to an integer index for the constellation point
        symbol_bits = binary_data[i:i + bits_per_symbol]
        symbol_index = 0
        for bit in symbol_bits:
            symbol_index = (symbol_index << 1) | bit
        
        modulating_signal[i // bits_per_symbol] = symbol_index

        # Calculate the indices corresponding to this symbol's duration in the signal.
        start_idx = (i // bits_per_symbol) * samples_per_symbol
        end_idx = ((i // bits_per_symbol) + 1) * samples_per_symbol

        # Modulate this symbol using the corresponding constellation point.
        qam_signal[start_idx:end_idx] = constellation_points[symbol_index] * np.exp(1j * 2 * np.pi * carrier_freq * symbol_time)

    return time, modulating_signal, carrier_signal_i, carrier_signal_q, qam_signal

def plot_qam_signals(time, modulating_signal, carrier_signal_i, carrier_signal_q, qam_signal, carrier_freq, constellation_points):
    """!
    @brief Plot the modulating signal, carrier signals, and the QAM modulated signal.
    
    @param time Time vector for the signals.
    @param modulating_signal Integer representation of the constellation points over time.
    @param carrier_signal_i In-phase carrier signal.
    @param carrier_signal_q Quadrature carrier signal.
    @param qam_signal QAM modulated signal.
    @param carrier_freq Frequency of carrier signal (Hz).
    @param constellation_points A list of complex numbers representing the constellation points.
    
    @code
    binary_data = [0, 1, 1, 0, 1, 1, 0, 0]
    carrier_freq = 5  # Hz
    sample_rate = 1000  # Hz
    bit_duration = 1    # second
    constellation_points = [1+1j, 1-1j, -1+1j, -1-1j] # 4-QAM

    time, modulating_signal, carrier_signal_i, carrier_signal_q, qam_signal = qam_modulation(
        binary_data, carrier_freq, sample_rate, bit_duration, constellation_points)
    plot_qam_signals(time, modulating_signal, carrier_signal_i, carrier_signal_q, qam_signal, carrier_freq, constellation_points)
    @endcode
    """
    plt.figure(figsize=(12, 10))

    # Modulating signal (constellation point indices)
    plt.subplot(5, 1, 1)
    plt.step(time[::int(len(time)/len(modulating_signal))], modulating_signal, where='post', linewidth=1.5, color='blue')
    plt.title('Modulating Signal (Constellation Point Indices)')
    plt.xlabel('Time (s)')
    plt.ylabel('Index')
    plt.grid(True)

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

    # QAM modulated signal (real part)
    plt.subplot(5, 1, 4)
    plt.plot(time, np.real(qam_signal), color='orange')
    plt.title('QAM Modulated Signal (Real Part)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    # QAM modulated signal (imaginary part)
    plt.subplot(5, 1, 5)
    plt.plot(time, np.imag(qam_signal), color='red')
    plt.title('QAM Modulated Signal (Imaginary Part)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def main_qam():
    """!
    @brief Main function to perform QAM modulation and plot the signals.
    
    @details
    Steps:
        1. Accept binary input from the user.
        2. Set QAM modulation parameters.
        3. Perform QAM modulation.
        4. Plot the resulting signals.
    """
    # Define QAM modulation parameters.
    binary_data = [0, 1, 1, 0, 1, 1, 0, 0]
    carrier_freq = 5  # Carrier frequency (Hz).
    sample_rate = 1000  # Sampling rate (Hz).
    bit_duration = 1    # Duration of each bit (seconds).
    constellation_points = [1+1j, 1-1j, -1+1j, -1-1j] # 4-QAM

    # Perform QAM modulation.
    time, modulating_signal, carrier_signal_i, carrier_signal_q, qam_signal = qam_modulation(
        binary_data, carrier_freq, sample_rate, bit_duration, constellation_points)

    # Plot the modulated signals.
    plot_qam_signals(time, modulating_signal, carrier_signal_i, carrier_signal_q, qam_signal, carrier_freq, constellation_points)

if __name__ == "__main__":
    main_qam()
