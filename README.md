# Coded by ph1n3y

# Port Scanner

A simple port scanner written in Python for penetration testing purposes.

## How to Use

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the port scanner script `python port_scanner.py <target_host> <start_port> <end_port>`.
   - `<target_host>`: The target host to scan.
   - `<start_port>`: The starting port number for scanning.
   - `<end_port>`: The ending port number for scanning.
4. The script will then scan the specified range of ports on the target host and print out open ports.

## Requirements

- Python 3.x
- argparse
- concurrent.futures
- socket

## Disclaimer

This tool is meant for educational and penetration testing purposes only. Unauthorized scanning of systems may be illegal in certain jurisdictions. Use at your own risk.
