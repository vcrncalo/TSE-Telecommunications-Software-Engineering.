import unittest
from QAM import qam_modulation  # Import the function from the main QAM modulation code
import numpy as np  # Required for array manipulations and validations in tests

class TestQAMModulation(unittest.TestCase):
    # Happy path tests
    def test_basic_case(self):
        """
        Test the basic functionality of the QAM modulation function.

        Verifies:
        - The lengths of all generated signals are consistent.
        - The modulating signal has the correct length.
        """
        binary_data = [0, 1, 1, 0, 1, 1, 0, 0]
        carrier_freq = 5  # Carrier frequency
        sample_rate = 1000  # Sampling rate
        bit_duration = 1  # Duration of each bit in seconds
        constellation_points = [1+1j, 1-1j, -1+1j, -1-1j] # 4-QAM

        # Call the QAM modulation function
        time, mod_signal, carrier_signal_i, carrier_signal_q, qam_signal = qam_modulation(
            binary_data, carrier_freq, sample_rate, bit_duration, constellation_points
        )

        # Verify the lengths of the generated signals
        self.assertEqual(len(time), len(qam_signal))
        self.assertEqual(len(carrier_signal_i), len(time))
        self.assertEqual(len(carrier_signal_q), len(time))

        # Verify that the modulating signal has the correct length
        self.assertEqual(len(mod_signal), len(binary_data) // int(np.log2(len(constellation_points))))

    def test_bit_duration(self):
        """
        Test the function with varying bit durations.

        Verifies:
        - The total duration of the generated signal matches the expected value.
        """
        binary_data = [1, 0, 1, 0, 1, 1]
        carrier_freq = 10
        sample_rate = 2000
        bit_duration = 0.5  # Duration of each bit in seconds
        constellation_points = [1+1j, 1-1j, -1+1j, -1-1j] # 4-QAM

        # Call the QAM modulation function
        time, mod_signal, carrier_signal_i, carrier_signal_q, qam_signal = qam_modulation(
            binary_data, carrier_freq, sample_rate, bit_duration, constellation_points
        )

        # Verify the total duration of the signal
        expected_duration = len(binary_data) / int(np.log2(len(constellation_points))) * bit_duration
        self.assertAlmostEqual(time[-1], expected_duration, delta=1 / sample_rate)

    def test_high_frequency(self):
        """
        Test the function with a high carrier frequency.

        Verifies:
        - The carrier signals are normalized sine and cosine waves with amplitude in the range [-1, 1].
        """
        binary_data = [1, 1, 0, 1, 0, 0]
        carrier_freq = 500
        sample_rate = 5000
        bit_duration = 1
        constellation_points = [1+1j, 1-1j, -1+1j, -1-1j] # 4-QAM

        # Call the QAM modulation function
        time, mod_signal, carrier_signal_i, carrier_signal_q, qam_signal = qam_modulation(
            binary_data, carrier_freq, sample_rate, bit_duration, constellation_points
        )

        # Ensure that the carrier signals are normalized
        self.assertTrue(np.all(np.abs(carrier_signal_i) <= 1), "In-phase carrier signal is not normalized.")
        self.assertTrue(np.all(np.abs(carrier_signal_q) <= 1), "Quadrature carrier signal is not normalized.")

    def test_large_binary_data(self):
        """
        Test the QAM modulation function with a large binary data input.

        Verifies:
        - The function scales appropriately without errors.
        """
        binary_data = [0, 1, 1, 0] * 1000  # Large binary sequence
        carrier_freq = 10
        sample_rate = 1000
        bit_duration = 0.5
        constellation_points = [1+1j, 1-1j, -1+1j, -1-1j] # 4-QAM

        time, mod_signal, carrier_signal_i, carrier_signal_q, qam_signal = qam_modulation(
            binary_data, carrier_freq, sample_rate, bit_duration, constellation_points
        )

        self.assertEqual(len(qam_signal), len(time))
        self.assertEqual(len(carrier_signal_i), len(time))
        self.assertEqual(len(carrier_signal_q), len(time))

    def test_single_symbol(self):
        """
        Test the QAM modulation function with a single symbol binary data input.

        Verifies:
        - The generated signals correspond to the single symbol.
        """
        binary_data = [1, 0]
        carrier_freq = 15
        sample_rate = 1000
        bit_duration = 1
        constellation_points = [1+1j, 1-1j, -1+1j, -1-1j] # 4-QAM

        time, mod_signal, carrier_signal_i, carrier_signal_q, qam_signal = qam_modulation(
            binary_data, carrier_freq, sample_rate, bit_duration, constellation_points
        )

        self.assertEqual(len(time), int(sample_rate * bit_duration))
        self.assertEqual(len(qam_signal), len(time))

    def test_invalid_binary_data_length(self):
        """
        Test the function with invalid binary input data length.

        Verifies:
        - The function raises a ValueError for binary data length not a multiple of bits per symbol.
        """
        binary_data = [1, 0, 1]  # Invalid binary data length for 4-QAM
        carrier_freq = 5
        sample_rate = 1000
        bit_duration = 1
        constellation_points = [1+1j, 1-1j, -1+1j, -1-1j] # 4-QAM

        # Expect a ValueError for invalid binary input
        with self.assertRaises(ValueError):
            qam_modulation(binary_data, carrier_freq, sample_rate, bit_duration, constellation_points)

    def test_invalid_constellation_points(self):
        """
        Test the function with invalid constellation points.

        Verifies:
        - The function raises a ValueError for non-complex constellation points.
        """
        binary_data = [0, 1, 1, 0]
        carrier_freq = 5
        sample_rate = 1000
        bit_duration = 1
        constellation_points = [1, 2, 3, 4]  # Invalid constellation points

        # Expect a ValueError for invalid constellation points
        with self.assertRaises(ValueError):
            qam_modulation(binary_data, carrier_freq, sample_rate, bit_duration, constellation_points)

    def test_invalid_constellation_points_number(self):
        """
        Test the function with invalid number of constellation points.

        Verifies:
        - The function raises a ValueError for number of constellation points not a power of 2.
        """
        binary_data = [0, 1, 1, 0, 1, 1]
        carrier_freq = 5
        sample_rate = 1000
        bit_duration = 1
        constellation_points = [1+1j, 1-1j, -1+1j]  # Invalid number of constellation points

        # Expect a ValueError for invalid constellation points
        with self.assertRaises(ValueError):
            qam_modulation(binary_data, carrier_freq, sample_rate, bit_duration, constellation_points)

    def test_negative_sample_rate(self):
        """
        Test the QAM modulation function with a negative sample rate.

        Verifies:
        - The function raises a ValueError when sample_rate is negative.
        """
        binary_data = [0, 1, 1, 0]
        carrier_freq = 5
        sample_rate = -1000
        bit_duration = 1
        constellation_points = [1+1j, 1-1j, -1+1j, -1-1j] # 4-QAM

        with self.assertRaises(ValueError):
            qam_modulation(binary_data, carrier_freq, sample_rate, bit_duration, constellation_points)

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
        constellation_points = [1+1j, 1-1j, -1+1j, -1-1j] # 4-QAM

        time, mod_signal, carrier_signal_i, carrier_signal_q, qam_signal = qam_modulation(
            binary_data, carrier_freq, sample_rate, bit_duration, constellation_points
        )

        self.assertEqual(len(time), 0)
        self.assertEqual(len(mod_signal), 0)
        self.assertEqual(len(carrier_signal_i), 0)
        self.assertEqual(len(carrier_signal_q), 0)
        self.assertEqual(len(qam_signal), 0)

if __name__ == "__main__":
    unittest.main()
