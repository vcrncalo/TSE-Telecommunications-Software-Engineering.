import unittest
from FM_modulation import fm_modulation, plot_fm_signals  # Import the functions from the main code
import numpy as np  # Required for array manipulations in tests

class TestFMModulation(unittest.TestCase):
    def test_increasing_carrier_frequency(self):
        """Test FM modulation with an increasing carrier frequency."""
        carrier_freq = 50
        sample_rate = 1000
        duration = 2
        freq_deviation = 5

        # Call the FM modulation function
        time, message_signal, carrier_signal, fm_signal = fm_modulation(carrier_freq, sample_rate, duration, freq_deviation)
        plot_fm_signals(time, message_signal, carrier_signal, fm_signal, carrier_freq, freq_deviation)

        # Verify the length of the generated signals
        self.assertEqual(len(time), len(message_signal))
        self.assertEqual(len(time), len(carrier_signal))
        self.assertEqual(len(time), len(fm_signal))

    def test_frequency_deviation_change(self):
        """Test FM modulation with different frequency deviation."""
        carrier_freq = 10
        sample_rate = 1000
        duration = 2
        freq_deviation = 20

        # Call the FM modulation function
        time, message_signal, carrier_signal, fm_signal = fm_modulation(carrier_freq, sample_rate, duration, freq_deviation)
        plot_fm_signals(time, message_signal, carrier_signal, fm_signal, carrier_freq, freq_deviation)

        # Verify the frequency deviation is reflected in the FM signal
        self.assertTrue(np.max(np.abs(fm_signal - carrier_signal)) > freq_deviation)

    def test_short_signal_duration(self):
        """Test FM modulation with a shorter signal duration."""
        carrier_freq = 10
        sample_rate = 1000
        duration = 0.5
        freq_deviation = 5

        # Call the FM modulation function
        time, message_signal, carrier_signal, fm_signal = fm_modulation(carrier_freq, sample_rate, duration, freq_deviation)
        plot_fm_signals(time, message_signal, carrier_signal, fm_signal, carrier_freq, freq_deviation)

        # Verify the total duration of the signal
        expected_duration = duration
        self.assertAlmostEqual(time[-1], expected_duration, delta=1 / sample_rate)

    def test_low_sample_rate(self):
        """Test FM modulation with a lower sampling rate."""
        carrier_freq = 10
        sample_rate = 100
        duration = 2
        freq_deviation = 5

        # Call the FM modulation function
        time, message_signal, carrier_signal, fm_signal = fm_modulation(carrier_freq, sample_rate, duration, freq_deviation)
        plot_fm_signals(time, message_signal, carrier_signal, fm_signal, carrier_freq, freq_deviation)

    def test_invalid_input(self):
        """Test FM modulation with invalid inputs."""
        # Define invalid inputs
        invalid_inputs = [
            ("invalid", 1000, 2, 5),  # Non-numeric carrier frequency
            (10, -1000, 2, 5),  # Negative sample rate
            (10, 1000, -2, 5),  # Negative duration
            (10, 1000, 2, "invalid"),  # Non-numeric frequency deviation
        ]

        for carrier_freq, sample_rate, duration, freq_deviation in invalid_inputs:
            with self.assertRaises(ValueError):
                fm_modulation(carrier_freq, sample_rate, duration, freq_deviation)


if __name__ == "__main__":
    unittest.main()
