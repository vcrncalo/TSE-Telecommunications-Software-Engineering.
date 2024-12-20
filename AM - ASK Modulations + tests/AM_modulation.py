import numpy as np  # For mathematical operations and generating signals.
import matplotlib.pyplot as plt  # For creating plots similar to those in MATLAB.

# --------------------
def amplitude_modulation(carrier_freq, sample_rate, duration):
    """
    Perform Amplitude Modulation (AM) of a message signal.

    Parameters:
    - carrier_freq: Frequency of the carrier signal in Hz.
    - sample_rate: Sampling rate in Hz.
    - duration: Duration of the signal in seconds.

    Returns:
    - time: Time vector for the entire signal duration.
    - message_signal: The base message signal (sinusoidal wave).
    - carrier_signal: The carrier signal (sinusoidal wave).
    - am_signal: The resulting amplitude-modulated signal.
    """
    # Generate a time vector with increments of 1/sample_rate.
    time = np.arange(0, duration, 1 / sample_rate)

    # Generate the message signal: a simple sine wave with frequency 1 Hz.
    message_signal = np.sin(2 * np.pi * time)

    # Generate the carrier signal: a sine wave with the specified carrier frequency.
    carrier_signal = np.sin(2 * np.pi * carrier_freq * time)

    # Apply amplitude modulation by multiplying the message signal with the carrier.
    am_signal = message_signal * np.cos(2 * np.pi * carrier_freq * time)

    return time, message_signal, carrier_signal, am_signal

# --------------------
def plot_am_signals(time, message_signal, carrier_signal, am_signal, carrier_freq):
    """
    Plot the message signal, carrier signal, and AM modulated signal.

    Parameters:
    - time: Time vector for the signals.
    - message_signal: The base message signal (sinusoidal wave).
    - carrier_signal: The carrier signal (sinusoidal wave).
    - am_signal: The resulting amplitude-modulated signal.
    - carrier_freq: Frequency of the carrier signal in Hz.
    """
    plt.figure(figsize=(12, 8))  # Set figure size.

    # Plot the message signal.
    plt.subplot(3, 1, 1)
    plt.plot(time, message_signal)
    plt.xlim([0, max(time)])
    plt.grid(True)
    plt.title('Message Signal: sin(2πt)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    # Plot the carrier signal.
    plt.subplot(3, 1, 2)
    plt.plot(time, carrier_signal)
    plt.xlim([0, max(time)])
    plt.grid(True)
    plt.title(f'Carrier Signal: sin(2πFc·t), Fc = {carrier_freq} Hz')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    # Add text to indicate carrier frequency.
    plt.text(0, 0.5, f'Fc = {carrier_freq} Hz', fontsize=12, color='red')

    # Plot the AM modulated signal.
    plt.subplot(3, 1, 3)
    plt.plot(time, am_signal)
    plt.xlim([0, max(time)])
    plt.grid(True)
    plt.title('Amplitude Modulated Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.tight_layout()  # Adjust layout to prevent overlap.
    plt.show()

# --------------------
def main_am(carrier_freq=10, sample_rate=1000, duration=2):
    """
    Main function to execute AM modulation and visualize the results.

    Parameters:
    - carrier_freq: Frequency of the carrier signal in Hz (default: 10 Hz).
    - sample_rate: Sampling rate in Hz (default: 1000 Hz).
    - duration: Duration of the signal in seconds (default: 2 seconds).

    Returns:
    - time: Time vector for the signals.
    - message_signal: The base message signal.
    - carrier_signal: The carrier signal.
    - am_signal: The amplitude-modulated signal.
    """
    # Perform AM modulation.
    time, message_signal, carrier_signal, am_signal = amplitude_modulation(
        carrier_freq, sample_rate, duration)

    # Plot the modulated signals.
    plot_am_signals(time, message_signal, carrier_signal, am_signal, carrier_freq)

    return time, message_signal, carrier_signal, am_signal

# --------------------
if __name__ == "__main__":
    # Execute the main function if the script is run directly.
    main_am()
