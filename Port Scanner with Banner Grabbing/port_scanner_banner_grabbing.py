import socket


def scan_port(host, port):
    """Scan a single port and try to grab a banner."""
    try:
        # Create a socket
        s = socket.socket()
        s.settimeout(1)  # wait max 1 second
        s.connect((host, port))

        try:
            # Try to receive banner info
            banner = s.recv(1024).decode().strip()
        except:
            banner = "No banner"

        print(f"Port {port} is open: {banner}")
        s.close()
        return True
    except:
        return False


def scan_host(host, start_port, end_port):
    print(f"Scanning {host} from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        scan_port(host, port)


def main():
    host = input("Enter the target IP or domain: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    scan_host(host, start_port, end_port)
    print("\nScan complete.")


if __name__ == "__main__":
    main()
