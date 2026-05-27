# Network-Traffic-Utilities-for-DNS-Traceroute-and-Port-Scan-Analysis
This project is intended for educational and authorized lab use only.
# Network Utility Suite

A simple Python-based command-line network utility suite that provides:

- DNS history display
- Hostname/IP resolution using `nslookup`
- Multithreaded TCP port scanning
- Route tracing with `tracert` / `traceroute`

## Features

- Interactive menu-driven interface
- TCP port scan for ports 1–1024 by default
- Basic banner grabbing for open ports
- Platform-aware DNS history and traceroute commands

## How it works

The project combines basic network utilities and reconnaissance-style checks in a single CLI menu.

### Functions
- **Show DNS history**: displays local DNS cache/history
- **Resolve host**: performs hostname/IP resolution
- **Port scanner**: checks common ports and grabs simple banners
- **Trace route**: shows the path to a target host

## Requirements

- Python 3.x
- Windows or Linux/macOS
- Terminal access

## Usage

Run the script:
```bash
python script2.py
