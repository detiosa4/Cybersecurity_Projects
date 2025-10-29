# Network Port Scanner

A simple Python tool to scan TCP ports on a target host and list open ports.

## Features

* Scan a range of ports
* Prints open ports in real-time
* Uses threading for faster scanning

## Usage

```bash
python port_scanner.py
```

Follow prompts for host, start port, and end port.

## Example

```
Host: scanme.nmap.org
Start port: 20
End port: 80
[OPEN] 22
[OPEN] 80
Open: [22, 80]
```

## Note

Only scan hosts you own or have permission to test. Educational purposes only.
