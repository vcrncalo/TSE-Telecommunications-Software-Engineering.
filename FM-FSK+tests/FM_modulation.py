import numpy as np
import matplotlib.pyplot as plt

def fm_modulation(carrier_freq, sample_rate, duration, freq_deviation):
    """!
    @brief Perform Frequency Modulation (FM) of a message signal.
    
    @param carrier_freq Carrier frequency in Hz.
    @param sample_rate Sampling rate for signal generation in Hz.
    @param duration Duration of the signal in seconds.
    @param freq_deviation Frequency deviation (maximum shift from carrier frequency in Hz).
    
    @return A tuple containing:
        - time: Time vector for the entire signal.
        - message_signal: The base message signal (a simple sine wave).
        - carrier_signal: The carrier signal before modulation.
        - fm_signal: The resulting FM modulated signal.
    
    @code
    carrier_freq = 10
    sample_rate = 1000
    duration = 2
    freq_deviation = 5
    time, message_signal, carrier_signal, fm_signal = fm_modulation(carrier_freq, sample_rate, duration, freq_deviation)
    @endcode
    """
    # Validate input parameters.
    if not isinstance(carrier_freq, (int, float)) or carrier_freq <= 0:
        raise ValueError("Carrier frequency must be a positive number.")
    if not isinstance(sample_rate, (int, float)) or sample_rate <= 0:
        raise ValueError("Sample rate must be a positive number.")
    if not isinstance(duration, (int, float)) or duration <= 0:
        raise ValueError("Duration must be a positive number.")
    if not isinstance(freq_deviation, (int, float)) or freq_deviation <= 0:
        raise ValueError("Frequency deviation must be a positive number.")

    # Generate a time vector for the signal.
    time = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # Create a message signal: a simple sine wave with frequency 1 Hz.
    message_signal = np.sin(2 * np.pi * time)

    # Generate the carrier signal: a sine wave with the given carrier frequency.
    carrier_signal = np.sin(2 * np.pi * carrier_freq * time)

    # Compute the integral of the message signal (numerical approximation).
    integral_message = np.cumsum(message_signal) * (1 / sample_rate)

    # Apply FM modulation: frequency deviation is added to the phase of the carrier.
    fm_signal = np.sin(2 * np.pi * carrier_freq * time + 2 * np.pi * freq_deviation * integral_message)

    return time, message_signal, carrier_signal, fm_signal

def plot_fm_signals(time, message_signal, carrier_signal, fm_signal, carrier_freq, freq_deviation):
    """!
    @brief Plot the message signal, carrier signal, and FM modulated signal.
    
    @param time Time vector for the signals.
    @param message_signal The base message signal.
    @param carrier_signal The carrier signal before modulation.
    @param fm_signal The resulting FM modulated signal.
    @param carrier_freq Carrier frequency in Hz.
    @param freq_deviation Frequency deviation in Hz.
    
    @code
    plot_fm_signals(time, message_signal, carrier_signal, fm_signal, carrier_freq=10, freq_deviation=5)
    @endcode
    """
    # Set up the figure and plot the signals in subplots.
    plt.figure(figsize=(12, 8))

    # Plot the message signal.
    plt.subplot(3, 1, 1)
    plt.plot(time, message_signal)
    plt.title('Message Signal: sin(2*pi*t)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    # Plot the carrier signal.
    plt.subplot(3, 1, 2)
    plt.plot(time, carrier_signal)
    plt.title(f'Carrier Signal: sin(2*pi*Fc*t), Fc = {carrier_freq} Hz')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    # Plot the FM modulated signal.
    plt.subplot(3, 1, 3)
    plt.plot(time, fm_signal)
    plt.title(f'FM Signal, Fc = {carrier_freq} Hz, Δf = {freq_deviation} Hz')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)

    plt.tight_layout()  # Adjust layout to prevent overlap.
    plt.show()

def main_fm():
    """!
    @brief Main function to execute FM modulation and visualize the results.
    
    Executes the FM modulation process and plots the message, carrier, and modulated signals.
    
    @code
    This function automatically executes when the script runs and plots the signals.
    Parameters used: carrier_freq=10, sample_rate=1000, duration=2, freq_deviation=5.
    @endcode
    """
    # Define FM modulation parameters.
    carrier_freq = 10       # Carrier frequency (Hz).
    sample_rate = 1000      # Sampling rate (Hz).
    duration = 2            # Duration of the signal (seconds).
    freq_deviation = 5      # Frequency deviation (Hz).

    # Perform FM modulation.
    time, message_signal, carrier_signal, fm_signal = fm_modulation(
        carrier_freq, sample_rate, duration, freq_deviation)

    # Plot the modulated signals.
    plot_fm_signals(time, message_signal, carrier_signal, fm_signal, carrier_freq, freq_deviation)

if __name__ == "__main__":
    main_fm()  # Run the main FM modulation function.
