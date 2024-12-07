import numpy as np
import matplotlib.pyplot as plt

# --------------------
def fm_modulation(carrier_freq, sample_rate, duration, freq_deviation):
    """
    FM modulation with given carrier frequency, sampling rate, signal duration, and frequency deviation.
    """
    time = np.arange(0, duration, 1 / sample_rate)  # Time vector with increments of 1 / sample_rate.
    message_signal = np.sin(2 * np.pi * time)  # Message signal: a simple sine wave.
    carrier_signal = np.sin(2 * np.pi * carrier_freq * time)  # Carrier signal: sine wave.
    integral_message = np.cumsum(message_signal) * (1 / sample_rate)  # Numerical integral of the message signal.
    fm_signal = np.sin(2 * np.pi * carrier_freq * time + 2 * np.pi * freq_deviation * integral_message)
    return time, message_signal, carrier_signal, fm_signal
# --------------------
def plot_fm_signals(time, message_signal, carrier_signal, fm_signal, carrier_freq, freq_deviation):
    """
    Function to plot the message signal, carrier signal, and FM signal on separate graphs.
    """
    plt.subplot(3, 1, 1)
    plt.plot(time, message_signal)
    plt.title('Message Signal: sin(2*pi*t)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid()

    plt.subplot(3, 1, 2)
    plt.plot(time, carrier_signal)
    plt.title('Carrier Signal: sin(2*pi*Fc*t)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.text(0, 0.5, f'Fc = {carrier_freq} Hz', fontsize=12, color='blue')

    plt.subplot(3, 1, 3)
    plt.plot(time, fm_signal)
    plt.title('FM Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.text(0, 0.5, f'Fc = {carrier_freq} Hz, Δf = {freq_deviation} Hz', fontsize=12, color='green')

    plt.tight_layout()
    plt.show()
# --------------------
def main_fm(carrier_freq=10, sample_rate=1000, duration=2, freq_deviation=5):
    """
    Main function to execute FM modulation and plot the resulting graphs.
    """
    time, message_signal, carrier_signal, fm_signal = fm_modulation(
        carrier_freq, sample_rate, duration, freq_deviation)
    plot_fm_signals(time, message_signal, carrier_signal, fm_signal, carrier_freq, freq_deviation)
# --------------------
if __name__ == "__main__":
    main_fm()  # Execute the main FM modulation function.



