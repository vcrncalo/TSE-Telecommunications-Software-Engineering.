import numpy as np
from AM_modulation import amplitude_modulation

# Define test parameters.
carrier_freq = 10
sample_rate = 1000
duration = 2
# Happy path tests
def test_am_vector_lengths():
    """
    Test 1: Verify that all generated signal vectors have the correct length.
    """
    time, message_signal, carrier_signal, am_signal = amplitude_modulation(
        carrier_freq, sample_rate, duration)
    expected_length = int(sample_rate * duration)
    assert len(time) == expected_length
    assert len(message_signal) == expected_length
    assert len(carrier_signal) == expected_length
    assert len(am_signal) == expected_length

def test_carrier_signal_amplitude():
    """
    Test 2: Verify that the carrier signal's amplitude remains within the range [-1, 1].
    """
    _, _, carrier_signal, _ = amplitude_modulation(
        carrier_freq, sample_rate, duration)
    assert np.all(carrier_signal <= 1)
    assert np.all(carrier_signal >= -1)

def test_am_signal_amplitude():
    """
    Test 3: Verify that the amplitude-modulated signal remains within the range [-1, 1].
    """
    _, _, _, am_signal = amplitude_modulation(
        carrier_freq, sample_rate, duration)
    assert np.all(am_signal <= 1)
    assert np.all(am_signal >= -1)

def test_am_signal_high_sampling_rate():
    """
    Test 4: The AM modulation function with a very high sampling rate.
    """
    high_sample_rate = 100000
    time, message_signal, carrier_signal, am_signal = amplitude_modulation(
        carrier_freq, high_sample_rate, duration)
    expected_length = int(high_sample_rate * duration)
    assert len(time) == expected_length
    assert len(message_signal) == expected_length
    assert len(carrier_signal) == expected_length
    assert len(am_signal) == expected_length

def test_am_signal_low_sampling_rate():
    """
    Test 5: The AM modulation function with a very low sampling rate.
    """
    low_sample_rate = 10
    time, message_signal, carrier_signal, am_signal = amplitude_modulation(
        carrier_freq, low_sample_rate, duration)
    expected_length = int(low_sample_rate * duration)
    assert len(time) == expected_length
    assert len(message_signal) == expected_length
    assert len(carrier_signal) == expected_length
    assert len(am_signal) == expected_length

def test_am_large_duration():
    """
    Test 6: The AM modulation function with a very large duration.
    """
    large_duration = 100
    time, message_signal, carrier_signal, am_signal = amplitude_modulation(
        carrier_freq, sample_rate, large_duration)
    expected_length = int(sample_rate * large_duration)
    assert len(time) == expected_length
    assert len(message_signal) == expected_length
    assert len(carrier_signal) == expected_length
    assert len(am_signal) == expected_length

def test_am_different_carrier_frequency():
    """
    Test 7: The AM modulation function with a different carrier frequency.
    """
    different_carrier_freq = 50
    time, message_signal, carrier_signal, am_signal = amplitude_modulation(
        different_carrier_freq, sample_rate, duration)
    expected_length = int(sample_rate * duration)
    assert len(time) == expected_length
    assert len(message_signal) == expected_length
    assert len(carrier_signal) == expected_length
    assert len(am_signal) == expected_length

def test_am_zero_carrier_frequency():
    """
    Test 8: The AM modulation function with a zero carrier frequency.
    """
    zero_carrier_freq = 0
    time, message_signal, carrier_signal, am_signal = amplitude_modulation(
        zero_carrier_freq, sample_rate, duration)
    expected_length = int(sample_rate * duration)
    assert len(time) == expected_length
    assert len(message_signal) == expected_length
    assert len(carrier_signal) == expected_length
    assert len(am_signal) == expected_length

# Sad path tests
def test_am_signal_zero_duration():
    """
    Test 8: The AM modulation function with zero duration.
    """
    time, message_signal, carrier_signal, am_signal = amplitude_modulation(
        carrier_freq, sample_rate, duration=0)
    assert len(time) == 0
    assert len(message_signal) == 0
    assert len(carrier_signal) == 0
    assert len(am_signal) == 0

def test_am_signal_edge_case_amplitude():
    """
    Test 9: Edge case for amplitude boundary conditions.
    """
    _, _, _, am_signal = amplitude_modulation(
        carrier_freq, sample_rate, duration)
    assert np.all(am_signal <= 1)
    assert np.all(am_signal >= -1)

