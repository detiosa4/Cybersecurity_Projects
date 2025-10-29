import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

def scan_port(host, port, t=1.0):
    s = socket.socket()
    s.settimeout(t)
    ok = s.connect_ex((host, port)) == 0
    s.close()
    return port if ok else None

def scan(host, a, b, workers=100):
    print(f"Scanning {host} {a}-{b}...")
    ports = range(max(1, a), min(65535, b) + 1)
    open_ports = []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(scan_port, host, p): p for p in ports}
        for f in as_completed(futs):
            r = f.result()
            if r:
                print(f"[OPEN] {r}")
                open_ports.append(r)
    print("Done.")
    return sorted(open_ports)

if __name__ == "__main__":
    target = input("Enter target host (e.g. scanme.nmap.org or 127.0.0.1): ").strip()
    start_port = int(input("Enter start port (e.g. 1): ").strip())
    end_port = int(input("Enter end port (e.g. 1024): ").strip())
    found = scan(target, start_port, end_port)
    print("Open:", found or "None found")