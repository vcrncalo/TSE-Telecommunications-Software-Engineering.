import unittest
from FSK_modulation import fsk_modulation  # Import the function from the main code
import numpy as np  # Required for array manipulations in tests

class TestFSKModulation(unittest.TestCase):
    def test_basic_case(self):
        """Test the basic case of FSK modulation."""
        binary_data = [0, 1, 0, 1]
        carrier_freq_0 = 5
        carrier_freq_1 = 10
        sample_rate = 1000
        bit_duration = 1

        # Call the FSK modulation function
        time, mod_signal, carrier_0, carrier_1, fsk_signal = fsk_modulation(
            binary_data, carrier_freq_0, carrier_freq_1, sample_rate, bit_duration
        )

        # Check the lengths of generated signals
        self.assertEqual(len(time), len(mod_signal))
        self.assertEqual(len(carrier_0), len(time))
        self.assertEqual(len(carrier_1), len(time))
        self.assertEqual(len(fsk_signal), len(time))

        # Verify that the modulating signal matches the binary data
        mod_signal_reshaped = mod_signal.reshape((len(binary_data), -1))
        np.testing.assert_array_equal(mod_signal_reshaped[:, 0], binary_data)

    def test_bit_duration(self):
        """Test with different bit durations."""
        binary_data = [1, 0, 1, 0]
        carrier_freq_0 = 5
        carrier_freq_1 = 15
        sample_rate = 2000
        bit_duration = 0.5

        # Call the FSK modulation function
        time, mod_signal, carrier_0, carrier_1, fsk_signal = fsk_modulation(
            binary_data, carrier_freq_0, carrier_freq_1, sample_rate, bit_duration
        )

        # Verify the total duration of the signal
        expected_duration = len(binary_data) * bit_duration
        self.assertAlmostEqual(time[-1], expected_duration, delta=1 / sample_rate)

    def test_high_frequencies(self):
        """Test with high carrier frequencies."""
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
        self.assertTrue(np.all(np.abs(carrier_0) <= 1))
        self.assertTrue(np.all(np.abs(carrier_1) <= 1))

    def test_invalid_binary_data(self):
        """Test for invalid binary input data."""
        binary_data = [1, 2, 0, -1]  # Invalid input
        carrier_freq_0 = 5
        carrier_freq_1 = 10
        sample_rate = 1000
        bit_duration = 1

        # Expecting ValueError for invalid binary data
        with self.assertRaises(ValueError):
            fsk_modulation(binary_data, carrier_freq_0, carrier_freq_1, sample_rate, bit_duration)


if __name__ == "__main__":
    unittest.main()
