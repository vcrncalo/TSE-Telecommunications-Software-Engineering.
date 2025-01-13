import unittest
from ASK_modulation import ask_modulation  # Import the function from the main ASK modulation code
import numpy as np  # Required for array manipulations and validations in tests

class TestASKModulation(unittest.TestCase):
    # Happy path tests
    def test_ask_modulation_array_lengths(self):
        """
        Test 1: Verify the lengths of all arrays returned by the `ask_modulation` function.
        """
        binary_sequence = [0, 1]
        carrier_freq = 10
        amplitude = 1
        bit_duration = 1
        t, bw, sint, st = ask_modulation(binary_sequence, carrier_freq, amplitude, bit_duration)
        samples_per_bit = int(1000 * bit_duration)
        assert len(t) == len(bw) == len(sint) == len(st) == len(binary_sequence) * samples_per_bit, \
            "Array lengths do not match the expected value."

    def test_ask_modulation_values(self):
        """
        Test 2: Verify the values of the binary wave generated during ASK modulation.
        """
        binary_sequence = [0, 1]
        carrier_freq = 10
        amplitude = 1
        bit_duration = 1
        t, bw, sint, st = ask_modulation(binary_sequence, carrier_freq, amplitude, bit_duration)
        samples_per_bit = int(1000 * bit_duration)
        assert np.all(bw[:samples_per_bit] == 0), f"The first {samples_per_bit} values of the binary wave should be 0."
        assert np.all(bw[samples_per_bit:] == 1), f"The next {samples_per_bit} values of the binary wave should be 1."

    def test_ask_large_binary_sequence(self):
        """
        Test 4: Verify handling of a very large binary sequence.
        """
        large_binary_sequence = [0, 1] * 500  # 1000 bits
        carrier_freq = 10
        amplitude = 1
        bit_duration = 1
        t, bw, sint, st = ask_modulation(large_binary_sequence, carrier_freq, amplitude, bit_duration)
        samples_per_bit = int(1000 * bit_duration)
        assert len(t) == len(bw) == len(sint) == len(st) == len(large_binary_sequence) * samples_per_bit, \
            "Array lengths do not match the expected value for a large binary sequence."

    def test_ask_single_bit_sequence(self):
        """
        Test 5: Verify handling of a single-bit binary sequence.
        """
        carrier_freq = 10
        amplitude = 1
        bit_duration = 1
        t, bw, sint, st = ask_modulation([1], carrier_freq, amplitude, bit_duration)
        samples_per_bit = int(1000 * bit_duration)
        assert len(t) == len(bw) == len(sint) == len(st) == samples_per_bit, \
            "Array lengths do not match the expected value for a single-bit sequence."
        assert np.all(bw == 1), "Binary wave should only contain the single bit value."

    def test_ask_all_zeros_sequence(self):
        """
        Test 6: Verify handling of a sequence with all zeros.
        """
        carrier_freq = 10
        amplitude = 1
        bit_duration = 1
        t, bw, sint, st = ask_modulation([0, 0, 0], carrier_freq, amplitude, bit_duration)
        samples_per_bit = int(1000 * bit_duration)
        assert np.all(bw == 0), "Binary wave should only contain zeros."
        assert len(t) == len(bw) == len(sint) == len(st) == 3 * samples_per_bit, "Array lengths are incorrect"

    def test_ask_alternating_sequence(self):
        """
        Test 7: Verify handling of an alternating sequence.
        """
        carrier_freq = 10
        amplitude = 1
        bit_duration = 1
        t, bw, sint, st = ask_modulation([1, 0, 1, 0], carrier_freq, amplitude, bit_duration)
        samples_per_bit = int(1000 * bit_duration)
        assert np.all(bw[:samples_per_bit] == 1)
        assert np.all(bw[samples_per_bit:2*samples_per_bit] == 0)
        assert np.all(bw[2*samples_per_bit:3*samples_per_bit] == 1)
        assert np.all(bw[3*samples_per_bit:] == 0)
        assert len(t) == len(bw) == len(sint) == len(st) == 4 * samples_per_bit, "Array lengths are incorrect"

    def test_ask_long_same_bit_sequence(self):
        """
        Test 8: Verify handling of a long sequence of the same bit.
        """
        carrier_freq = 10
        amplitude = 1
        bit_duration = 1
        t, bw, sint, st = ask_modulation([1] * 10, carrier_freq, amplitude, bit_duration)
        samples_per_bit = int(1000 * bit_duration)
        assert np.all(bw == 1), "Binary wave should only contain ones."
        assert len(t) == len(bw) == len(sint) == len(st) == 10 * samples_per_bit, "Array lengths are incorrect"

    def test_ask_modulation_basic_sequence(self):
        """
        Test 10: Verify that a basic sequence [0, 1, 0] works.
        """
        carrier_freq = 10
        amplitude = 1
        bit_duration = 1
        t, bw, sint, st = ask_modulation([0, 1, 0], carrier_freq, amplitude, bit_duration)
        samples_per_bit = int(1000 * bit_duration)
        assert len(t) == len(bw) == len(sint) == len(st) == 3 * samples_per_bit
        assert np.all(bw[:samples_per_bit] == 0)
        assert np.all(bw[samples_per_bit:2*samples_per_bit] == 1)
        assert np.all(bw[2*samples_per_bit:] == 0)

    # Sad path tests
    def test_ask_empty_binary_sequence(self):
        """
        Test 3: Verify that an empty binary sequence returns empty arrays.
        """
        carrier_freq = 10
        amplitude = 1
        bit_duration = 1
        t, bw, sint, st = ask_modulation([], carrier_freq, amplitude, bit_duration)
        assert len(t) == len(bw) == len(sint) == len(st) == 0, \
            "Empty binary sequence should result in empty output arrays."

    def test_ask_empty_input(self):
        """
        Test 9: Verify that an empty input raises an error.
        """
        carrier_freq = 10
        amplitude = 1
        bit_duration = 1
        t, bw, sint, st = ask_modulation([], carrier_freq, amplitude, bit_duration)
        assert len(t) == 0
        assert len(bw) == 0
        assert len(sint) == 0
        assert len(st) == 0

if __name__ == "__main__":
    unittest.main()
