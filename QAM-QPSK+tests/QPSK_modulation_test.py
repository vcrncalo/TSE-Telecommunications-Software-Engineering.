import unittest
from QPSK_modulation import qpsk_modulation  # Import the function from the main QPSK modulation code
import numpy as np  # Required for array manipulations and validations in tests

class TestQPSKModulation(unittest.TestCase):
    # Happy path tests
    def test_basic_case(self):
        """
        Test the basic functionality of the QPSK modulation function.

        Verifies:
        - The lengths of all generated signals are consistent.
        - The modulating signal has the correct length.
        """
        binary_data = [0, 1, 1, 0, 1, 1, 0, 0]
        carrier_freq = 5  # Carrier frequency
        sample_rate = 1000  # Sampling rate
        bit_duration = 1  # Duration of each bit in seconds

        # Call the QPSK modulation function
        time, mod_signal, carrier_signal_i, carrier_signal_q, qpsk_signal = qpsk_modulation(
            binary_data, carrier_freq, sample_rate, bit_duration
        )

        # Verify the lengths of the generated signals
        self.assertEqual(len(time), len(qpsk_signal))
        self.assertEqual(len(carrier_signal_i), len(time))
        self.assertEqual(len(carrier_signal_q), len(time))

        # Verify that the modulating signal has the correct length
        self.assertEqual(len(mod_signal), len(binary_data) // 2)

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

        # Call the QPSK modulation function
        time, mod_signal, carrier_signal_i, carrier_signal_q, qpsk_signal = qpsk_modulation(
            binary_data, carrier_freq, sample_rate, bit_duration
        )

        # Verify the total duration of the signal
        expected_duration = len(binary_data) / 2 * bit_duration
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

        # Call the QPSK modulation function
        time, mod_signal, carrier_signal_i, carrier_signal_q, qpsk_signal = qpsk_modulation(
            binary_data, carrier_freq, sample_rate, bit_duration
        )

        # Ensure that the carrier signals are normalized
        self.assertTrue(np.all(np.abs(carrier_signal_i) <= 1), "In-phase carrier signal is not normalized.")
        self.assertTrue(np.all(np.abs(carrier_signal_q) <= 1), "Quadrature carrier signal is not normalized.")

    def test_large_binary_data(self):
        """
        Test the QPSK modulation function with a large binary data input.

        Verifies:
        - The function scales appropriately without errors.
        """
        binary_data = [0, 1, 1, 0] * 1000  # Large binary sequence
        carrier_freq = 10
        sample_rate = 1000
        bit_duration = 0.5

        time, mod_signal, carrier_signal_i, carrier_signal_q, qpsk_signal = qpsk_modulation(
            binary_data, carrier_freq, sample_rate, bit_duration
        )

        self.assertEqual(len(qpsk_signal), len(time))
        self.assertEqual(len(carrier_signal_i), len(time))
        self.assertEqual(len(carrier_signal_q), len(time))

    def test_single_symbol(self):
        """
        Test the QPSK modulation function with a single symbol binary data input.

        Verifies:
        - The generated signals correspond to the single symbol.
        """
        binary_data = [1, 0]
        carrier_freq = 15
        sample_rate = 1000
        bit_duration = 1

        time, mod_signal, carrier_signal_i, carrier_signal_q, qpsk_signal = qpsk_modulation(
            binary_data, carrier_freq, sample_rate, bit_duration
        )

        self.assertEqual(len(time), int(sample_rate * bit_duration))
        self.assertEqual(len(qpsk_signal), len(time))

    def test_invalid_binary_data_length(self):
        """
        Test the function with invalid binary input data length.

        Verifies:
        - The function raises a ValueError for binary data length not a multiple of 2.
        """
        binary_data = [1, 0, 1]  # Invalid binary data length for QPSK
        carrier_freq = 5
        sample_rate = 1000
        bit_duration = 1

        # Expect a ValueError for invalid binary input
        with self.assertRaises(ValueError):
            qpsk_modulation(binary_data, carrier_freq, sample_rate, bit_duration)

    def test_negative_sample_rate(self):
        """
        Test the QPSK modulation function with a negative sample rate.

        Verifies:
        - The function raises a ValueError when sample_rate is negative.
        """
        binary_data = [0, 1, 1, 0]
        carrier_freq = 5
        sample_rate = -1000
        bit_duration = 1

        with self.assertRaises(ValueError):
            qpsk_modulation(binary_data, carrier_freq, sample_rate, bit_duration)

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

        time, mod_signal, carrier_signal_i, carrier_signal_q, qpsk_signal = qpsk_modulation(
            binary_data, carrier_freq, sample_rate, bit_duration
        )

        self.assertEqual(len(time), 0)
        self.assertEqual(len(mod_signal), 0)
        self.assertEqual(len(carrier_signal_i), 0)
        self.assertEqual(len(carrier_signal_q), 0)
        self.assertEqual(len(qpsk_signal), 0)

    def test_zero_carrier_frequency(self):
        """
        Test the function with a zero carrier frequency.

        Verifies:
        - The carrier signals are constant (all zeros).
        """
        binary_data = [1, 0, 1, 1]
        carrier_freq = 0
        sample_rate = 1000
        bit_duration = 1

        time, mod_signal, carrier_signal_i, carrier_signal_q, qpsk_signal = qpsk_modulation(
            binary_data, carrier_freq, sample_rate, bit_duration
        )
        self.assertTrue(np.all(carrier_signal_i == 1), "In-phase carrier signal is not constant.")
        self.assertTrue(np.all(carrier_signal_q == 0), "Quadrature carrier signal is not constant.")

    def test_uneven_sample_rate_bit_duration(self):
        """
        Test the function with a sample rate that is not a multiple of the bit duration.

        Verifies:
        - The function still generates signals without errors.
        """
        binary_data = [0, 1, 1, 0, 1, 0]
        carrier_freq = 10
        sample_rate = 1200
        bit_duration = 0.7

        time, mod_signal, carrier_signal_i, carrier_signal_q, qpsk_signal = qpsk_modulation(
            binary_data, carrier_freq, sample_rate, bit_duration
        )

        self.assertEqual(len(time), len(qpsk_signal))
        self.assertEqual(len(carrier_signal_i), len(time))
        self.assertEqual(len(carrier_signal_q), len(time))

if __name__ == "__main__":
    unittest.main()
