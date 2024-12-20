import numpy as np  # For numerical operations and testing signal properties.
from AM_modulation import amplitude_modulation  # Import the amplitude modulation function from the main module.

# Define test parameters.
carrier_freq = 10  # Carrier signal frequency in Hz.
sample_rate = 1000  # Sampling rate in Hz.
duration = 2  # Signal duration in seconds.

# --------------------
def test_am_vector_lengths():
    """
    Test 1: Verify that all generated signal vectors (time, message signal, carrier signal, and AM signal)
    have the correct length based on the sampling rate and duration.
    """
    time, message_signal, carrier_signal, am_signal = amplitude_modulation(
        carrier_freq, sample_rate, duration)
    expected_length = int(sample_rate * duration)  # Expected vector length.
    assert len(time) == len(message_signal) == len(carrier_signal) == len(am_signal) == expected_length, \
        "Vector lengths do not match the expected value."

# --------------------
def test_carrier_signal_amplitude():
    """
    Test 2: Verify that the carrier signal's amplitude remains within the range [-1, 1].
    """
    _, _, carrier_signal, _ = amplitude_modulation(
        carrier_freq, sample_rate, duration)
    assert np.all(carrier_signal <= 1) and np.all(carrier_signal >= -1), \
        "Carrier signal amplitude is outside the range [-1, 1]."

# --------------------
def test_am_signal_amplitude():
    """
    Test 3: Verify that the amplitude-modulated signal remains within the range [-1, 1].
    """
    _, _, _, am_signal = amplitude_modulation(
        carrier_freq, sample_rate, duration)
    assert np.all(am_signal <= 1) and np.all(am_signal >= -1), \
        "AM signal amplitude is outside the range [-1, 1]."

# --------------------

# Note: Use a test runner like pytest to execute these test functions.
# For example, save this file as `test_am_modulation.py` and run `pytest test_am_modulation.py` in the terminal.
