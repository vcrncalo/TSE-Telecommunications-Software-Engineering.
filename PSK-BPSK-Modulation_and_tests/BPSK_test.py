import numpy as np
import matplotlib.pyplot as plt

# The main BPSK modulation function from your script
def bpsk_modulation(Nbits=4000, baud=900, fs=44100, f0=1800):
    """
    Perform Binary Phase-Shift Keying (BPSK) modulation.

    Parameters:
        Nbits (int): Number of bits in the input signal (default: 4000).
        baud (int): Baud rate or symbol rate (symbols per second, default: 900).
        fs (int): Sampling frequency (Hz, default: 44100).
        f0 (int): Carrier frequency (Hz, default: 1800).

    Returns:
        tuple: Contains the following:
            - t (numpy.ndarray): Time vector for the signal.
            - inputSignal (numpy.ndarray): Digital signal mapped to BPSK levels (-1, 1).
            - carrier1 (numpy.ndarray): Carrier wave (cosine) signal.
            - BPSK_signal (numpy.ndarray): Modulated BPSK signal.
            - fs (int): Sampling frequency used.
    """
    # Configuration
    Ns = int(fs / baud)         # Number of samples per symbol
    N = Nbits * Ns              # Total number of samples
    t = np.arange(0, N) / fs    # Time points
    timeDomainVisibleLimit = 20 / baud  # Limit for representation of time domain signals

    # Signals
    inputBits = np.random.randn(Nbits, 1) > 0
    inputSignal = (np.tile(inputBits * 2 - 1, (1, Ns))).ravel()
    carrier1 = np.cos(2 * np.pi * f0 * t)
    BPSK_signal = inputSignal * carrier1

    return t, inputSignal, carrier1, BPSK_signal, fs  # Return fs too

# Happy Path Tests
def test_happy_path():
    """
    Test BPSK modulation with valid parameters and plot the results.
    """
    # Running BPSK modulation with valid parameters
    t, inputSignal, carrier1, BPSK_signal, fs = bpsk_modulation()

    # Check if the returned arrays are not empty
    assert len(t) > 0, "Time array is empty"
    assert len(inputSignal) > 0, "Input signal is empty"
    assert len(carrier1) > 0, "Carrier signal is empty"
    assert len(BPSK_signal) > 0, "BPSK signal is empty"
    
    # Check the shape consistency
    assert len(inputSignal) == len(BPSK_signal), "Input signal and BPSK signal have different lengths"

    # Optional: Check if values are within expected ranges
    assert np.all(np.abs(inputSignal) == 1), "Input signal values are not correct (-1 or 1)"
    assert np.all(np.isfinite(carrier1)), "Carrier signal contains non-finite values"
    assert np.all(np.isfinite(BPSK_signal)), "BPSK signal contains non-finite values"

    print("Happy path test passed!")

    # Plotting the results (for visualization)
    timeDomainVisibleLimit = 20 / 900  # Same as baud rate to match original settings
    fig, axis = plt.subplots(3, 1, figsize=(10, 8))
    fig.suptitle('BPSK Modulation Signals', fontsize=14)

    axis[0].plot(t[:int(fs * timeDomainVisibleLimit)], inputSignal[:int(fs * timeDomainVisibleLimit)], color='C1')
    axis[0].set_title('Input Signal (Digital)', fontsize=12)
    axis[0].set_xlabel('Time [s]', fontsize=10)
    axis[0].set_ylabel('Amplitude [V]', fontsize=10)
    axis[0].grid(linestyle='dotted')

    axis[1].plot(t[:int(fs * timeDomainVisibleLimit)], carrier1[:int(fs * timeDomainVisibleLimit)], color='C2')
    axis[1].set_title('Carrier Signal', fontsize=12)
    axis[1].set_xlabel('Time [s]', fontsize=10)
    axis[1].set_ylabel('Amplitude [V]', fontsize=10)
    axis[1].grid(linestyle='dotted')

    axis[2].plot(t[:int(fs * timeDomainVisibleLimit)], BPSK_signal[:int(fs * timeDomainVisibleLimit)], color='C3')
    axis[2].set_title('BPSK Modulated Signal', fontsize=12)
    axis[2].set_xlabel('Time [s]', fontsize=10)
    axis[2].set_ylabel('Amplitude [V]', fontsize=10)
    axis[2].grid(linestyle='dotted')

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

# Sad Path Tests (simulating an error)
def test_sad_path():
    """
    Test BPSK modulation with invalid parameters and ensure errors are raised.
    """
    try:
        # Running BPSK modulation with an invalid number of bits (negative value)
        t, inputSignal, carrier1, BPSK_signal, fs = bpsk_modulation(Nbits=-4000)
        print("Sad path test failed: No error raised")
    except Exception as e:
        # Ensure an exception is raised due to invalid Nbits
        assert isinstance(e, ValueError), f"Expected ValueError, got {type(e)}"
        print("Sad path test passed with expected error:", str(e))

# Additional Happy Path Tests
def test_happy_path_2():
    t, inputSignal, carrier1, BPSK_signal, fs = bpsk_modulation(Nbits=5000, baud=1000)
    assert len(inputSignal) == len(BPSK_signal), "Input and BPSK signal lengths mismatch"
    print("Happy path test 2 passed!")

def test_happy_path_3():
    t, inputSignal, carrier1, BPSK_signal, fs = bpsk_modulation(Nbits=6000, baud=1500, f0=2500)
    assert len(inputSignal) == len(BPSK_signal), "Input and BPSK signal lengths mismatch"
    print("Happy path test 3 passed!")

def test_happy_path_4():
    t, inputSignal, carrier1, BPSK_signal, fs = bpsk_modulation(Nbits=10000, baud=500)
    assert len(inputSignal) == len(BPSK_signal), "Input and BPSK signal lengths mismatch"
    print("Happy path test 4 passed!")

def test_happy_path_5():
    t, inputSignal, carrier1, BPSK_signal, fs = bpsk_modulation(Nbits=2000, baud=1200, f0=1500)
    assert len(inputSignal) == len(BPSK_signal), "Input and BPSK signal lengths mismatch"
    print("Happy path test 5 passed!")

# Additional Sad Path Tests
def test_sad_path_2():
    try:
        t, inputSignal, carrier1, BPSK_signal, fs = bpsk_modulation(Nbits=-4000)
        print("Sad path test 2 failed: No error raised")
    except ValueError:
        print("Sad path test 2 passed with ValueError as expected")

def test_sad_path_3():
    try:
        t, inputSignal, carrier1, BPSK_signal, fs = bpsk_modulation(Nbits=4000, baud=0)
        print("Sad path test 3 failed: No error raised")
    except ZeroDivisionError:
        print("Sad path test 3 passed with ZeroDivisionError as expected")

def test_sad_path_4():
    try:
        t, inputSignal, carrier1, BPSK_signal, fs = bpsk_modulation(Nbits=4000, baud=900, f0=-1800)
        print("Sad path test 4 failed: No error raised")
    except ValueError:
        print("Sad path test 4 passed with ValueError as expected for negative frequency")

def test_sad_path_5():
    try:
        t, inputSignal, carrier1, BPSK_signal, fs = bpsk_modulation(Nbits="4000")  # Invalid input type for Nbits
        print("Sad path test 5 failed: No error raised")
    except TypeError:
        print("Sad path test 5 passed with TypeError as expected")

def test_sad_path_6():
    try:
        t, inputSignal, carrier1, BPSK_signal, fs = bpsk_modulation(Nbits=0)  # Invalid Nbits value (zero)
        print("Sad path test 6 failed: No error raised")
    except ValueError:
        print("Sad path test 6 passed with ValueError as expected")

def test_sad_path_7():
    try:
        t, inputSignal, carrier1, BPSK_signal, fs = bpsk_modulation(Nbits=4000, baud=-900)  # Invalid baud rate (negative)
        print("Sad path test 7 failed: No error raised")
    except ValueError:
        print("Sad path test 7 passed with ValueError as expected for negative baud rate")

def test_sad_path_8():
    try:
        t, inputSignal, carrier1, BPSK_signal, fs = bpsk_modulation(Nbits=4000, baud=900, f0=100000)  # Too high carrier frequency
        print("Sad path test 8 failed: No error raised")
    except ValueError:
        print("Sad path test 8 passed with ValueError for excessively high carrier frequency")

def test_sad_path_9():
    try:
        t, inputSignal, carrier1, BPSK_signal, fs = bpsk_modulation(Nbits=4000, baud=900, f0=50000)  # Too high carrier frequency
        print("Sad path test 9 failed: No error raised")
    except ValueError:
        print("Sad path test 9 passed with ValueError for excessively high carrier frequency")

def test_sad_path_10():
    try:
        t, inputSignal, carrier1, BPSK_signal, fs = bpsk_modulation(Nbits=4000, baud=900, fs=-44100)  # Invalid sampling rate
        print("Sad path test 10 failed: No error raised")
    except ValueError:
        print("Sad path test 10 passed with ValueError for negative sampling rate")
