# Test code for FSK_modulation.py (FSK Modulation)
import unittest
from FSK_modulation import fsk_modulation  # Import the function from the main FSK modulation code
import numpy as np  # Required for array manipulations and validations in tests


class TestFSKModulation(unittest.TestCase):
    def test_basic_case(self):
        """
        Test the basic functionality of the FSK modulation function.

        Verifies:
        - The lengths of all generated signals are consistent.
        - The modulating signal corresponds correctly to the binary data input.
        """
        binary_data = [0, 1, 0, 1]
        carrier_freq_0 = 5  # Frequency for binary '0'
        carrier_freq_1 = 10  # Frequency for binary '1'
        sample_rate = 1000  # Sampling rate
        bit_duration = 1  # Duration of each bit in seconds

        # Call the FSK modulation function
        time, mod_signal, carrier_0, carrier_1, fsk_signal = fsk_modulation(
            binary_data, carrier_freq_0, carrier_freq_1, sample_rate, bit_duration
        )

        # Verify the lengths of the generated signals
        self.assertEqual(len(time), len(mod_signal))
        self.assertEqual(len(carrier_0), len(time))
        self.assertEqual(len(carrier_1), len(time))
        self.assertEqual(len(fsk_signal), len(time))

        # Verify that the modulating signal matches the binary input
        mod_signal_reshaped = mod_signal.reshape((len(binary_data), -1))
        np.testing.assert_array_equal(mod_signal_reshaped[:, 0], binary_data)

    def test_bit_duration(self):
        """
        Test the function with varying bit durations.

        Verifies:
        - The total duration of the generated signal matches the expected value.
        """
        binary_data = [1, 0, 1, 0]
        carrier_freq_0 = 5
        carrier_freq_1 = 15
        sample_rate = 2000
        bit_duration = 0.5  # Duration of each bit in seconds

        # Call the FSK modulation function
        time, mod_signal, carrier_0, carrier_1, fsk_signal = fsk_modulation(
            binary_data, carrier_freq_0, carrier_freq_1, sample_rate, bit_duration
        )

        # Verify the total duration of the signal
        expected_duration = len(binary_data) * bit_duration
        self.assertAlmostEqual(time[-1], expected_duration, delta=1 / sample_rate)

    def test_high_frequencies(self):
        """
        Test the function with high carrier frequencies.

        Verifies:
        - The carrier signals are normalized sine waves with amplitudes in the range [-1, 1].
        """
        binary_data = [1, 1, 0, 1]
        carrier_freq_0 = 50
        carrier_freq_1 = 100
        sample_rate = 5000
        bit_duration = 1

        # Call the FSK modulation function
        time, mod_signal, carrier_0, carrier_1, fsk_signal = fsk_modulation(
            binary_data, carrier_freq_0, carrier_freq_1, sample_rate, bit_duration
        )

        # Ensure that the carrier signals are normalized sine waves
        self.assertTrue(np.all(np.abs(carrier_0) <= 1), "Carrier 0 signal is not normalized.")
        self.assertTrue(np.all(np.abs(carrier_1) <= 1), "Carrier 1 signal is not normalized.")

    def test_invalid_binary_data(self):
        """
        Test the function with invalid binary input data.

        Verifies:
        - The function raises a ValueError for non-binary input data.
        """
        binary_data = [1, 2, 0, -1]  # Invalid binary data
        carrier_freq_0 = 5
        carrier_freq_1 = 10
        sample_rate = 1000
        bit_duration = 1

        # Expect a ValueError for invalid binary input
        with self.assertRaises(ValueError):
            fsk_modulation(binary_data, carrier_freq_0, carrier_freq_1, sample_rate, bit_duration)

    def test_single_bit(self):
        """
        Test the FSK modulation function with a single-bit binary data input.

        Verifies:
        - The generated signals correspond to the single bit.
        """
        binary_data = [1]
        carrier_freq_0 = 5
        carrier_freq_1 = 15
        sample_rate = 1000
        bit_duration = 1

        time, mod_signal, carrier_0, carrier_1, fsk_signal = fsk_modulation(
            binary_data, carrier_freq_0, carrier_freq_1, sample_rate, bit_duration
        )

        self.assertEqual(len(time), int(sample_rate * bit_duration))
        self.assertEqual(len(fsk_signal), len(time))

    def test_zero_bit_duration(self):
        """
        Test the FSK modulation function with zero bit duration.

        Verifies:
        - The function returns empty arrays.
        """
        binary_data = [0, 1]
        carrier_freq_0 = 5
        carrier_freq_1 = 10
        sample_rate = 1000
        bit_duration = 0

        time, mod_signal, carrier_0, carrier_1, fsk_signal = fsk_modulation(
            binary_data, carrier_freq_0, carrier_freq_1, sample_rate, bit_duration
        )

        self.assertEqual(len(time), 0)
        self.assertEqual(len(mod_signal), 0)
        self.assertEqual(len(carrier_0), 0)
        self.assertEqual(len(carrier_1), 0)
        self.assertEqual(len(fsk_signal), 0)

    def test_large_binary_data(self):
        """
        Test the FSK modulation function with a large binary data input.

        Verifies:
        - The function scales appropriately without errors.
        """
        binary_data = [0, 1] * 1000  # Large binary sequence
        carrier_freq_0 = 5
        carrier_freq_1 = 10
        sample_rate = 1000
        bit_duration = 0.5

        time, mod_signal, carrier_0, carrier_1, fsk_signal = fsk_modulation(
            binary_data, carrier_freq_0, carrier_freq_1, sample_rate, bit_duration
        )

        self.assertEqual(len(mod_signal), len(time))
        self.assertEqual(len(fsk_signal), len(time))

if __name__ == "__main__":
    unittest.main()
