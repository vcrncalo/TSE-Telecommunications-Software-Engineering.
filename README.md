# Telecommunications software engineering - Digital transmitter design and signal modulation

## Project Goal

*The goal of this project is to design a basic digital transmitter, focusing on:*  
- Signal generation,  
- Implementation of various modulation techniques,  
- Analysis of a communication channel with noise, 
- Evaluation of the efficiency and robustness of different modulation schemes.

---

## Project Description

This project explores the concept of a digital transmitter, how it operates, and how signals are generated and prepared for transmission through a communication channel. It delves into the practical aspects of signal modulation and the challenges of transmitting signals through noisy channels.

### Main Activities

1. *Designing a digital transmitter:* 
   - Developing a foundational digital transmitter using Python, focusing on modular design and clear signal processing steps.

2. *Implementation of modulation schemes:*
   - Amplitude Modulation (AM),
   - Amplitude Shift Keying (ASK),
   - Frequency Modulation (FM),
   - Frequency Shift Keying (FSK),
   - Phase Shift Keying (PSK),
   - Binary Phase Shift Keying (BPSK),
   - Quadrature Amplitude Modulation (QAM),
   - Quadrature Phase Shift Keying (QPSK).

3. *Simulation of a communication channel with noise:*  
   - Implementing a channel with Additive White Gaussian Noise (AWGN).  
   - Analyzing the Signal-to-Noise Ratio (SNR).

4. *Evaluation of efficiency and robustness:*
   - Assessing the energy efficiency of each modulation scheme.  
   - Analyzing noise resistance.

## Repository Structure

|Directory/File name|Description|
|--------------|-----------|
|AM-ASK+tests|This directory contains all code files necessary for AM and ASK modulations, as well as their respective test files and modulation images.|
|FM-FSK+tests|This directory contains all code files necessary for FM and FSK modulations, as well as their respective test files and modulation images.|
|PSK-BPSK+tests|This directory contains all code files necessary for PSK and BPSK modulations, as well as their respective test files and modulation images.|
|QAM-QPSK+tests|This directory contains all code files necessary for QAM and QPSK modulations, as well as their respective test files and modulation images.|
|GUI|This directory contains all code files necessary for the GUI.|
|Images|This directory contains a variety of images related to modulations and tests.|
|.github|This directory contains test.yml file which checks all tests and will notify the user if the tests don't pass (useful for debugging)|
|.coverage|This file was generated with `pytest -v -cov`, it run all Python tests in the root directory|
|README.md|Project details.|

---

## Modulation techniques

### Amplitude Modulation (AM)

**Amplitude Modulation (AM)** is a modulation technique where the amplitude of the carrier signal is varied in proportion to the instantaneous amplitude of the message signal. It's a simple method but is susceptible to noise.

<details>
<summary>Amplitude Modulation (AM) image</summary>
<p align="center">
<img src=Modulation_files/AM-ASK+tests/Images/AM_modulation.png>
<br>
Figure 1: Amplitude modulation
</p>
</details>

### Amplitude Shift Keying (ASK)

**Amplitude Shift Keying (ASK)** is a form of amplitude modulation that represents digital data as variations in the amplitude of a carrier wave. In its simplest form, the presence of a carrier wave represents a binary 1, and the absence represents a binary 0.

<details>
<summary>Amplitude Shift Keying (ASK) image</summary>
<p align="center">
<img src=Modulation_files/AM-ASK+tests/Images/ASK_modulation.png>
<br>
Figure 2: Amplitude shift keying
</p>
</details>

### Frequency Modulation (FM)

**Frequency Modulation (FM)** is a modulation technique where the frequency of the carrier signal is varied in proportion to the instantaneous amplitude of the message signal. FM is less susceptible to noise than AM.

<details>
<summary>Frequency Modulation (FM) image</summary>
<p align="center">
<img src=Modulation_files/FM-FSK+tests/Images/FM_modulation.png>
<br>
Figure 3: Frequency modulation
</p>
</details>

### Frequency Shift Keying (FSK)

**Frequency Shift Keying (FSK)** is a form of frequency modulation that represents digital data as variations in the frequency of a carrier wave. Different frequencies are used to represent different binary values.

<details>
<summary>Frequency Shift Keying (FSK) image</summary>
<p align="center">
<img src=Modulation_files/FM-FSK+tests/Images/FSK_modulation.png>
<br>
Figure 4: Frequency shift keying
</p>
</details>

### Phase Shift Keying (PSK)

**Phase Shift Keying (PSK)** is a modulation technique where the phase of the carrier signal is varied to represent digital data. The amplitude and frequency of the carrier signal remain constant.

<details>
<summary>Phase Shift Keying (PSK) image</summary>
<p align="center">
<img src=Modulation_files/PSK-BPSK+tests/Images/PSK_modulation.png>
<br>
Figure 5: Phase shift keying
</p>
</details>

### Binary Phase Shift Keying (BPSK)

**Binary Phase Shift Keying (BPSK)** is a form of phase shift keying where the phase of the carrier signal is varied to represent binary data. It uses two phases to represent binary 0 and 1.

<details>
<summary>Binary Phase Shift Keying (BPSK) image</summary>
<p align="center">
<img src=Modulation_files/PSK-BPSK+tests/Images/BPSK_modulation.png>
<br>
Figure 6: Binary phase shift keying
</p>
</details>

### Quadrature Amplitude Modulation (QAM)

**Quadrature Amplitude Modulation (QAM)** is a modulation technique that combines both amplitude and phase modulation to transmit more data per symbol. It uses multiple amplitude levels and phase shifts to encode data.

<details>
<summary>Quadrature Amplitude Modulation (QAM) image</summary>
<p align="center">
<img src=Modulation_files/QAM-QPSK+tests/Images/QAM_modulation.png>
<br>
Figure 6: Quadrature amplitude modulation
</p>
</details>

### Quadrature Phase Shift Keying (QPSK)

**Quadrature Phase Shift Keying (QPSK)** is a form of phase shift keying where the phase of the carrier signal is varied to represent digital data. It uses four phases to represent two bits of data.

<details>
<summary>Quadrature Phase Shift Keying (QPSK) image</summary>
<p align="center">
<img src=Modulation_files/QAM-QPSK+tests/Images/QPSK_modulation.png>
<br>
Figure 7: Quadrature phase shift keying
</p>
</details>

---

## Pytest

*The pytest framework is used to run the tests for each modulation technique. The tests can be run with: `pytest -v -cov 'file.py'`.*

*Figure 8 shows how pytest output looks when running the tests for all the modulation techniques:*

<p align="center">
<img src=Images/Main_coverage.png>
<br>
Figure 8: Code coverage
</p>

---

## Doxygen

**Doxygen** is a documentation generator used across several programming languages, including Python. It parses specially-formatted comments within the code to produce documentation in various formats like HTML, LaTeX, and man pages.

### Doxyfile

A **Doxyfile** is Doxygen's configuration file, controlling the documentation generation process. It specifies settings such as input files, output directories, and documentation style. Doxyfile can be generated with: `doxygen -g Doxyfile`, and it can later be edited with a text editor, such as vim with: `vim Doxyfile`. Once we've configured Doxfile the way we want it to be, we can finally type: `doxygen Doxyfile` which will create `html` and `latex` directories, and later, `latex` directory can be used to compile a PDF document from there. 

<u>*Key Doxyfile Settings:*</u>

The Doxyfile uses a variety of settings to configure the documentation generation. Here are some of the key settings:

#### Project Information
-   **`PROJECT_NAME`**: The name of the project.
-   **`PROJECT_NUMBER`**: The version number of the project.

#### Input and Output
-   **`OUTPUT_DIRECTORY`**: The directory where the generated documentation will be placed.
-   **`INPUT`**: Specifies the input files or directories to be processed by Doxygen.
-    **`FILE_PATTERNS`**: Specifies the file patterns to be included in the documentation.
-   **`RECURSIVE`**:  Whether to recursively search for input files in subdirectories.
-   **`HTML_OUTPUT`**: Specifies the directory where the HTML documentation will be placed.
-   **`LATEX_OUTPUT`**: Specifies the directory where the LaTeX documentation will be placed.

#### Extraction Options
-   **`EXTRACT_ALL`**: Whether to extract documentation from all code elements, even if they are not explicitly documented.
-   **`EXTRACT_PRIVATE`**: Whether to extract documentation from private members.
-   **`EXTRACT_STATIC`**: Whether to extract documentation from static members.

#### Preprocessing and Includes
-   **`ENABLE_PREPROCESSING`**: Whether to enable preprocessing of the input files.
-   **`MACRO_EXPANSION`**: Whether to expand macros in the input files.
-   **`SEARCH_INCLUDES`**: Whether to search for include files in the input files.
-   **`INCLUDE_PATH`**: The path to the include files.

#### Other Settings
-   **`IMAGE_PATH`**: The path to the images used in the documentation.
-   **`EXAMPLE_PATH`**: The path to the example files.
-   **`GENERATE_HTML`**: Whether to generate HTML documentation.
-   **`GENERATE_LATEX`**: Whether to generate LaTeX documentation.
-   **`GENERATE_TREEVIEW`**: Whether to generate a tree view of the documentation.

The Doxyfile is central to configuring Doxygen. The `INPUT` setting is used to specify the files or directories to be processed, and the `RECURSIVE` setting is important for projects with subdirectories. The current specified input is "." which means that all files in the current directory will be processed, and the Doxyfile was generated in the root directory. The `FILE_PATTERNS` setting allows for specific file types to be included in the documentation.

---

## GUI

The project includes a graphical user interface (GUI) built using Tkinter. The GUI allows users to select a modulation technique, adjust its parameters, and visualize the modulated signal.

### Features

-   **Modulation Selection:** Users can choose from a variety of modulation techniques using a dropdown menu.
-   **Parameter Adjustment:** The GUI provides input fields for adjusting the parameters of the selected modulation technique.
-   **Signal Visualization:** The GUI displays plots of the message signal, carrier signal, and the modulated signal.
-   **Help Menu:** The GUI includes a help menu that provides information about the program and how to use it.

### GUI Versions

This project includes two versions of the GUI, each with different functionalities and design approaches.

<u>*GUI Version 1*</u>

The first version of the GUI (`GUI/GUI_v1`) is designed to load and run tests for different modulation techniques. It provides a way to select a modulation type, choose a test path (happy or sad path), and run the corresponding tests. This version is more focused on testing the modulation functions rather than visualizing the modulated signals.

#### Features of GUI Version 1

-   **Modulation Selection:** Users can select a modulation technique from a dropdown menu.
-   **Test Path Selection:** Users can choose to run either happy path or sad path tests.
-   **Test Execution:** The GUI runs the selected test and displays a success or error message.
-   **Terminal Output:** Detailed error messages for sad path tests are displayed in the terminal.

#### How to Run GUI Version 1

To run the first version of the GUI, navigate to the `GUI/GUI_v1` directory and execute the `GUI.py` file.

```bash
cd GUI/GUI_v1
python GUI.py
```

<u>*GUI Version 2:*</u>

The second version of the GUI (`GUI/GUI_v2`) is designed to simulate and visualize various modulation techniques. It allows users to select a modulation type, adjust its parameters, and visualize the modulated signal in real-time. This version is more focused on the practical application and visualization of modulation techniques.

#### Features of GUI Version 2

-   **Modulation Selection:** Users can choose from a variety of modulation techniques using a dropdown menu.
-   **Parameter Adjustment:** The GUI provides input fields for adjusting the parameters of the selected modulation technique.
-   **Signal Visualization:** The GUI displays plots of the message signal, carrier signal, and the modulated signal.
-   **Help Menu:** The GUI includes a help menu that provides information about the program and how to use it.

#### How to Run GUI Version 2

To run the second version of the GUI, navigate to the `GUI/GUI_v2` directory and execute the `GUI.py` file.

```bash
cd GUI/GUI_v2
python GUI.py
```

---

## Technologies Used

- **Programming Language:** Python  
- **Libraries:**  
  - `numpy` - Numerical data processing.  
  - `matplotlib` - Visualization of simulation results.  
  - `scipy` - Noise generation and SNR analysis.
  - `pytest` - Testing framework.
  - `coverage` - Code coverage analysis.
  - `tkinter` - GUI framework.
