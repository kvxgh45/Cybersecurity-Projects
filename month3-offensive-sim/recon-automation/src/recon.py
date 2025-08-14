import socket, subprocess, sys
def dns_lookup(domain):
    try:
        return socket.gethostbyname_ex(domain)
    except Exception as e:
        return str(e)
def whois(domain):
    try:
        return subprocess.check_output(["whois", domain], text=True, timeout=15)
    except Exception as e:
        return f"whois error: {e}"
if __name__ == "__main__":
    domain = sys.argv[1] if len(sys.argv)>1 else "example.com"
    print("DNS:", dns_lookup(domain))
    print("WHOIS:", whois(domain)[:1000], "...")
