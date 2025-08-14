import socket, sys

def scan_target(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} open")
            s.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <target> [start_port] [end_port]")
        sys.exit(1)
    target = sys.argv[1]
    start = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    end = int(sys.argv[3]) if len(sys.argv) > 3 else 1024
    scan_target(target, range(start, end+1))
