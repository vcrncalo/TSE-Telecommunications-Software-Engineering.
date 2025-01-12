import unittest
import numpy as np
from AM_modulation import amplitude_modulation

class TestAMModulation(unittest.TestCase):
    # Happy path tests
    def test_am_vector_lengths(self):
        """
        Test 1: Verify that all generated signal vectors have the correct length.
        """
        carrier_freq = 10
        sample_rate = 1000
        duration = 2
        time, message_signal, carrier_signal, am_signal = amplitude_modulation(
            carrier_freq, sample_rate, duration)
        expected_length = int(sample_rate * duration)
        self.assertEqual(len(time), expected_length)
        self.assertEqual(len(message_signal), expected_length)
        self.assertEqual(len(carrier_signal), expected_length)
        self.assertEqual(len(am_signal), expected_length)

    def test_carrier_signal_amplitude(self):
        """
        Test 2: Verify that the carrier signal's amplitude remains within the range [-1, 1].
        """
        carrier_freq = 10
        sample_rate = 1000
        duration = 2
        _, _, carrier_signal, _ = amplitude_modulation(
            carrier_freq, sample_rate, duration)
        self.assertTrue(np.all(carrier_signal <= 1))
        self.assertTrue(np.all(carrier_signal >= -1))

    def test_am_signal_amplitude(self):
        """
        Test 3: Verify that the amplitude-modulated signal remains within the range [-1, 1].
        """
        carrier_freq = 10
        sample_rate = 1000
        duration = 2
        _, _, _, am_signal = amplitude_modulation(
            carrier_freq, sample_rate, duration)
        self.assertTrue(np.all(am_signal <= 1))
        self.assertTrue(np.all(am_signal >= -1))

    def test_am_signal_high_sampling_rate(self):
        """
        Test 4: The AM modulation function with a very high sampling rate.
        """
        carrier_freq = 10
        high_sample_rate = 100000
        duration = 2
        time, message_signal, carrier_signal, am_signal = amplitude_modulation(
            carrier_freq, high_sample_rate, duration)
        expected_length = int(high_sample_rate * duration)
        self.assertEqual(len(time), expected_length)
        self.assertEqual(len(message_signal), expected_length)
        self.assertEqual(len(carrier_signal), expected_length)
        self.assertEqual(len(am_signal), expected_length)

    def test_am_signal_low_sampling_rate(self):
        """
        Test 5: The AM modulation function with a very low sampling rate.
        """
        carrier_freq = 10
        low_sample_rate = 10
        duration = 2
        time, message_signal, carrier_signal, am_signal = amplitude_modulation(
            carrier_freq, low_sample_rate, duration)
        expected_length = int(low_sample_rate * duration)
        self.assertEqual(len(time), expected_length)
        self.assertEqual(len(message_signal), expected_length)
        self.assertEqual(len(carrier_signal), expected_length)
        self.assertEqual(len(am_signal), expected_length)

    def test_am_large_duration(self):
        """
        Test 6: The AM modulation function with a very large duration.
        """
        carrier_freq = 10
        sample_rate = 1000
        large_duration = 100
        time, message_signal, carrier_signal, am_signal = amplitude_modulation(
            carrier_freq, sample_rate, large_duration)
        expected_length = int(sample_rate * large_duration)
        self.assertEqual(len(time), expected_length)
        self.assertEqual(len(message_signal), expected_length)
        self.assertEqual(len(carrier_signal), expected_length)
        self.assertEqual(len(am_signal), expected_length)

    def test_am_different_carrier_frequency(self):
        """
        Test 7: The AM modulation function with a different carrier frequency.
        """
        different_carrier_freq = 50
        sample_rate = 1000
        duration = 2
        time, message_signal, carrier_signal, am_signal = amplitude_modulation(
            different_carrier_freq, sample_rate, duration)
        expected_length = int(sample_rate * duration)
        self.assertEqual(len(time), expected_length)
        self.assertEqual(len(message_signal), expected_length)
        self.assertEqual(len(carrier_signal), expected_length)
        self.assertEqual(len(am_signal), expected_length)

    def test_am_zero_carrier_frequency(self):
        """
        Test 8: The AM modulation function with a zero carrier frequency.
        """
        zero_carrier_freq = 0
        sample_rate = 1000
        duration = 2
        time, message_signal, carrier_signal, am_signal = amplitude_modulation(
            zero_carrier_freq, sample_rate, duration)
        expected_length = int(sample_rate * duration)
        self.assertEqual(len(time), expected_length)
        self.assertEqual(len(message_signal), expected_length)
        self.assertEqual(len(carrier_signal), expected_length)
        self.assertEqual(len(am_signal), expected_length)

    # Sad path tests
    def test_am_signal_zero_duration(self):
        """
        Test 9: The AM modulation function with zero duration.
        """
        carrier_freq = 10
        sample_rate = 1000
        time, message_signal, carrier_signal, am_signal = amplitude_modulation(
            carrier_freq, sample_rate, duration=0)
        self.assertEqual(len(time), 0)
        self.assertEqual(len(message_signal), 0)
        self.assertEqual(len(carrier_signal), 0)
        self.assertEqual(len(am_signal), 0)

    def test_am_signal_edge_case_amplitude(self):
        """
        Test 10: Edge case for amplitude boundary conditions.
        """
        carrier_freq = 10
        sample_rate = 1000
        duration = 2
        _, _, _, am_signal = amplitude_modulation(
            carrier_freq, sample_rate, duration)
        self.assertTrue(np.all(am_signal <= 1))
        self.assertTrue(np.all(am_signal >= -1))

if __name__ == "__main__":
    unittest.main()

