# Test code for ASK_modulation.py (ASK Modulation)
import numpy as np  # Provides functionality for creating complex arrays and matrices.
from ASK_modulation import ask_modulation  # Import the `ask_modulation` function from the ASK modulation code.

# --------------------
# Define the binary sequence for testing. To ensure all tests pass, use this specific sequence.
binary_sequence = [0, 1]

# --------------------
def test_ask_modulation_array_lengths():
    """
    Test 1: Verify the lengths of all arrays returned by the `ask_modulation` function.

    Checks:
        - All returned arrays (time vector, binary wave, carrier signal, and modulated signal)
          have the same length.
        - The length is equal to the length of the binary sequence multiplied by 100 (repetition factor).
    """
    t, bw, sint, st = ask_modulation(binary_sequence)  # Call the function and retrieve outputs.
    assert len(t) == len(bw) == len(sint) == len(st) == len(binary_sequence) * 100, \
        "Array lengths do not match the expected value."

# --------------------
def test_ask_modulation_values():
    """
    Test 2: Verify the values of the binary wave generated during ASK modulation.

    Checks:
        - The first 100 values in the binary wave array correspond to the first binary bit (0).
        - The subsequent 100 values correspond to the second binary bit (1).
    """
    t, bw, sint, st = ask_modulation(binary_sequence)  # Call the function and retrieve outputs.
    assert np.all(bw[:100] == 0), "The first 100 values of the binary wave should be 0."
    assert np.all(bw[100:] == 1), "The next 100 values of the binary wave should be 1."

# --------------------
# Additional Tests for ASK Modulation

def test_ask_empty_binary_sequence():
    """
    Test 3: Verify that an empty binary sequence returns empty arrays.
    """
    t, bw, sint, st = ask_modulation([])  # Pass an empty binary sequence.
    assert len(t) == len(bw) == len(sint) == len(st) == 0, \
        "Empty binary sequence should result in empty output arrays."

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
    t, bw, sint, st = ask_modulation([1])  # Single-bit sequence.
    assert len(t) == len(bw) == len(sint) == len(st) == 100, \
        "Array lengths do not match the expected value for a single-bit sequence."
    assert np.all(bw == 1), "Binary wave should only contain the single bit value."

def test_ask_invalid_binary_values():
    """
    Test 6: Verify that non-binary values raise an error or produce unexpected results.
    """
    try:
        ask_modulation([2, 3])  # Invalid binary values.
    except ValueError:
        assert True  # Expected behavior: exception is raised.
    else:
        assert "Non-binary values should raise an exception."