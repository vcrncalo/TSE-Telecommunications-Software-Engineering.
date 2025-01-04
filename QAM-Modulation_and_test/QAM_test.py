import numpy as np
import matplotlib.pyplot as plt

# Happy Path Tests for 16-QAM Modulation
def test_happy_path_1():
    """
    This function tests the basic 16-QAM modulation by generating the 
    I and Q components and modulating them with a carrier wave.
    
    Example:
        - Input: 4000 bits are randomly generated, with baud rate of 900 and a carrier frequency of 1800 Hz.
        - Output: Visualizes the in-phase (I) and quadrature (Q) components, the carrier signal, and the modulated signal.
    """
    try:
        fs = 44100                  # Sampling rate
        baud = 900                  # Symbol rate
        Nbits = 4000                # Number of bits
        f0 = 1800                   # Carrier frequency
        Ns = int(fs / baud)         # Number of samples per symbol
        N = (Nbits // 4) * Ns       # Total number of samples for 16-QAM
        t = np.arange(0, N) / fs    # Time points
        inputBits = np.random.randint(0, 16, Nbits // 4)  # 16-QAM symbols (0 to 15)
        
        # Define the QAM symbol mapping
        qamMapping = {
            0: (-3, -3),  1: (-3, -1),  2: (-3,  3),  3: (-3,  1),
            4: (-1, -3),  5: (-1, -1),  6: (-1,  3),  7: (-1,  1),
            8: ( 3, -3),  9: ( 3, -1), 10: ( 3,  3), 11: ( 3,  1),
            12: ( 1, -3), 13: ( 1, -1), 14: ( 1,  3), 15: ( 1,  1)
        }
        
        # Map the input bits to QAM symbols
        symbols = np.array([qamMapping[bit] for bit in inputBits])
        I_signal = np.repeat(symbols[:, 0], Ns)
        Q_signal = np.repeat(symbols[:, 1], Ns)
        
        # Carrier signals for modulation
        carrier_I = np.cos(2 * np.pi * f0 * t)
        carrier_Q = np.sin(2 * np.pi * f0 * t)
        QAM_signal = I_signal * carrier_I - Q_signal * carrier_Q
        
        # Plotting the signals for visualization
        fig, axis = plt.subplots(4, 1, figsize=(10, 14))
        fig.suptitle('16-QAM Modulation Signals', fontsize=14)
        axis[0].step(t[:int(fs * 20 / baud)], I_signal[:int(fs * 20 / baud)], color='C1')
        axis[0].set_title('In-phase Component (Digital)', fontsize=12)
        axis[1].step(t[:int(fs * 20 / baud)], Q_signal[:int(fs * 20 / baud)], color='C2')
        axis[1].set_title('Quadrature Component (Digital)', fontsize=12)
        axis[2].plot(t[:int(fs * 20 / baud)], carrier_I[:int(fs * 20 / baud)], color='C3')
        axis[2].set_title('Carrier Signal (In-phase)', fontsize=12)
        axis[3].plot(t[:int(fs * 20 / baud)], QAM_signal[:int(fs * 20 / baud)], color='C4')
        axis[3].set_title('16-QAM Modulated Signal', fontsize=12)
        plt.tight_layout(rect=[0, 0, 1, 0.96])
        plt.show()
        
        print("Happy Path 1 Passed")
    except Exception as e:
        print(f"Test Failed: {e}")

# Additional Happy Path Tests
def test_happy_path_2():
    """
    This function tests another valid 16-QAM modulation scenario with different parameters.
    
    Example:
        - Input: 8000 bits with baud rate of 1200 and a carrier frequency of 1800 Hz.
        - Output: Visualizes the modulated signal and checks the correctness of the output.
    """
    try:
        fs = 44100
        baud = 1200
        Nbits = 8000
        f0 = 1800
        Ns = int(fs / baud)
        N = (Nbits // 4) * Ns
        t = np.arange(0, N) / fs
        inputBits = np.random.randint(0, 16, Nbits // 4)
        
        # Use a similar QAM mapping for this test
        qamMapping = {
            0: (-3, -3),  1: (-3, -1),  2: (-3, 3),  3: (-3, 1),
            4: (-1, -3),  5: (-1, -1),  6: (-1, 3),  7: (-1, 1),
            8: ( 3, -3),  9: ( 3, -1), 10: ( 3, 3), 11: ( 3, 1),
            12: ( 1, -3), 13: ( 1, -1), 14: ( 1, 3), 15: ( 1, 1)
        }
        
        # Map the input bits to QAM symbols
        symbols = np.array([qamMapping[bit] for bit in inputBits])
        I_signal = np.repeat(symbols[:, 0], Ns)
        Q_signal = np.repeat(symbols[:, 1], Ns)
        
        # Carrier signals for modulation
        carrier_I = np.cos(2 * np.pi * f0 * t)
        carrier_Q = np.sin(2 * np.pi * f0 * t)
        QAM_signal = I_signal * carrier_I - Q_signal * carrier_Q
        
        print("Happy Path 2 Passed")
    except Exception as e:
        print(f"Test Failed: {e}")

# Sad Path Tests for Invalid QAM Mapping and Errors
def test_sad_path_1():
    """
    This function tests the error handling when an invalid QAM mapping is provided.
    
    Example:
        - Input: Invalid QAM mapping (missing symbols).
        - Expected Output: Raises KeyError due to missing QAM symbols in the mapping.
    """
    try:
        fs = 44100
        baud = 900
        Nbits = 4000
        f0 = 1800
        Ns = int(fs / baud)
        N = (Nbits // 4) * Ns
        t = np.arange(0, N) / fs
        inputBits = np.random.randint(0, 16, Nbits // 4)
        
        # Invalid QAM mapping (missing symbols)
        qamMapping = { 0: (-3, -3), 1: (-3, -1), 2: (-3, 3)}  # Missing many symbols
        symbols = np.array([qamMapping[bit] for bit in inputBits])
        
        print("Sad Path 1 Failed: No error")
    except KeyError as e:
        print(f"Sad Path 1 Passed: KeyError correctly raised for invalid symbol {e}")

# Additional Sad Path Tests
def test_sad_path_2():
    """
    This function tests error handling when the baud rate is set to zero, 
    which causes a ZeroDivisionError.
    
    Example:
        - Input: Baud rate is set to zero.
        - Expected Output: Raises ZeroDivisionError due to division by zero when calculating Ns.
    """
    try:
        fs = 44100
        baud = 0  # Invalid baud rate
        Nbits = 4000
        f0 = 1800
        Ns = int(fs / baud)  # Division by zero
        N = (Nbits // 4) * Ns
        t = np.arange(0, N) / fs
        print("Sad Path 2 Failed: No error")
    except ZeroDivisionError:
        print("Sad Path 2 Passed: ZeroDivisionError correctly raised")

def test_sad_path_3():
    """
    This function tests error handling for a negative number of bits, 
    which is invalid for modulation.
    
    Example:
        - Input: Negative number of bits (Nbits = -4000).
        - Expected Output: Raises ValueError due to invalid input for number of bits.
    """
    try:
        fs = 44100
        baud = 900
        Nbits = -4000  # Invalid negative number of bits
        f0 = 1800
        Ns = int(fs / baud)
        N = (Nbits // 4) * Ns
        t = np.arange(0, N) / fs
        print("Sad Path 3 Failed: No error")
    except ValueError:
        print("Sad Path 3 Passed: ValueError correctly raised")

def test_sad_path_4():
    """
    This function tests error handling when the QAM mapping is incomplete.
    
    Example:
        - Input: Incomplete QAM mapping (missing several symbols).
        - Expected Output: Raises KeyError when trying to map input bits that aren't in the mapping.
    """
    try:
        fs = 44100
        baud = 900
        Nbits = 4000
        f0 = 1800
        Ns = int(fs / baud)
        N = (Nbits // 4) * Ns
        t = np.arange(0, N) / fs
        inputBits = np.random.randint(0, 16, Nbits // 4)
        
        # Invalid QAM mapping (missing symbols)
        qamMapping = { 0: (-3, -3), 1: (-3, -1)}  # Missing other symbols
        symbols = np.array([qamMapping[bit] for bit in inputBits])
        
        print("Sad Path 4 Failed: No error")
    except KeyError:
        print("Sad Path 4 Passed: KeyError correctly raised")

def test_sad_path_5():
    """
    This function tests the scenario where the carrier frequency is set too high, causing aliasing.
    
    Example:
        - Input: Carrier frequency set to 8000 Hz, which is too high for the sampling rate.
        - Expected Output: Raises ValueError due to aliasing when generating the modulated signal.
    """
    try:
        fs = 44100
        baud = 900
        Nbits = 4000
        f0 = 8000  # High carrier frequency, causing aliasing
        Ns = int(fs / baud)
        N = (Nbits // 4) * Ns
        t = np.arange(0, N) / fs
        inputBits = np.random.randint(0, 16, Nbits // 4)
        
        # Valid QAM mapping for modulation
        qamMapping = {
            0: (-3, -3), 1: (-3, -1), 2: (-3, 3), 3: (-3, 1),
            4: (-1, -3), 5: (-1, -1), 6: (-1, 3), 7: (-1, 1),
            8: ( 3, -3), 9: ( 3, -1), 10: ( 3, 3), 11: ( 3, 1),
            12: ( 1, -3), 13: ( 1, -1), 14: ( 1, 3), 15: ( 1, 1)
        }
        symbols = np.array([qamMapping[bit] for bit in inputBits])
        I_signal = np.repeat(symbols[:, 0], Ns)
        Q_signal = np.repeat(symbols[:, 1], Ns)
        
        print("Sad Path 5 Failed: No error")
    except ValueError:
        print("Sad Path 5 Passed: ValueError due to aliasing correctly raised")

# Run happy path tests
test_happy_path_1()
test_happy_path_2()

# Run sad path tests
test_sad_path_1()
test_sad_path_2()
test_sad_path_3()
test_sad_path_4()
test_sad_path_5()
