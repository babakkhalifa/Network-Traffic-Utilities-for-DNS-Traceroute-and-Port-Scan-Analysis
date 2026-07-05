# Network Utility Suite

A Python-based command-line network utility suite for basic network diagnostics and educational security analysis.

## Features

- Display local DNS history
- Resolve hostnames and IP addresses using `nslookup`
- Multithreaded TCP port scanning
- Route tracing using `tracert` / `traceroute`
- Menu-driven interactive interface

## Project Purpose

This project was created as a learning and portfolio project to demonstrate:
- Python scripting
- Socket programming
- Multithreading
- Basic network troubleshooting
- Security awareness

## Important Note

This tool is intended only for:
- educational use
- lab environments
- systems you own
- systems where you have explicit permission to test

Unauthorized scanning or probing may violate policy or law.

## How It Works

The script provides a simple menu with four utilities:

1. **DNS History**
   - Displays the local DNS cache/history on supported systems.

2. **Hostname/IP Resolution**
   - Uses `nslookup` to resolve domain names and IP addresses.

3. **Port Scanner**
   - Scans TCP ports from 1 to 1024 by default.
   - Uses multithreading for better performance.
   - Attempts basic banner grabbing on open ports.

4. **Trace Route**
   - Uses `tracert` on Windows or `traceroute` on Linux/macOS.

## Requirements

- Python 3.x
- Windows, Linux, or macOS
- Terminal access

## Usage
git clone :
```bash
git clone https://github.com/babakkhalifa/Network-Traffic-Utilities-for-DNS-Traceroute-and-Port-Scan-Analysis.git


