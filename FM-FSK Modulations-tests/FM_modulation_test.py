# Test code for FM_modulation.py (Frequency Modulation)
import unittest
from FM_Modulation import fm_modulation  # Import the FM modulation function
import numpy as np  # Required for numerical calculations and validations in tests


class TestFMModulation(unittest.TestCase):
    def test_increasing_carrier_frequency(self):
        """
        Test FM modulation with a standard carrier frequency and parameters.

        Verifies:
        - Signal lengths are consistent across all generated components.
        """
        carrier_freq = 50  # Carrier frequency in Hz
        sample_rate = 1000  # Sampling rate in Hz
        duration = 2  # Duration of the signal in seconds
        freq_deviation = 5  # Frequency deviation in Hz

        # Call the FM modulation function
        time, message_signal, carrier_signal, fm_signal = fm_modulation(
            carrier_freq, sample_rate, duration, freq_deviation
        )

        # Verify that all signals have the same length
        self.assertEqual(len(time), len(message_signal))
        self.assertEqual(len(time), len(carrier_signal))
        self.assertEqual(len(time), len(fm_signal))

    def test_frequency_deviation_change(self):
        """
        Test FM modulation with varying frequency deviation.

        Verifies:
        - The maximum instantaneous frequency deviation matches or exceeds the set value.
        """
        carrier_freq = 10  # Carrier frequency in Hz
        sample_rate = 1000  # Sampling rate in Hz
        duration = 2  # Signal duration in seconds
        freq_deviation = 20  # Frequency deviation in Hz

        # Call the FM modulation function
        time, message_signal, carrier_signal, fm_signal = fm_modulation(
            carrier_freq, sample_rate, duration, freq_deviation
        )

        # Calculate instantaneous frequency deviation
        phase = np.unwrap(
            np.angle(
                np.sin(
                    2 * np.pi * carrier_freq * time
                    + 2 * np.pi * freq_deviation * np.cumsum(message_signal) * (1 / sample_rate)
                )
            )
        )
        instantaneous_frequency = np.diff(phase) * sample_rate / (2 * np.pi)

        # Verify the maximum frequency deviation
        max_deviation = np.max(np.abs(instantaneous_frequency - carrier_freq))
        self.assertTrue(
            max_deviation >= freq_deviation,
            f"Expected max deviation >= {freq_deviation}, got {max_deviation}",
        )

    def test_short_signal_duration(self):
        """
        Test FM modulation with a shorter signal duration.

        Verifies:
        - The total duration of the generated signal is as expected.
        """
        carrier_freq = 10  # Carrier frequency in Hz
        sample_rate = 1000  # Sampling rate in Hz
        duration = 0.5  # Signal duration in seconds
        freq_deviation = 5  # Frequency deviation in Hz

        # Call the FM modulation function
        time, message_signal, carrier_signal, fm_signal = fm_modulation(
            carrier_freq, sample_rate, duration, freq_deviation
        )

        # Verify the total duration of the signal
        expected_duration = duration
        self.assertAlmostEqual(
            time[-1],
            expected_duration - (1 / sample_rate),
            delta=1e-6,
            msg=f"Expected time[-1] close to {expected_duration}",
        )

    def test_low_sample_rate(self):
        """
        Test FM modulation with a lower sampling rate.

        Verifies:
        - Signal lengths are consistent despite the lower resolution.
        """
        carrier_freq = 10  # Carrier frequency in Hz
        sample_rate = 100  # Lower sampling rate in Hz
        duration = 2  # Signal duration in seconds
        freq_deviation = 5  # Frequency deviation in Hz

        # Call the FM modulation function
        time, message_signal, carrier_signal, fm_signal = fm_modulation(
            carrier_freq, sample_rate, duration, freq_deviation
        )

        # Verify signal lengths
        self.assertEqual(len(time), len(message_signal))
        self.assertEqual(len(time), len(carrier_signal))
        self.assertEqual(len(time), len(fm_signal))

    def test_invalid_input(self):
        """
        Test FM modulation with invalid inputs.

        Verifies:
        - The function raises a ValueError for invalid parameter combinations.
        """
        # Define invalid input combinations
        invalid_inputs = [
            ("invalid", 1000, 2, 5),  # Non-numeric carrier frequency
            (10, -1000, 2, 5),  # Negative sampling rate
            (10, 1000, -2, 5),  # Negative signal duration
            (10, 1000, 2, "invalid"),  # Non-numeric frequency deviation
        ]

        for carrier_freq, sample_rate, duration, freq_deviation in invalid_inputs:
            with self.assertRaises(ValueError):
                fm_modulation(carrier_freq, sample_rate, duration, freq_deviation)


if __name__ == "__main__":
    unittest.main()
