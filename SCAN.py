import os
import time
import sys
from datetime import datetime
import threading
import socket


DEFAULT_TIMEOUT = 0.5 
MAX_THREADS = 100     
SCAN_RANGE_START = 1  
SCAN_RANGE_END = 1024 


port_lock = threading.Lock()
open_ports = []
service_info = {} 


def clear_screen():
    if os.name == 'nt': 
        os.system('cls')
    else: 
        os.system('clear')


def scan_port(target_ip, port):
    """
    Tries to connect to a specific port on the target IP.
    If the port is open, it adds it to the open_ports list and attempts to grab service banner.
    """
    try:
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(DEFAULT_TIMEOUT) 
            
            result = sock.connect_ex((target_ip, port))

            if result == 0: 
                with port_lock:
                    open_ports.append(port)
                    print(f"[+] Port {port} is open")

               
                try:
                 
                    sock.send(b"\r\n") 
                    banner = sock.recv(1024).decode('utf-8', errors='ignore').split('\n')[0]
                    if banner:
                        service_info[port] = banner.strip() 
                        print(f"    -> Service banner on port {port}: {service_info[port][:70]}...") # نمایش بخشی از بنر
                    else:
                        service_info[port] = "No Banner Received"
                except Exception as banner_err:
                    service_info[port] = "Banner Error"
                    pass 

    except socket.timeout:
        
        pass
    except socket.error as e:
        
        
        pass
    except Exception as e:
        pass


def run_port_scanner():
    """
    Initializes and runs the port scanner.
    Gets target from user, resolves IP, starts threads, and displays results.
    """
    global open_ports, service_info 
    open_ports = [] 
    service_info = {} 

    clear_screen()
    print("="*60)
    print("           Simple Port Scanner using Python ")
    print("="*60)

    target_host = input("Enter the IP address or hostname to scan: ")

    try:
        target_ip = socket.gethostbyname(target_host)
        print(f"\nScanning target: {target_host} ({target_ip})")
        print(f"Scanning ports from {SCAN_RANGE_START} to {SCAN_RANGE_END}")
        print("Timeout set to:", DEFAULT_TIMEOUT, "seconds per port")
        print(f"Max concurrent threads: {MAX_THREADS}")
        print("-"*60)
    except socket.gaierror:
        print("\n[-] Hostname could not be resolved. Exiting port scanner.")
        return 
    except socket.error:
        print("\n[-] Couldn't connect to the host. Exiting port scanner.")
        return 

    start_time = datetime.now()

    threads = []
    ports_to_scan = range(SCAN_RANGE_START, SCAN_RANGE_END + 1)


    for port in ports_to_scan:
        thread = threading.Thread(target=scan_port, args=(target_ip, port))
        threads.append(thread)
        thread.start()

       
        while threading.active_count() > MAX_THREADS + 1: 
            time.sleep(0.05)

    for thread in threads:
        thread.join()

    end_time = datetime.now()
    total_time = end_time - start_time

    print("\n" + "="*60)
    print("Scan completed.")
    print(f"Target IP: {target_ip}")
    print(f"Total time taken: {total_time}")
    print(f"Found {len(open_ports)} open ports.")

    if open_ports:
        print("\n--- Open Ports ---")
        open_ports.sort()
        for port in open_ports:
            service = service_info.get(port, "Unknown")
            display_service = (service[:60] + '...') if len(service) > 60 else service
            print(f"Port {port:<5} | Status: Open | Service: {display_service}")
    else:
        print("No open ports found in the specified range.")

    print("="*60)
    input("\nPress Enter to return to the main menu...") 

def possibility_1():
    """Scans DNS history."""
    clear_screen()
    print("Waiting to display DNS history...")
    time.sleep(2)
    
    if os.name == 'nt':
        os.system("ipconfig /displaydns")
    else:
        print("DNS history display command is specific to Windows (ipconfig /displaydns).")
        print("For Linux/macOS, you might use 'dig -x +trace google.com' or check system logs.")
    print("\nDNS history display finished.")
    input("Press Enter to return to the main menu...")

def possibility_2():
    """Changes host names to IP and vice-versa using nslookup."""
    clear_screen()
    print("Enter the hostname or IP you want to look up:")
    entry = input("> ")
    print(f"Looking up: {entry}...")
    time.sleep(2)
    os.system(f"nslookup {entry}")
    print("\nLookup finished.")
    input("Press Enter to return to the main menu...")


def possibility_4():
    """Shows router ways to access hosts (IP) using tracert/traceroute."""
    clear_screen()
    print("Enter the hostname or IP to trace its route:")
    entry2 = input("> ")
    print(f"Tracing route to {entry2}...")
    time.sleep(2)
    if os.name == 'nt':
        os.system(f"tracert {entry2}")
    else:
        os.system(f"traceroute {entry2}")
    print("\nRoute tracing finished.")
    input("Press Enter to return to the main menu...")

def main_menu():
    """Displays the main menu and handles user choices."""
    while True:
        clear_screen()
        print("="*60)
        print("           Main Menu - Network Utility Script")
        print("="*60)
        print("1 : Scan DNS History")
        print("2 : Resolve Hostname/IP (nslookup)")
        print("3 : Scan Ports of a Host")
        print("4 : Trace Route to Host")
        print("5 : Exit")
        print("="*60)

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            possibility_1()
        elif choice == '2':
            possibility_2()
        elif choice == '3':
            run_port_scanner() 
        elif choice == '4':
            possibility_4()
        elif choice == '5':
            print("Exiting the script. Goodbye!")
            break 
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
            time.sleep(2)


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nScript interrupted by user. Exiting.")
        sys.exit()
    except Exception as e:
        print(f"\n[-] An unexpected error occurred: {e}")
        sys.exit()
