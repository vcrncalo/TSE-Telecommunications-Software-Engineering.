# Telecommunication software engineering - Digital transmitter design and signal modulation

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

|Directory name|Description|
|--------------|-----------|
|AM-ASK+tests|This directory contains all code files necessary for AM and ASK modulations, as well as their respective test files.|
|FM-FSK+tests|This directory contains all code files necessary for FM and FSK modulations, as well as their respective test files.|
|PSK-BPSK+tests|This directory contains all code files necessary for PSK and BPSK modulations, as well as their respective test files.|
|QAM-QPSK+tests|This directory contains all code files necessary for QAM and QPSK modulations, as well as their respective test files.|
|README.md|Project details.|

---

## Modulation techniques

### Amplitude Modulation (AM)

**Amplitude Modulation (AM)** is a modulation technique where the amplitude of the carrier signal is varied in proportion to the instantaneous amplitude of the message signal. It's a simple method but is susceptible to noise.

<details>
<summary>Amplitude Modulation (AM) image</summary>
<p align="center">
<img src=AM-ASK+tests/Images/AM_modulation.png>
<br>
Figure 1: Amplitude modulation
</p>
</details>

### Amplitude Shift Keying (ASK)

**Amplitude Shift Keying (ASK)** is a form of amplitude modulation that represents digital data as variations in the amplitude of a carrier wave. In its simplest form, the presence of a carrier wave represents a binary 1, and the absence represents a binary 0.

<details>
<summary>Amplitude Shift Keying (ASK) image</summary>
<p align="center">
<img src=AM-ASK+tests/Images/ASK_modulation.png>
<br>
Figure 2: Amplitude shift keying
</p>
</details>

### Frequency Modulation (FM)

**Frequency Modulation (FM)** is a modulation technique where the frequency of the carrier signal is varied in proportion to the instantaneous amplitude of the message signal. FM is less susceptible to noise than AM.

<details>
<summary>Frequency Modulation (FM) image</summary>
<p align="center">
<img src=FM-FSK+tests/Images/FM_modulation.png>
<br>
Figure 3: Frequency modulation
</p>
</details>

### Frequency Shift Keying (FSK)

**Frequency Shift Keying (FSK)** is a form of frequency modulation that represents digital data as variations in the frequency of a carrier wave. Different frequencies are used to represent different binary values.

<details>
<summary>Frequency Shift Keying (FSK) image</summary>
<p align="center">
<img src=FM-FSK+tests/Images/FSK_modulation.png>
<br>
Figure 4: Frequency shift keying
</p>
</details>

### Phase Shift Keying (PSK)

**Phase Shift Keying (PSK)** is a modulation technique where the phase of the carrier signal is varied to represent digital data. The amplitude and frequency of the carrier signal remain constant.

<details>
<summary>Phase Shift Keying (PSK) image</summary>
<p align="center">
<img src=PSK-BPSK+tests/Images/PSK_modulation.png>
<br>
Figure 5: Phase shift keying
</p>
</details>

### Binary Phase Shift Keying (BPSK)

**Binary Phase Shift Keying (BPSK)** is a form of phase shift keying where the phase of the carrier signal is varied to represent binary data. It uses two phases to represent binary 0 and 1.

<details>
<summary>Binary Phase Shift Keying (BPSK) image</summary>
<p align="center">
<img src=PSK-BPSK+tests/Images/BPSK_modulation.png>
<br>
Figure 6: Binary phase shift keying
</p>
</details>

### Quadrature Amplitude Modulation (QAM)

**Quadrature Amplitude Modulation (QAM)** is a modulation technique that combines both amplitude and phase modulation to transmit more data per symbol. It uses multiple amplitude levels and phase shifts to encode data.

<details>
<summary>Quadrature Amplitude Modulation (QAM) image</summary>
<p align="center">
<img src=QAM-QPSK+tests/Images/QAM_modulation.png>
<br>
Figure 6: Quadrature amplitude modulation
</p>
</details>

### Quadrature Phase Shift Keying (QPSK)

**Quadrature Phase Shift Keying (QPSK)** is a form of phase shift keying where the phase of the carrier signal is varied to represent digital data. It uses four phases to represent two bits of data.

<details>
<summary>Quadrature Phase Shift Keying (QPSK) image</summary>
<p align="center">
<img src=QAM-QPSK+tests/Images/QPSK_modulation.png>
<br>
Figure 7: Quadrature phase shift keying
</p>
</details>

---

## Pytest

*The pytest framework is used to run the tests for each modulation technique. The tests can be run with: `pytest -v --cov 'file.py'`.*

*Figure 8 shows how pytest output looks when running the tests for all the modulation techniques:*

<p align="center">
<img src=Images/Main_coverage.png>
<br>
Figure 8: Code coverage
</p>

---

## Technologies Used

- **Programming Language:** Python  
- **Libraries:**  
  - `numpy` - Numerical data processing.  
  - `matplotlib` - Visualization of simulation results.  
  - `scipy` - Noise generation and SNR analysis. .
  - `pytest` - Testing framework.
  - `coverage` - Code coverage analysis.
