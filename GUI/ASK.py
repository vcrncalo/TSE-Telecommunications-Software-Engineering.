import numpy as np  # For mathematical operations and generating signals.
import matplotlib.pyplot as plt  # For creating plots.
import pytest  # For testing

# --------------------
# Code for ASK Modulation
# --------------------
def ask_modulation(binary_sequence):
    """
    Generates ASK (Amplitude Shift Keying) modulation components for a given binary sequence.

    Parameters:
        binary_sequence (list): A binary sequence (e.g., [1, 0, 1, 0]).

    Returns:
        tuple: Contains the following:
            - t (numpy array): Time vector for the signal.
            - bw (numpy array): Repeated binary sequence to match the signal duration.
            - sint (numpy array): Carrier sinusoidal signal.
            - st (numpy array): ASK modulated signal.
    """
    n = len(binary_sequence)  # Length of the binary sequence.
    bw = np.repeat(binary_sequence, 100)  # Each bit is repeated 100 times.
    t = np.linspace(0, n, len(bw))  # Time vector from 0 to n with len(bw) points.
    sint = np.sin(2 * np.pi * t)  # Carrier sinusoidal signal.
    st = bw * sint  # ASK modulated signal is the product of the binary signal and the sinusoidal signal.
    return t, bw, sint, st  # Return the components.


# --------------------
def plot_ask_signals(t, bw, sint, st):
    """
    Plots the digital signal, carrier signal, and ASK modulated signal.

    Parameters:
        t (numpy array): Time vector for the signal.
        bw (numpy array): Repeated binary sequence.
        sint (numpy array): Carrier sinusoidal signal.
        st (numpy array): ASK modulated signal.
    """
    plt.figure(figsize=(10, 5))  # Set the figure size.

    # Plot the digital signal.
    plt.subplot(3, 1, 1)  # 3 rows, 1 column, first plot.
    plt.plot(t, bw, linewidth=1.5)  # Plot the digital signal.
    plt.grid(True)  # Enable grid.
    plt.axis([0, max(t), -2, 2])  # Set x and y axis limits.
    plt.title('Digital Signal')  # Title of the plot.
    plt.xlabel('Time')  # Label for the x-axis.
    plt.ylabel('Amplitude')  # Label for the y-axis.

    # Plot the carrier signal.
    plt.subplot(3, 1, 2)
    plt.plot(t, sint, linewidth=1.5)
    plt.grid(True)
    plt.axis([0, max(t), -2, 2])
    plt.title('Carrier Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')

    # Plot the ASK modulated signal.
    plt.subplot(3, 1, 3)
    plt.plot(t, st, linewidth=1.5)
    plt.grid(True)
    plt.axis([0, max(t), -2, 2])
    plt.title('ASK Modulated Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')

    plt.tight_layout()  # Adjust layout to prevent overlapping.
    plt.show()  # Display the plot.


# --------------------
def main_ask_modulation(binary_sequence=[0, 1]):
    """
    Main function to execute ASK modulation and visualize the results.

    Parameters:
    - binary_sequence: Binary sequence for ASK modulation (default: [0, 1]).

    Returns:
    - t: Time vector for the signal.
    - bw: Repeated binary sequence.
    - sint: Carrier sinusoidal signal.
    - st: ASK modulated signal.
    """
    # Perform ASK modulation and obtain the components.
    t, bw, sint, st = ask_modulation(binary_sequence)

    # Plot the ASK signals.
    plot_ask_signals(t, bw, sint, st)

    return t, bw, sint, st


# --------------------
# Happy Path Test (Only one test to ensure the graph is plotted and signals are generated)
def test_happy_path_ask():
    """
    Test 1: Verify that the ASK modulation works correctly and generates the plots.
    """
    binary_sequence = [0, 1]
    t, bw, sint, st = ask_modulation(binary_sequence)  # Call the function and retrieve outputs.

    # Ensure the signals have been generated with correct length.
    expected_length = len(binary_sequence) * 100  # Expected vector length.
    assert len(t) == len(bw) == len(sint) == len(st) == expected_length, \
        "Array lengths do not match the expected value."

    # Call the plot function to verify the plot is shown.
    plot_ask_signals(t, bw, sint, st)


# --------------------
# Sad Path Tests (Tests for invalid inputs)
def test_sad_path_invalid_ask_signal():
    """
    Test 2: Verify handling of invalid parameters (e.g., empty binary sequence).
    """
    try:
        ask_modulation([])  # Invalid binary sequence (empty list).
        assert False, "Expected an error due to empty binary sequence."
    except ValueError as e:
        assert str(e) == "Binary sequence cannot be empty."


# --------------------
# Run tests
if __name__ == "__main__":
    # Run the main function to generate ASK signals.
    binary_sequence = input(
        "Enter a binary sequence in the format [1, 0, 1, 0] with brackets, commas, and spaces: ")
    # Convert user input into a list of integers.
    binary_sequence = list(map(int, binary_sequence.strip('[]').split(",")))

    # Perform ASK modulation and plot the signals.
    main_ask_modulation(binary_sequence)

    # Run happy path test (only one test that checks the ASK functionality)
    print("Running Happy Path Test...")
    pytest.main(["-v", "test_happy_path_ask"])

    # Run sad path tests
    print("Running Sad Path Test...")
    pytest.main(["-v", "test_sad_path_invalid_ask_signal"])

