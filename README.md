## Veleno ARP Spoofing Tool

![poison](https://github.com/ethanlacerenza/Veleno/assets/71321892/3d4c9f37-551f-42f9-b489-746219e8e5c0)
This tool allows you to perform ARP spoofing attacks on a local network to redirect traffic through your machine.

## Requirements

- Python 3
- `netifaces` module
- `scapy` library

You can install the required libraries using pip:


## Usage

1. Run the script `veleno.py`.
2. The script will prompt you to enter the name of the network interface you want to use (e.g., eth0).
3. Once the interface is provided, the script will start sending ARP packets continuously to redirect traffic to your machine.
4. To stop the ARP spoofing attack, you can terminate the script.

## Disclaimer

This tool is intended for educational purposes only. Misuse of this tool may violate local, state, or federal laws. Use it at your own risk.

