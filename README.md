# Advanced Ransomware Simulation

**Note: This project is for educational purposes only. Running this code can cause permanent data loss. Use it responsibly in a controlled and isolated environment, such as a virtual machine.**

## Overview

This repository contains an advanced implementation of a ransomware simulation script. The purpose of this project is to educate cybersecurity professionals about the inner workings of ransomware, including its encryption techniques, propagation methods, anti-debugging measures, and more.

**Disclaimer**: The authors are not responsible for any damages caused by the misuse of this code.

## Features

- **Encryption**: Utilizes the Fernet library to encrypt files in a specified directory using a unique encryption key.
- **Persistence**: Ensures the ransomware script runs automatically upon system startup by adding it to the list of startup programs.
- **Network Propagation**: Copies the ransomware script to available network shares, facilitating its spread across a network.
- **Anti-Debugging and Anti-VM Techniques**: Implements various techniques to detect debugging environments and virtualized systems, making analysis more challenging.
- **Multi-Threading**: Executes multiple functions concurrently using threading, enhancing the efficiency and responsiveness of the ransomware simulation.
- **Ransom Note Generation**: Creates a ransom note file containing instructions for victims, including payment details and warnings.

## Usage

1. **Setup Environment**: Run the code in a controlled and isolated environment, such as a virtual machine, to prevent unintended damage to real data.
2. **Configuration**: Update the paths and settings in the script according to your environment and preferences.
3. **Execution**: Run the main script to initiate the ransomware simulation. Ensure that you have necessary permissions to execute the script and access the specified directories.
4. **Simulation**: Observe the behavior of the ransomware simulation, including encryption of files, propagation across network shares, and generation of a ransom note.
5. **Analysis and Learning**: Use the simulation to study ransomware behavior, understand defense mechanisms, and enhance cybersecurity skills.

## Disclaimer

This project is designed for educational purposes only. Do not use this code for malicious purposes. The authors are not responsible for any damages caused by the misuse of this code.
