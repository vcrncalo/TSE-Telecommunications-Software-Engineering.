import numpy as np
import matplotlib.pyplot as plt

# --------------------
# FM Modulation Functions
# --------------------

def fm_modulation(carrier_freq, sample_rate, duration, freq_deviation):
    """
    FM modulation with given carrier frequency, sampling rate, signal duration, and frequency deviation.
    """
    if carrier_freq <= 0:
        raise ValueError("Carrier frequency must be greater than 0.")
    if sample_rate <= 0:
        raise ValueError("Sample rate must be greater than 0.")
    if duration <= 0:
        raise ValueError("Duration must be greater than 0.")
    if freq_deviation < 0:
        raise ValueError("Frequency deviation must be non-negative.")

    time = np.arange(0, duration, 1 / sample_rate)  # Time vector
    message_signal = np.sin(2 * np.pi * time)  # Message signal
    carrier_signal = np.sin(2 * np.pi * carrier_freq * time)  # Carrier signal
    integral_message = np.cumsum(message_signal) * (1 / sample_rate)  # Integral of message signal
    fm_signal = np.sin(2 * np.pi * carrier_freq * time + 2 * np.pi * freq_deviation * integral_message)
    return time, message_signal, carrier_signal, fm_signal


def plot_fm_signals(time, message_signal, carrier_signal, fm_signal, carrier_freq, freq_deviation):
    """
    Function to plot the message signal, carrier signal, and FM signal on separate graphs.
    """
    plt.subplot(3, 1, 1)
    plt.plot(time, message_signal)
    plt.title('Message Signal: sin(2*pi*t)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid()

    plt.subplot(3, 1, 2)
    plt.plot(time, carrier_signal)
    plt.title('Carrier Signal: sin(2*pi*Fc*t)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.text(0, 0.5, f'Fc = {carrier_freq} Hz', fontsize=12, color='blue')

    plt.subplot(3, 1, 3)
    plt.plot(time, fm_signal)
    plt.title('FM Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.text(0, 0.5, f'Fc = {carrier_freq} Hz, Δf = {freq_deviation} Hz', fontsize=12, color='green')

    plt.tight_layout()
    plt.show()


# --------------------
# Happy Path Tests for FM Modulation
# --------------------

def test_happy_path_1():
    """Happy path test 1: Normal case with standard parameters."""
    carrier_freq = 50
    sample_rate = 1000
    duration = 2
    freq_deviation = 5
    time, message_signal, carrier_signal, fm_signal = fm_modulation(carrier_freq, sample_rate, duration, freq_deviation)
    plot_fm_signals(time, message_signal, carrier_signal, fm_signal, carrier_freq, freq_deviation)

def test_happy_path_2():
    """Happy path test 2: Higher frequency deviation."""
    carrier_freq = 50
    sample_rate = 1000
    duration = 2
    freq_deviation = 20
    time, message_signal, carrier_signal, fm_signal = fm_modulation(carrier_freq, sample_rate, duration, freq_deviation)
    plot_fm_signals(time, message_signal, carrier_signal, fm_signal, carrier_freq, freq_deviation)

def test_happy_path_3():
    """Happy path test 3: Longer signal duration."""
    carrier_freq = 50
    sample_rate = 1000
    duration = 5  # Longer duration
    freq_deviation = 5
    time, message_signal, carrier_signal, fm_signal = fm_modulation(carrier_freq, sample_rate, duration, freq_deviation)
    plot_fm_signals(time, message_signal, carrier_signal, fm_signal, carrier_freq, freq_deviation)

def test_happy_path_4():
    """Happy path test 4: Low sample rate."""
    carrier_freq = 10
    sample_rate = 500  # Lower sample rate
    duration = 2
    freq_deviation = 5
    time, message_signal, carrier_signal, fm_signal = fm_modulation(carrier_freq, sample_rate, duration, freq_deviation)
    plot_fm_signals(time, message_signal, carrier_signal, fm_signal, carrier_freq, freq_deviation)


# --------------------
# Sad Path Tests for FM Modulation (Tests that should fail)
# --------------------

def test_sad_path_1():
    """Sad path test 1: Extremely low carrier frequency."""
    carrier_freq = 0.1  # Too low carrier frequency for FM
    sample_rate = 1000
    duration = 2
    freq_deviation = 5
    try:
        time, message_signal, carrier_signal, fm_signal = fm_modulation(carrier_freq, sample_rate, duration, freq_deviation)
        # No plotting for sad path tests
        print("Sad path test 1 failed, but no graph should be generated due to the error.")
    except ValueError as e:
        assert str(e) == "Carrier frequency must be greater than 0."
        print(f"Sad path test 1 failed as expected: {e}")
        return
    raise AssertionError("Sad path test 1 passed, but it should have failed.")


def test_sad_path_2():
    """Sad path test 2: Extremely low sample rate causing aliasing."""
    carrier_freq = 10
    sample_rate = 20  # Too low sample rate, aliasing will occur
    duration = 2
    freq_deviation = 5
    try:
        time, message_signal, carrier_signal, fm_signal = fm_modulation(carrier_freq, sample_rate, duration, freq_deviation)
        # No plotting for sad path tests
        print("Sad path test 2 failed, but no graph should be generated due to the error.")
    except ValueError as e:
        assert str(e) == "Sample rate must be greater than 0."
        print(f"Sad path test 2 failed as expected: {e}")
        return
    raise AssertionError("Sad path test 2 passed, but it should have failed.")


def test_sad_path_3():
    """Sad path test 3: Extremely short duration."""
    carrier_freq = 10
    sample_rate = 1000
    duration = 0.01  # Extremely short duration, almost no signal can be processed
    freq_deviation = 5
    try:
        time, message_signal, carrier_signal, fm_signal = fm_modulation(carrier_freq, sample_rate, duration, freq_deviation)
        # No plotting for sad path tests
        print("Sad path test 3 failed, but no graph should be generated due to the error.")
    except ValueError as e:
        assert str(e) == "Duration must be greater than 0."
        print(f"Sad path test 3 failed as expected: {e}")
        return
    raise AssertionError("Sad path test 3 passed, but it should have failed.")


def test_sad_path_4():
    """Sad path test 4: Excessive frequency deviation."""
    carrier_freq = 50
    sample_rate = 1000
    duration = 2
    freq_deviation = 5000  # Excessively high frequency deviation
    try:
        time, message_signal, carrier_signal, fm_signal = fm_modulation(carrier_freq, sample_rate, duration, freq_deviation)
        # No plotting for sad path tests
        print("Sad path test 4 failed, but no graph should be generated due to the error.")
    except ValueError as e:
        assert str(e) == "Frequency deviation must be non-negative."
        print(f"Sad path test 4 failed as expected: {e}")
        return
    raise AssertionError("Sad path test 4 passed, but it should have failed.")

