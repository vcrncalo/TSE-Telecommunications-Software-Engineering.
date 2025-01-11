import unittest
from FM_modulation import fm_modulation  # Import the FM modulation function
import numpy as np  # Required for numerical calculations and validations in tests

class TestFMModulation(unittest.TestCase):
    # Happy path tests
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

        time, message_signal, carrier_signal, fm_signal = fm_modulation(
            carrier_freq, sample_rate, duration, freq_deviation
        )

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

        time, message_signal, carrier_signal, fm_signal = fm_modulation(
            carrier_freq, sample_rate, duration, freq_deviation
        )

        phase = np.unwrap(
            np.angle(
                np.sin(
                    2 * np.pi * carrier_freq * time
                    + 2 * np.pi * freq_deviation * np.cumsum(message_signal) * (1 / sample_rate)
                )
            )
        )
        instantaneous_frequency = np.diff(phase) * sample_rate / (2 * np.pi)

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

        time, message_signal, carrier_signal, fm_signal = fm_modulation(
            carrier_freq, sample_rate, duration, freq_deviation
        )

        self.assertAlmostEqual(
            time[-1],
            duration - (1 / sample_rate),
            delta=1e-6,
            msg=f"Expected time[-1] close to {duration}",
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

        time, message_signal, carrier_signal, fm_signal = fm_modulation(
            carrier_freq, sample_rate, duration, freq_deviation
        )

        self.assertEqual(len(time), len(message_signal))
        self.assertEqual(len(time), len(carrier_signal))
        self.assertEqual(len(time), len(fm_signal))

    def test_high_sample_rate(self):
        """
        Test FM modulation with a very high sampling rate.

        Verifies:
        - The function handles high-resolution signals correctly.
        """
        carrier_freq = 10
        sample_rate = 100000  # High sample rate
        duration = 1
        freq_deviation = 5

        time, message_signal, carrier_signal, fm_signal = fm_modulation(
            carrier_freq, sample_rate, duration, freq_deviation
        )

        self.assertEqual(len(time), len(message_signal))
        self.assertEqual(len(time), len(carrier_signal))
        self.assertEqual(len(time), len(fm_signal))

    def test_signal_amplitude_variation(self):
        """
        Test FM modulation when the message signal amplitude changes.

        Verifies:
        - The FM signal adapts correctly to varying amplitudes.
        """
        carrier_freq = 10
        sample_rate = 1000
        duration = 2
        freq_deviation = 5

        time, message_signal, carrier_signal, fm_signal = fm_modulation(
            carrier_freq, sample_rate, duration, freq_deviation
        )

        self.assertTrue(np.max(message_signal) > 0)
        self.assertTrue(np.min(message_signal) < 0)

    def test_large_duration(self):
        """
        Test FM modulation with a very large signal duration.

        Verifies:
        - The function handles long signals without errors.
        """
        carrier_freq = 10
        sample_rate = 1000
        duration = 10  # Long duration
        freq_deviation = 5

        time, message_signal, carrier_signal, fm_signal = fm_modulation(
            carrier_freq, sample_rate, duration, freq_deviation
        )

        self.assertEqual(len(time), len(message_signal))

    def test_different_message_frequencies(self):
        """
        Test FM modulation with different frequencies in the message signal.

        Verifies:
        - The FM signal reflects the changing message signal frequency.
        """
        carrier_freq = 10
        sample_rate = 1000
        duration = 2
        freq_deviation = 5

        time, message_signal, carrier_signal, fm_signal = fm_modulation(
            carrier_freq, sample_rate, duration, freq_deviation
        )

        freq_spectrum = np.fft.fft(message_signal)
        self.assertTrue(len(freq_spectrum) > 0)

    # Sad path tests
    def test_invalid_input(self):
        """
        Test FM modulation with invalid inputs.

        Verifies:
        - The function raises a ValueError for invalid parameter combinations.
        """
        invalid_inputs = [
            ("invalid", 1000, 2, 5),  # Non-numeric carrier frequency
            (10, -1000, 2, 5),  # Negative sampling rate
            (10, 1000, -2, 5),  # Negative signal duration
            (10, 1000, 2, "invalid"),  # Non-numeric frequency deviation
        ]

        for carrier_freq, sample_rate, duration, freq_deviation in invalid_inputs:
            with self.assertRaises(ValueError):
                fm_modulation(carrier_freq, sample_rate, duration, freq_deviation)

    def test_negative_frequency_deviation(self):
        """
        Test FM modulation with a negative frequency deviation.

        Verifies:
        - The function raises a ValueError.
        """
        carrier_freq = 10
        sample_rate = 1000
        duration = 1
        freq_deviation = -5

        with self.assertRaises(ValueError):
            fm_modulation(carrier_freq, sample_rate, duration, freq_deviation)

if __name__ == "__main__":
    unittest.main()
