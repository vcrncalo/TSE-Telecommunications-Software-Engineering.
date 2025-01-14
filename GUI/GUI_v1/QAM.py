import numpy as np
import matplotlib.pyplot as plt

def test_happy_path():
    try:
        # Call the script as a function (or encapsulate the logic into a function for testing)
        fs = 44100                  # Sampling rate
        baud = 900                  # Symbol rate
        Nbits = 4000                # Number of bits
        f0 = 1800                   # Carrier frequency
        Ns = int(fs / baud)         # Number of samples per symbol
        N = (Nbits // 4) * Ns       # Total number of samples for 16-QAM
        t = np.arange(0, N) / fs    # Time points
        timeDomainVisibleLimit = 20 / baud  # Limit for representation of time domain signals

        # Signals
        inputBits = np.random.randint(0, 16, Nbits // 4)  # 16-QAM symbols (0 to 15)
        qamMapping = {
            0: (-3, -3),  1: (-3, -1),  2: (-3,  3),  3: (-3,  1),
            4: (-1, -3),  5: (-1, -1),  6: (-1,  3),  7: (-1,  1),
            8: ( 3, -3),  9: ( 3, -1), 10: ( 3,  3), 11: ( 3,  1),
           12: ( 1, -3), 13: ( 1, -1), 14: ( 1,  3), 15: ( 1,  1)
        }

        # Map 16-QAM symbols to I and Q components
        symbols = np.array([qamMapping[bit] for bit in inputBits])
        I_signal = np.repeat(symbols[:, 0], Ns)
        Q_signal = np.repeat(symbols[:, 1], Ns)

        # Generate carrier signals
        carrier_I = np.cos(2 * np.pi * f0 * t)
        carrier_Q = np.sin(2 * np.pi * f0 * t)

        # Modulated QAM signal
        QAM_signal = I_signal * carrier_I - Q_signal * carrier_Q

        # Plotting Digital Signal, Carrier, and Modulated Signal
        fig, axis = plt.subplots(4, 1, figsize=(10, 14))
        fig.suptitle('16-QAM Modulation Signals', fontsize=14)

        axis[0].step(t[:int(fs * timeDomainVisibleLimit)], I_signal[:int(fs * timeDomainVisibleLimit)], color='C1')
        axis[0].set_title('In-phase Component (Digital)', fontsize=12)
        axis[0].set_xlabel('Time [s]', fontsize=10)
        axis[0].set_ylabel('Amplitude [V]', fontsize=10)
        axis[0].grid(linestyle='dotted')

        axis[1].step(t[:int(fs * timeDomainVisibleLimit)], Q_signal[:int(fs * timeDomainVisibleLimit)], color='C2')
        axis[1].set_title('Quadrature Component (Digital)', fontsize=12)
        axis[1].set_xlabel('Time [s]', fontsize=10)
        axis[1].set_ylabel('Amplitude [V]', fontsize=10)
        axis[1].grid(linestyle='dotted')

        axis[2].plot(t[:int(fs * timeDomainVisibleLimit)], carrier_I[:int(fs * timeDomainVisibleLimit)], color='C3')
        axis[2].set_title('Carrier Signal (In-phase)', fontsize=12)
        axis[2].set_xlabel('Time [s]', fontsize=10)
        axis[2].set_ylabel('Amplitude [V]', fontsize=10)
        axis[2].grid(linestyle='dotted')

        axis[3].plot(t[:int(fs * timeDomainVisibleLimit)], QAM_signal[:int(fs * timeDomainVisibleLimit)], color='C4')
        axis[3].set_title('16-QAM Modulated Signal', fontsize=12)
        axis[3].set_xlabel('Time [s]', fontsize=10)
        axis[3].set_ylabel('Amplitude [V]', fontsize=10)
        axis[3].grid(linestyle='dotted')

        plt.tight_layout(rect=[0, 0, 1, 0.96])
        plt.show()

        print("Happy path test passed: Plot generated successfully.")

    except Exception as e:
        print(f"Happy path test failed: {e}")

# Run the happy path test
# test_happy_path()

def test_sad_path():
    try:
        # Testing with an invalid symbol mapping (e.g., missing or incorrect symbols)
        fs = 44100                  # Sampling rate
        baud = 900                  # Symbol rate
        Nbits = 4000                # Number of bits
        f0 = 1800                   # Carrier frequency
        Ns = int(fs / baud)         # Number of samples per symbol
        N = (Nbits // 4) * Ns       # Total number of samples for 16-QAM
        t = np.arange(0, N) / fs    # Time points
        timeDomainVisibleLimit = 20 / baud  # Limit for representation of time domain signals

        # Invalid mapping with missing symbols
        inputBits = np.random.randint(0, 16, Nbits // 4)
        qamMapping = {
            0: (-3, -3),  1: (-3, -1),  2: (-3,  3)  # Missing some symbols
        }

        # Try to map symbols and catch any errors
        try:
            symbols = np.array([qamMapping[bit] for bit in inputBits])
            print("Sad path test failed: No error raised for invalid mapping.")
        except KeyError as e:
            print(f"Sad path test passed: KeyError correctly raised for invalid symbol {e}")

    except Exception as e:
        print(f"Sad path test failed: {e}")

# Run the sad path test
# test_sad_path()

