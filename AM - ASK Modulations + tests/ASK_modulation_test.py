# Test code for ASK_modulation.py (ASK Modulation)
import numpy as np  # Provides functionality for creating complex arrays and matrices.
from ASK_modulation import ask_modulation  # Import the `ask_modulation` function from the ASK modulation code.

# --------------------
# Define the binary sequence for testing. To ensure all tests pass, use this specific sequence.
binary_sequence = [0, 1]


# Alternate test sequence: binary_sequence = [1, 0]

# --------------------
def test_ask_modulation_array_lengths():
    """
    Test to verify the lengths of all arrays returned by the `ask_modulation` function.

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
    Test to verify the values of the binary wave generated during ASK modulation.

    Checks:
        - The first 100 values in the binary wave array correspond to the first binary bit (0).
        - The subsequent 100 values correspond to the second binary bit (1).
    """
    t, bw, sint, st = ask_modulation(binary_sequence)  # Call the function and retrieve outputs.
    assert np.all(bw[:100] == 0), "The first 100 values of the binary wave should be 0."
    assert np.all(bw[100:] == 1), "The next 100 values of the binary wave should be 1."

# --------------------
