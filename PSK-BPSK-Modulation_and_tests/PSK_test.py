import numpy as np
import matplotlib.pyplot as plt

# Define signal parameters for generating the digital signal, modulated signal, and carrier signal
def generate_signal(duration, fc, bit_rate, bits_per_symbol):
    num_symbols = int(duration * bit_rate / bits_per_symbol)  # Calculate number of symbols

    # Define 16-PSK constellation
    constellation = np.exp(1j * np.pi / 8 * np.arange(16))

    # Generate random bit sequence
    bits = np.random.randint(0, 2, size=num_symbols * bits_per_symbol)

    # Encode bits into symbols
    symbols = []
    for i in range(0, len(bits), bits_per_symbol):
        index = int(''.join(map(str, bits[i:i+bits_per_symbol])), 2)
        symbols.append(constellation[index])

    # Time vector for signal generation
    t = np.linspace(0, duration, int(duration * bit_rate), endpoint=False)

    # Generate the modulated signal
    signal = np.zeros_like(t, dtype=np.complex128)
    for i, symbol in enumerate(symbols):
        start_index = i * int(bit_rate / bits_per_symbol)
        end_index = start_index + int(bit_rate / bits_per_symbol)
        signal[start_index:end_index] = symbol * np.exp(1j * 2 * np.pi * fc * t[start_index:end_index])

    # Generate the carrier signal (pure cosine wave)
    carrier_signal = np.cos(2 * np.pi * fc * t)

    # Generate the information signal as a continuous waveform
    info_signal = np.zeros_like(t)
    for i, symbol in enumerate(symbols):
        start_index = i * int(bit_rate / bits_per_symbol)
        end_index = start_index + int(bit_rate / bits_per_symbol)
        info_signal[start_index:end_index] = np.real(symbol)

    return t, info_signal, carrier_signal, signal

# Plot the signals
def plot_signals(t, info_signal, carrier_signal, modulated_signal, title="Signal Plots"):
    plt.figure(figsize=(20, 10))

    # Information signal plot (Continuous waveform of modulated symbols)
    plt.subplot(3, 1, 1)
    plt.plot(t, info_signal, color='g', label='Information Signal (Continuous)')
    plt.title('Information Signal (Continuous)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend()

    # Carrier signal plot (Carrier Wave)
    plt.subplot(3, 1, 2)
    plt.plot(t, carrier_signal, color='b', label='Carrier Signal')
    plt.title('Carrier Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend()

    # Modulated signal plot (16-PSK Modulation)
    plt.subplot(3, 1, 3)
    plt.plot(t, modulated_signal.real, color='r', label='16-PSK Modulated Signal')
    plt.title('16-PSK Modulated Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.xlim(0, t[-1])
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Happy Path Tests

def test_valid_duration_1():
    print("Running Happy Path Test: Valid Duration (1)...")
    try:
        duration = 2.0  # seconds
        fc = 6  # Hz
        bit_rate = 5000  # bps
        bits_per_symbol = 4  # 16-PSK
        
        t, info_signal, carrier_signal, signal = generate_signal(duration, fc, bit_rate, bits_per_symbol)
        
        plot_signals(t, info_signal, carrier_signal, signal)
        print("Test passed successfully.")
    except Exception as e:
        print(f"Error: {e}")

def test_valid_duration_2():
    print("Running Happy Path Test: Valid Duration (2)...")
    try:
        duration = 5.0  # seconds
        fc = 10  # Hz
        bit_rate = 2000  # bps
        bits_per_symbol = 8  # 256-PSK
        
        t, info_signal, carrier_signal, signal = generate_signal(duration, fc, bit_rate, bits_per_symbol)
        
        plot_signals(t, info_signal, carrier_signal, signal)
        print("Test passed successfully.")
    except Exception as e:
        print(f"Error: {e}")

def test_valid_frequency():
    print("Running Happy Path Test: Valid Carrier Frequency...")
    try:
        duration = 2.0  # seconds
        fc = 10  # Hz (Valid frequency)
        bit_rate = 5000  # bps
        bits_per_symbol = 4  # 16-PSK
        
        t, info_signal, carrier_signal, signal = generate_signal(duration, fc, bit_rate, bits_per_symbol)
        
        plot_signals(t, info_signal, carrier_signal, signal)
        print("Test passed successfully.")
    except Exception as e:
        print(f"Error: {e}")

def test_valid_bits_per_symbol():
    print("Running Happy Path Test: Valid Bits Per Symbol...")
    try:
        duration = 2.0  # seconds
        fc = 6  # Hz
        bit_rate = 5000  # bps
        bits_per_symbol = 8  # 256-PSK
        
        t, info_signal, carrier_signal, signal = generate_signal(duration, fc, bit_rate, bits_per_symbol)
        
        plot_signals(t, info_signal, carrier_signal, signal)
        print("Test passed successfully.")
    except Exception as e:
        print(f"Error: {e}")

def test_short_duration():
    print("Running Happy Path Test: Short Duration...")
    try:
        duration = 0.1  # seconds
        fc = 6  # Hz
        bit_rate = 5000  # bps
        bits_per_symbol = 4  # 16-PSK
        
        t, info_signal, carrier_signal, signal = generate_signal(duration, fc, bit_rate, bits_per_symbol)
        
        plot_signals(t, info_signal, carrier_signal, signal)
        print("Test passed successfully.")
    except Exception as e:
        print(f"Error: {e}")

def test_high_bit_rate():
    print("Running Happy Path Test: High Bit Rate...")
    try:
        duration = 2.0  # seconds
        fc = 6  # Hz
        bit_rate = 10000  # bps
        bits_per_symbol = 4  # 16-PSK
        
        t, info_signal, carrier_signal, signal = generate_signal(duration, fc, bit_rate, bits_per_symbol)
        
        plot_signals(t, info_signal, carrier_signal, signal)
        print("Test passed successfully.")
    except Exception as e:
        print(f"Error: {e}")

def test_multiple_symbols():
    print("Running Happy Path Test: Multiple Symbols...")
    try:
        duration = 2.0  # seconds
        fc = 6  # Hz
        bit_rate = 5000  # bps
        bits_per_symbol = 8  # 256-PSK
        
        t, info_signal, carrier_signal, signal = generate_signal(duration, fc, bit_rate, bits_per_symbol)
        
        plot_signals(t, info_signal, carrier_signal, signal)
        print("Test passed successfully.")
    except Exception as e:
        print(f"Error: {e}")

def test_varied_bit_rate():
    print("Running Happy Path Test: Varied Bit Rate...")
    try:
        duration = 2.0  # seconds
        fc = 6  # Hz
        bit_rate = 1500  # bps
        bits_per_symbol = 4  # 16-PSK
        
        t, info_signal, carrier_signal, signal = generate_signal(duration, fc, bit_rate, bits_per_symbol)
        
        plot_signals(t, info_signal, carrier_signal, signal)
        print("Test passed successfully.")
    except Exception as e:
        print(f"Error: {e}")

def test_high_frequency():
    print("Running Happy Path Test: High Frequency...")
    try:
        duration = 2.0  # seconds
        fc = 50  # Hz (High frequency)
        bit_rate = 5000  # bps
        bits_per_symbol = 4  # 16-PSK
        
        t, info_signal, carrier_signal, signal = generate_signal(duration, fc, bit_rate, bits_per_symbol)
        
        plot_signals(t, info_signal, carrier_signal, signal)
        print("Test passed successfully.")
    except Exception as e:
        print(f"Error: {e}")

def test_long_duration():
    print("Running Happy Path Test: Long Duration...")
    try:
        duration = 10.0  # seconds
        fc = 6  # Hz
        bit_rate = 5000  # bps
        bits_per_symbol = 4  # 16-PSK
        t, info_signal, carrier_signal, signal = generate_signal(duration, fc, bit_rate, bits_per_symbol)
        
        plot_signals(t, info_signal, carrier_signal, signal)
        print("Test passed successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Sad Path Tests

def test_invalid_duration_negative():
    print("Running Sad Path Test: Invalid Negative Duration...")
    try:
        duration = -1.0  # Invalid negative duration
        fc = 6  # Hz
        bit_rate = 5000  # bps
        bits_per_symbol = 4  # 16-PSK
        
        t, info_signal, carrier_signal, signal = generate_signal(duration, fc, bit_rate, bits_per_symbol)
        
        plot_signals(t, info_signal, carrier_signal, signal)
        print("Sad path test passed successfully (unexpected behavior).")
    except Exception as e:
        print(f"Error: {e}")

def test_invalid_bit_rate_zero():
    print("Running Sad Path Test: Invalid Zero Bit Rate...")
    try:
        duration = 2.0  # seconds
        fc = 6  # Hz
        bit_rate = 0  # Invalid zero bit rate
        bits_per_symbol = 4  # 16-PSK
        
        t, info_signal, carrier_signal, signal = generate_signal(duration, fc, bit_rate, bits_per_symbol)
        
        plot_signals(t, info_signal, carrier_signal, signal)
        print("Sad path test passed successfully (unexpected behavior).")
    except Exception as e:
        print(f"Error: {e}")

def test_invalid_frequency_high():
    print("Running Sad Path Test: Invalid High Frequency...")
    try:
        duration = 2.0  # seconds
        fc = 1000000  # Invalid high frequency
        bit_rate = 5000  # bps
        bits_per_symbol = 4  # 16-PSK
        
        t, info_signal, carrier_signal, signal = generate_signal(duration, fc, bit_rate, bits_per_symbol)
        
        plot_signals(t, info_signal, carrier_signal, signal)
        print("Sad path test passed successfully (unexpected behavior).")
    except Exception as e:
        print(f"Error: {e}")

def test_invalid_bit_rate_negative():
    print("Running Sad Path Test: Invalid Negative Bit Rate...")
    try:
        duration = 2.0  # seconds
        fc = 6  # Hz
        bit_rate = -5000  # Invalid negative bit rate
        bits_per_symbol = 4  # 16-PSK
        
        t, info_signal, carrier_signal, signal = generate_signal(duration, fc, bit_rate, bits_per_symbol)
        
        plot_signals(t, info_signal, carrier_signal, signal)
        print("Sad path test passed successfully (unexpected behavior).")
    except Exception as e:
        print(f"Error: {e}")

def test_invalid_symbol_rate():
    print("Running Sad Path Test: Invalid Symbol Rate...")
    try:
        duration = 2.0  # seconds
        fc = 6  # Hz
        bit_rate = 5000  # bps
        bits_per_symbol = 4  # 16-PSK
        
        # Overwrite symbol rate to make it invalid
        bits_per_symbol = 999  # Invalid symbol rate
        
        t, info_signal, carrier_signal, signal = generate_signal(duration, fc, bit_rate, bits_per_symbol)
        
        plot_signals(t, info_signal, carrier_signal, signal)
        print("Sad path test passed successfully (unexpected behavior).")
    except Exception as e:
        print(f"Error: {e}")
