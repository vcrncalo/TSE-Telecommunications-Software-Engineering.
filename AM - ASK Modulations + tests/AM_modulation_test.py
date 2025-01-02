# Test code for AM_modulation.py (AM Modulation)
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
# Additional Tests for AM Modulation

def test_am_signal_zero_duration():
    """
    Test 4: The AM modulation function with zero duration.
    Expected: All output arrays should have zero length.
    """
    time, message_signal, carrier_signal, am_signal = amplitude_modulation(
        carrier_freq, sample_rate, duration=0)
    assert len(time) == len(message_signal) == len(carrier_signal) == len(am_signal) == 0, \
        "Output arrays should have zero length for zero duration."

def test_am_signal_high_sampling_rate():
    """
    Test 5: The AM modulation function with a very high sampling rate.
    Expected: The function should handle large data sizes without errors.
    """
    high_sample_rate = 100000  # 100 kHz
    time, message_signal, carrier_signal, am_signal = amplitude_modulation(
        carrier_freq, high_sample_rate, duration)
    assert len(time) == len(message_signal) == len(carrier_signal) == len(am_signal) == int(high_sample_rate * duration), \
        "Vector lengths do not match the expected value for high sampling rate."

def test_am_signal_low_sampling_rate():
    """
    Test 6: The AM modulation function with a very low sampling rate.
    Expected: The function should handle small data sizes and still return valid results.
    """
    low_sample_rate = 10  # 10 Hz
    time, message_signal, carrier_signal, am_signal = amplitude_modulation(
        carrier_freq, low_sample_rate, duration)
    assert len(time) == len(message_signal) == len(carrier_signal) == len(am_signal) == int(low_sample_rate * duration), \
        "Vector lengths do not match the expected value for low sampling rate."

def test_am_signal_edge_case_amplitude():
    """
    Test 8: Edge case for amplitude boundary conditions.
    Expected: Signal values should remain within [-1, 1].
    """
    _, _, _, am_signal = amplitude_modulation(
        carrier_freq, sample_rate, duration)
    assert np.all(am_signal <= 1) and np.all(am_signal >= -1), \
        "AM signal exceeds amplitude boundary conditions."

def test_am_zero_sampling_rate():
    """
    Test 9: The AM modulation function with zero sampling rate.
    Expected: Should raise an error or return empty arrays.
    """
    try:
        amplitude_modulation(carrier_freq, 0, duration)
    except ZeroDivisionError:
        assert True  # Expected behavior: exception is raised.
    else:
        assert False, "Zero sampling rate should raise an exception."

def test_am_large_duration():
    """
    Test 10: The AM modulation function with a very large duration.
    Expected: Should handle large data sizes without errors.
    """
    large_duration = 100  # 100 seconds
    time, message_signal, carrier_signal, am_signal = amplitude_modulation(
        carrier_freq, sample_rate, large_duration)
    assert len(time) == len(message_signal) == len(carrier_signal) == len(am_signal) == int(sample_rate * large_duration), \
        "Vector lengths do not match the expected value for large duration."
