import numpy as np  # For mathematical operations and generating signals.
import matplotlib.pyplot as plt  # For creating plots.
import pytest  # For testing

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
# Happy Path Test (Only one test to ensure the graph is plotted and signals are generated)
def test_happy_path_am():
    """
    Test 1: Verify that the AM modulation works correctly and generates the plots.
    """
    time, message_signal, carrier_signal, am_signal = amplitude_modulation(10, 1000, 2)
    
    # Ensure the signals have been generated with correct length.
    expected_length = int(1000 * 2)  # Expected vector length.
    assert len(time) == len(message_signal) == len(carrier_signal) == len(am_signal) == expected_length, \
        "Vector lengths do not match the expected value."

    # Call the plot function to verify the plot is shown.
    plot_am_signals(time, message_signal, carrier_signal, am_signal, 10)

# --------------------
# Sad Path Tests (Tests for invalid inputs)
def test_sad_path_invalid_am_signal():
    """
    Test 2: Verify handling of invalid parameters (e.g., negative sample rate).
    """
    try:
        amplitude_modulation(10, -1000, 2)  # Invalid sample rate (negative).
        assert False, "Expected an error due to negative sample rate."
    except ValueError as e:
        assert str(e) == "Sample rate must be positive."

# --------------------
# Run tests
if __name__ == "__main__":
    main_am()  # Run the main function to generate AM signals
    # Run happy path test (only one test that checks the AM functionality)
    print("Running Happy Path Test...")
    pytest.main(["-v", "test_happy_path_am"])

    # Run sad path tests
    print("Running Sad Path Test...")
    pytest.main(["-v", "test_sad_path_invalid_am_signal"])

