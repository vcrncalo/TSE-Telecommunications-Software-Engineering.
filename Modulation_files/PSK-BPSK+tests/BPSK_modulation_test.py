import unittest
from BPSK_modulation import bpsk_modulation  # Import the function from the main BPSK modulation code
import numpy as np  # Required for array manipulations and validations in tests

class TestBPSKModulation(unittest.TestCase):
    # Happy path tests
    def test_basic_case(self):
        """
        Test the basic functionality of the BPSK modulation function.

        Verifies:
        - The lengths of all generated signals are consistent.
        - The modulating signal corresponds correctly to the binary data input.
        """
        binary_data = [0, 1, 0, 1]
        carrier_freq = 5  # Carrier frequency
        sample_rate = 1000  # Sampling rate
        bit_duration = 1  # Duration of each bit in seconds

        # Call the BPSK modulation function
        time, mod_signal, carrier_signal, bpsk_signal = bpsk_modulation(
            binary_data, carrier_freq, sample_rate, bit_duration
        )

        # Verify the lengths of the generated signals
        self.assertEqual(len(time), len(mod_signal))
        self.assertEqual(len(carrier_signal), len(time))
        self.assertEqual(len(bpsk_signal), len(time))

        # Verify that the modulating signal matches the binary input
        mod_signal_reshaped = mod_signal.reshape((len(binary_data), -1))
        np.testing.assert_array_equal(mod_signal_reshaped[:, 0], binary_data)

    # Happy path tests
    def test_bit_duration(self):
        """
        Test the function with varying bit durations.

        Verifies:
        - The total duration of the generated signal matches the expected value.
        """
        binary_data = [1, 0, 1, 0]
        carrier_freq = 10
        sample_rate = 2000
        bit_duration = 0.5  # Duration of each bit in seconds

        # Call the BPSK modulation function
        time, mod_signal, carrier_signal, bpsk_signal = bpsk_modulation(
            binary_data, carrier_freq, sample_rate, bit_duration
        )

        # Verify the total duration of the signal
        expected_duration = len(binary_data) * bit_duration
        self.assertAlmostEqual(time[-1], expected_duration, delta=1 / sample_rate)

    # Happy path tests
    def test_high_frequency(self):
        """
        Test the function with a high carrier frequency.

        Verifies:
        - The carrier signal is a normalized sine wave with amplitude in the range [-1, 1].
        """
        binary_data = [1, 1, 0, 1]
        carrier_freq = 500
        sample_rate = 5000
        bit_duration = 1

        # Call the BPSK modulation function
        time, mod_signal, carrier_signal, bpsk_signal = bpsk_modulation(
            binary_data, carrier_freq, sample_rate, bit_duration
        )

        # Ensure that the carrier signal is a normalized sine wave
        self.assertTrue(np.all(np.abs(carrier_signal) <= 1), "Carrier signal is not normalized.")

    # Happy path tests
    def test_large_binary_data(self):
        """
        Test the BPSK modulation function with a large binary data input.

        Verifies:
        - The function scales appropriately without errors.
        """
        binary_data = [0, 1] * 1000  # Large binary sequence
        carrier_freq = 10
        sample_rate = 1000
        bit_duration = 0.5

        time, mod_signal, carrier_signal, bpsk_signal = bpsk_modulation(
            binary_data, carrier_freq, sample_rate, bit_duration
        )

        self.assertEqual(len(mod_signal), len(time))
        self.assertEqual(len(bpsk_signal), len(time))

    # Happy path tests
    def test_single_bit(self):
        """
        Test the BPSK modulation function with a single-bit binary data input.

        Verifies:
        - The generated signals correspond to the single bit.
        """
        binary_data = [1]
        carrier_freq = 15
        sample_rate = 1000
        bit_duration = 1

        time, mod_signal, carrier_signal, bpsk_signal = bpsk_modulation(
            binary_data, carrier_freq, sample_rate, bit_duration
        )

        self.assertEqual(len(time), int(sample_rate * bit_duration))
        self.assertEqual(len(bpsk_signal), len(time))

    # Sad path tests
    def test_invalid_binary_data(self):
        """
        Test the function with invalid binary input data.

        Verifies:
        - The function raises a ValueError for non-binary input data.
        """
        binary_data = [1, 2, 0, -1]  # Invalid binary data
        carrier_freq = 5
        sample_rate = 1000
        bit_duration = 1

        # Expect a ValueError for invalid binary input
        with self.assertRaises(ValueError):
            bpsk_modulation(binary_data, carrier_freq, sample_rate, bit_duration)

    # Sad path tests
    def test_zero_bit_duration(self):
        """
        Test the BPSK modulation function with zero bit duration.

        Verifies:
        - The function returns empty arrays.
        """
        binary_data = [0, 1]
        carrier_freq = 5
        sample_rate = 1000
        bit_duration = 0

        time, mod_signal, carrier_signal, bpsk_signal = bpsk_modulation(
            binary_data, carrier_freq, sample_rate, bit_duration
        )

        self.assertEqual(len(time), 0)
        self.assertEqual(len(mod_signal), 0)
        self.assertEqual(len(carrier_signal), 0)
        self.assertEqual(len(bpsk_signal), 0)

    # Sad path tests
    def test_negative_sample_rate(self):
        """
        Test the function with a negative sample rate.

        Verifies:
        - The function raises a ValueError for a negative sample rate.
        """
        binary_data = [0, 1]
        carrier_freq = 5
        sample_rate = -1000
        bit_duration = 1

        with self.assertRaises(ValueError):
            bpsk_modulation(binary_data, carrier_freq, sample_rate, bit_duration)

    # Sad path tests
    def test_negative_bit_duration(self):
        """
        Test the function with a negative bit duration.

        Verifies:
        - The function raises a ValueError for a negative bit duration.
        """
        binary_data = [0, 1]
        carrier_freq = 5
        sample_rate = 1000
        bit_duration = -1

        with self.assertRaises(ValueError):
            bpsk_modulation(binary_data, carrier_freq, sample_rate, bit_duration)

    def test_empty_binary_data(self):
        """
        Test the function with empty binary data.

        Verifies:
        - The function returns empty arrays when the binary data is empty.
        """
        binary_data = []
        carrier_freq = 5
        sample_rate = 1000
        bit_duration = 1

        time, mod_signal, carrier_signal, bpsk_signal = bpsk_modulation(
            binary_data, carrier_freq, sample_rate, bit_duration
        )

        self.assertEqual(len(time), 0)
        self.assertEqual(len(mod_signal), 0)
        self.assertEqual(len(carrier_signal), 0)
        self.assertEqual(len(bpsk_signal), 0)

if __name__ == "__main__":
    unittest.main()
