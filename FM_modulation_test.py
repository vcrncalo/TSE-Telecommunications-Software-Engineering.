import unittest
from FM_modulation import fm_modulation  # Import the functions from the main code
import numpy as np  # Required for array manipulations in tests

class TestFMModulation(unittest.TestCase):
    def test_increasing_carrier_frequency(self):
        """Test FM modulation with an increasing carrier frequency."""
        carrier_freq = 50
        sample_rate = 1000
        duration = 2
        freq_deviation = 5

        #Call
        time, message_signal, carrier_signal, fm_signal = fm_modulation(carrier_freq, sample_rate, duration, freq_deviation)
        
        #Veriy
        self.assertEqual(len(time), len(message_signal))
        self.assertEqual(len(time), len(carrier_signal))
        self.assertEqual(len(time), len(fm_signal))

    def test_frequency_deviation_change(self):
        """Test FM modulation with different frequency deviation."""
        carrier_freq = 10
        sample_rate = 1000
        duration = 2
        freq_deviation = 20

        # Calling the FM modulation function
        time, message_signal, carrier_signal, fm_signal = fm_modulation(carrier_freq, sample_rate, duration, freq_deviation)
        
        # Calculate instantaneous frequency deviation
        phase = np.unwrap(np.angle(np.sin(2 * np.pi * carrier_freq * time + 2 * np.pi * freq_deviation * np.cumsum(message_signal) * (1 / sample_rate))))
        instantaneous_frequency = np.diff(phase) * sample_rate / (2 * np.pi)

        # Verify the maximum frequency deviation
        max_deviation = np.max(np.abs(instantaneous_frequency - carrier_freq))
        self.assertTrue(max_deviation >= freq_deviation, f"Expected max deviation >= {freq_deviation}, got {max_deviation}")

    def test_short_signal_duration(self):
        """Test FM modulation with a shorter signal duration."""
        carrier_freq = 10
        sample_rate = 1000
        duration = 0.5
        freq_deviation = 5

        # Calling the FM modulation function
        time, message_signal, carrier_signal, fm_signal = fm_modulation(carrier_freq, sample_rate, duration, freq_deviation)

        # Verifyin the total duration of the signal
        expected_duration = duration
        self.assertAlmostEqual(time[-1], expected_duration - (1 / sample_rate), delta=1e-6, msg=f"Expected time[-1] close to {expected_duration}")

    def test_low_sample_rate(self):
        """Test FM modulation with a lower sampling rate."""
        carrier_freq = 10
        sample_rate = 100
        duration = 2
        freq_deviation = 5

        # Call the FM modulation function
        time, message_signal, carrier_signal, fm_signal = fm_modulation(carrier_freq, sample_rate, duration, freq_deviation)

        # Verify signal lengths
        self.assertEqual(len(time), len(message_signal))
        self.assertEqual(len(time), len(carrier_signal))
        self.assertEqual(len(time), len(fm_signal))

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
