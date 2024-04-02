import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

def scan_port(target_host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_host, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except KeyboardInterrupt:
        print("\nExiting...")
        exit()
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting...")
        exit()
    except socket.error:
        print("Couldn't connect to server")
        exit()

def port_scan(target_host, start_port, end_port):
    print(f"Scanning target: {target_host}")
    print("Scanning ports {} to {}".format(start_port, end_port))
    with ThreadPoolExecutor(max_workers=20) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, target_host, port)

def main():
    parser = argparse.ArgumentParser(description="Simple port scanner")
    parser.add_argument("host", help="Target host to scan")
    parser.add_argument("start_port", type=int, help="Starting port number")
    parser.add_argument("end_port", type=int, help="Ending port number")
    args = parser.parse_args()

    target_host = args.host
    start_port = args.start_port
    end_port = args.end_port

    port_scan(target_host, start_port, end_port)

if __name__ == "__main__":
    main()
