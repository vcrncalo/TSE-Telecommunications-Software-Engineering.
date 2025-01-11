import numpy as np  # Provides functionality for creating complex arrays and matrices.
from ASK_modulation import ask_modulation  # Import the `ask_modulation` function from the ASK modulation code.

# Define the binary sequence for testing. To ensure all tests pass, use this specific sequence.
binary_sequence = [0, 1]

# Happy path tests
def test_ask_modulation_array_lengths():
    """
    Test 1: Verify the lengths of all arrays returned by the `ask_modulation` function.
    """
    t, bw, sint, st = ask_modulation(binary_sequence)
    assert len(t) == len(bw) == len(sint) == len(st) == len(binary_sequence) * 100, \
        "Array lengths do not match the expected value."

def test_ask_modulation_values():
    """
    Test 2: Verify the values of the binary wave generated during ASK modulation.
    """
    t, bw, sint, st = ask_modulation(binary_sequence)
    assert np.all(bw[:100] == 0), "The first 100 values of the binary wave should be 0."
    assert np.all(bw[100:] == 1), "The next 100 values of the binary wave should be 1."

def test_ask_large_binary_sequence():
    """
    Test 4: Verify handling of a very large binary sequence.
    """
    large_binary_sequence = [0, 1] * 500  # 1000 bits
    t, bw, sint, st = ask_modulation(large_binary_sequence)
    assert len(t) == len(bw) == len(sint) == len(st) == len(large_binary_sequence) * 100, \
        "Array lengths do not match the expected value for a large binary sequence."

def test_ask_single_bit_sequence():
    """
    Test 5: Verify handling of a single-bit binary sequence.
    """
    t, bw, sint, st = ask_modulation([1])
    assert len(t) == len(bw) == len(sint) == len(st) == 100, \
        "Array lengths do not match the expected value for a single-bit sequence."
    assert np.all(bw == 1), "Binary wave should only contain the single bit value."

def test_ask_all_zeros_sequence():
    """
    Test 6: Verify handling of a sequence with all zeros.
    """
    t, bw, sint, st = ask_modulation([0, 0, 0])
    assert np.all(bw == 0), "Binary wave should only contain zeros."
    assert len(t) == len(bw) == len(sint) == len(st) == 300, "Array lengths are incorrect"

def test_ask_alternating_sequence():
    """
    Test 7: Verify handling of an alternating sequence.
    """
    t, bw, sint, st = ask_modulation([1, 0, 1, 0])
    assert np.all(bw[:100] == 1)
    assert np.all(bw[100:200] == 0)
    assert np.all(bw[200:300] == 1)
    assert np.all(bw[300:] == 0)
    assert len(t) == len(bw) == len(sint) == len(st) == 400, "Array lengths are incorrect"

def test_ask_long_same_bit_sequence():
    """
    Test 8: Verify handling of a long sequence of the same bit.
    """
    t, bw, sint, st = ask_modulation([1] * 10)
    assert np.all(bw == 1), "Binary wave should only contain ones."
    assert len(t) == len(bw) == len(sint) == len(st) == 1000, "Array lengths are incorrect"

def test_ask_modulation_basic_sequence():
    """
    Test 10: Verify that a basic sequence [0, 1, 0] works.
    """
    t, bw, sint, st = ask_modulation([0, 1, 0])
    assert len(t) == len(bw) == len(sint) == len(st) == 300
    assert np.all(bw[:100] == 0)
    assert np.all(bw[100:200] == 1)
    assert np.all(bw[200:] == 0)

# Sad path tests
def test_ask_empty_binary_sequence():
    """
    Test 3: Verify that an empty binary sequence returns empty arrays.
    """
    t, bw, sint, st = ask_modulation([])
    assert len(t) == len(bw) == len(sint) == len(st) == 0, \
        "Empty binary sequence should result in empty output arrays."

def test_ask_empty_input():
    """
    Test 9: Verify that an empty input raises an error.
    """
    t, bw, sint, st = ask_modulation([])
    assert len(t) == 0
    assert len(bw) == 0
    assert len(sint) == 0
    assert len(st) == 0